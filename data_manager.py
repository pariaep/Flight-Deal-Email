import requests
SHEETY_ENDPOINT = "https://api.sheety.co/yourKey/flightDeals/sheet1"
class DataManager:
    def __init__(self):
        self.destination_data = {}
        self.customer_data = {}

    def get_destination_data(self):
        headers = {
            "Authorization": f"Your-Code",
            "Content-Type": "application/json",
        }
        response = requests.get(url=SHEETY_ENDPOINT, headers=headers)
        response.raise_for_status()
        data = response.json()
        self.destination_data = data["sheet1"]
        return self.destination_data

    def update_destination_code(self):
        headers = {
            "Authorization": f"Your-Code",
            "Content-Type": "application/json",
        }
        for city in self.destination_data:
            new_data = {
                "sheet1": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(url=f"{SHEETY_ENDPOINT}/{city['id']}", json=new_data, headers=headers)
            print(response.text)

    def get_customer_emails(self):
        customer_endpoint = "https://api.sheety.co/ba2f4cb14847ab681367f2673455283f/flightDeals/sheet2"
        headers = {
            "Authorization": "Your-Code",
            "Content-Type": "application/json",
        }
        response = requests.get(customer_endpoint, headers=headers)
        data = response.json()
        self.customer_data = data["sheet2"]
        return self.customer_data
