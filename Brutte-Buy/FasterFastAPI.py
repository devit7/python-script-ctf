import httpx
import time

URL = "http://64.227.131.98:40000"

class BaseAPI:
    def __init__(self, url=URL):
        self.client = httpx.Client(base_url=url)

class API(BaseAPI):
    def buy(self, token, item_id, quantity, lucky_number):
        data = [{"item_id": item_id, "quantity": quantity, "lucky_number": lucky_number}]
        response = self.client.post("/api/buy", json=data, params={"token": token})
        return response



# Example usage
api_instance = API()

for _ in range(100):
    response = api_instance.buy(token="zwb76i", item_id="lottery_coupon", quantity=0, lucky_number=809448)
    print(response.status_code)
    print(response.text)
    time.sleep(0.1)  # Sleep for 100ms
