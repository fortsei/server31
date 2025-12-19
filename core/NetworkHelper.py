import requests

class HotelAPI:
    BASE_URL = "http://127.0.0.1:8001/api/guests/"

    @staticmethod
    def get_guests():
        response = requests.get(HotelAPI.BASE_URL)
        return response.json()

    @staticmethod
    def delete_guest(guest_id):
        url = f"{HotelAPI.BASE_URL}{guest_id}/"
        return requests.delete(url)
