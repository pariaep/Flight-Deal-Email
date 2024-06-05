import requests
from flight_data import FlightData
TEQ_ENDPOINT = "https://tequila-api.kiwi.com"
TEQ_API_KEY = "tey4ymh-jRsXNr3-tUMglWL9ZnqOGfsm"
class FlightSearch:
    def get_destination_code(self, city):
        location_endpoint = f"{TEQ_ENDPOINT}/locations/query"
        headers = {"apikey": TEQ_API_KEY}
        query = {"term": city, "location_type": "city"}
        response = requests.get(url=location_endpoint, headers=headers, params=query)
        response.raise_for_status()
        results = response.json()["locations"]
        code = results[0]["code"]
        return code

    def check_flights(self, origin_code, destination_code, from_time, to_time):
        headers = {"apikey": TEQ_API_KEY}
        query = {
            "fly_from": origin_code,
            "fly_to": destination_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 3,
            "nights_in_dst_to": 7,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 1,
            "curr": "USD"
        }
        response = requests.get(url=f"{TEQ_ENDPOINT}/v2/search", headers=headers, params=query)
        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {destination_code}.")
            return None

        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )
        print(f"{flight_data.destination_city}: ${flight_data.price}")
        return flight_data