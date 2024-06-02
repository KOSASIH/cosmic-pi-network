import requests
import json

class SatelliteIntegration:
    def __init__(self, api_key, api_secret):
        self.api_key = api_key
        self.api_secret = api_secret
        self.base_url = "https://satellite.cosmicpi.network/api/v1"

    def get_satellite_data(self, satellite_id):
        headers = {
            "Authorization": "Bearer " + self.api_key,
            "Content-Type": "application/json"
        }
        response = requests.get(self.base_url + "/satellites/" + satellite_id, headers=headers)
        return json.loads(response.content)

    def send_command(self, satellite_id, command):
        headers = {
            "Authorization": "Bearer " + self.api_key,
            "Content-Type": "application/json"
        }
        data = {
            "command": command
        }
        response = requests.post(self.base_url + "/satellites/" + satellite_id + "/commands", headers=headers, json=data)
        return json.loads(response.content)

# Example usage
api_key = "your_api_key"
api_secret = "your_api_secret"
integration = SatelliteIntegration(api_key, api_secret)

satellite_data = integration.get_satellite_data("satellite_id")
print("Satellite Data:", satellite_data)

command_response = integration.send_command("satellite_id", "take_photo")
print("Command Response:", command_response)
