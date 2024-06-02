
**src/cosmic_pi_network/api/api.py**
```python
import requests
from requests.structures import CaseInsensitiveDict

class API:
    def __init__(self):
        pass

    def send_request(self, method, url, headers=None, params=None, data=None):
        response = requests.request(method, url, headers=headers, params=params, data=data)
        return response

    def get_weather(self, city):
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=your_api_key"
        response = self.send_request("GET", url)
        weather_data = response.json()
        return weather_data

# Example usage
api = API()
weather_data = api.get_weather("New York")
print("Weather data:", weather_data)
