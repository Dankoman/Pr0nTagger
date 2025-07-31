# Client for interacting with the Stash API to send images and clear temporary files.
# This client uses the requests library to handle HTTP requests to the Stash API.
import requests

class StashAPIClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def send_image(self, image_path):
        with open(image_path, 'rb') as image_file:
            files = {'image': image_file}
            response = requests.post(f"{self.base_url}/", files=files)
            return response.json()

    def clear_temp_files(self):
        response = requests.post(f"{self.base_url}/clear_temp")
        return response.json()