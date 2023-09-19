import requests
import json

class Botics:
    def __init__(self, token):
        self.token = token
        self.url = f"https://api.telegram.org/bot{self.token}"
        url = f"{self.url}/getMe"
        response = requests.get(url)
        result = response.json()
        bot_username = result['result']['username']
        bot_name = result['result']['first_name']
        bot_id = result['result']['id']
        
        print(f"Bot has started successfully.")
        print(f"Bot Name: {bot_name}")
        print(f"Username: @{bot_username}")
        print(f"Bot ID: {bot_id}")

    @property
    def base_url(self):
        return self.url