import requests
import json

class AdvancedDeviceManagement:
    def __init__(self, api_key, api_secret):
        self.api_key = api_key
        self.api_secret = api_secret
        self.base_url = "https://iot.cosmicpi.network/api/v1"

    def get_devices(self):
        headers = {
            "Authorization": "Bearer " + self.api_key,
            "Content-Type": "application/json"
        }
        response = requests.get(self.base_url + "/devices", headers=headers)
        return json.loads(response.content)

    def get_device(self, device_id):
        headers = {
            "Authorization":"Bearer " + self.api_key,
            "Content-Type": "application/json"
        }
        response = requests.get(self.base_url + "/devices/" + device_id, headers=headers)
        return json.loads(response.content)

    def create_device(self, device_name, device_type):
        headers = {
            "Authorization": "Bearer " + self.api_key,
            "Content-Type": "application/json"
        }
        data = {
            "name": device_name,
            "type": device_type
        }
        response = requests.post(self.base_url + "/devices", headers=headers, json=data)
        return json.loads(response.content)

    def update_device(self, device_id, device_name, device_type):
        headers = {
            "Authorization": "Bearer " + self.api_key,
            "Content-Type": "application/json"
        }
        data = {
            "name": device_name,
            "type": device_type
        }
        response = requests.put(self.base_url + "/devices/" + device_id, headers=headers, json=data)
        return json.loads(response.content)

    def delete_device(self, device_id):
        headers = {
            "Authorization": "Bearer " + self.api_key,
            "Content-Type": "application/json"
        }
        response = requests.delete(self.base_url + "/devices/" + device_id, headers=headers)
        return json.loads(response.content)

# Example usage
api_key = "your_api_key"
api_secret = "your_api_secret"
device_management = AdvancedDeviceManagement(api_key, api_secret)

devices = device_management.get_devices()
print("Devices:", devices)

device = device_management.get_device("device_id")
print("Device:", device)

new_device = device_management.create_device("New Device", "Sensor")
print("New Device:", new_device)

updated_device = device_management.update_device("device_id", "Updated Device", "Actuator")
print("Updated Device:", updated_device)

deleted_device = device_management.delete_device("device_id")
print("Deleted Device:", deleted_device)
