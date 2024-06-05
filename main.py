from data_manager import DataManager
from flight_search import FlightSearch
from datetime import datetime, timedelta
from notification_manager import NotificationManager

ORIGIN_CITY_IATA = "DFW"
notification_manager = NotificationManager()
flight_search = FlightSearch()
data_manager = DataManager()
sheet_data = data_manager.get_destination_data()

if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    print(f"sheet_data:\n {sheet_data}")

    data_manager.destination_data = sheet_data
    data_manager.update_destination_code()

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=180)

for destination in sheet_data:
    flight = flight_search.check_flights(ORIGIN_CITY_IATA, destination["iataCode"],
                                         from_time=tomorrow, to_time=six_month_from_today)

    if flight is None:
        continue

    if flight.price < destination["lowestPrice"]:
        users = data_manager.get_customer_emails()
        emails = [row["email"] for row in users]
        names = [row["firstName"] for row in users]
        message = (f"Low price alert! Only ${flight.price} to fly from{flight.origin_city}-{flight.origin_airport} to "
                   f"{flight.destination_city}-{flight.destination_airport}")

        notification_manager.send_email(emails, message)
