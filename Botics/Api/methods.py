import requests
from ..Types import InlineKeyboard, Keyboard, Message

class Methods:
    def __init__(self, bot):
        self.base_url = bot.base_url

    def send_message(self, chat_id, text, keyboard=None):
        url = f"{self.base_url}/sendMessage"
        payload = {"chat_id": chat_id, "text": text}
        
        if keyboard:
            payload["reply_markup"] = keyboard.serialize()

        response = requests.post(url, json=payload)
        response.raise_for_status()
        return response.json()

    def send_photo(self, chat_id, photo, caption=None, keyboard=None):
        url = f"{self.base_url}/sendPhoto"
        payload = {"chat_id": chat_id}

        if caption:
            payload["caption"] = caption

        files = {"photo": (photo.file_id, requests.get(photo.file_id).content)}

        response = requests.post(url, data=payload, files=files)
        response.raise_for_status()
        return response.json()

    def send_video(self, chat_id, video, duration=None, caption=None, keyboard=None):
        url = f"{self.base_url}/sendVideo"
        payload = {"chat_id": chat_id}
        
        if duration:
            payload["duration"] = duration
        
        if caption:
            payload["caption"] = caption

        files = {"video": (video.file_id, requests.get(video.file_id).content)}

        response = requests.post(url, data=payload, files=files)
        response.raise_for_status()
        return response.json()

    # Методы для изменения сообщений
    def edit_text(self, chat_id, message_id, text, keyboard=None):
        url = f"{self.base_url}/editMessageText"
        payload = {"chat_id": chat_id, "message_id": message_id, "text": text}
        
        if keyboard:
            payload["reply_markup"] = keyboard.serialize()

        response = requests.post(url, json=payload)
        response.raise_for_status()
        return response.json()

    def edit_video(self, chat_id, message_id, video, duration=None, caption=None, keyboard=None):
        url = f"{self.base_url}/editMessageMedia"
        payload = {"chat_id": chat_id, "message_id": message_id, "media": {"type": "video", "media": video.file_id}}
        
        if duration:
            payload["media"]["duration"] = duration
        
        if caption:
            payload["media"]["caption"] = caption

        response = requests.post(url, json=payload)
        response.raise_for_status()
        return response.json()

    def edit_photo(self, chat_id, message_id, photo, caption=None, keyboard=None):
        url = f"{self.base_url}/editMessageMedia"
        payload = {"chat_id": chat_id, "message_id": message_id, "media": {"type": "photo", "media": photo.file_id}}
        
        if caption:
            payload["media"]["caption"] = caption

        response = requests.post(url, json=payload)
        response.raise_for_status()
        return response.json()
    
    # Удаление сообщения
    def delete_message(self, chat_id, message_id):
        url = f"{self.base_url}/deleteMessage"
        payload = {"chat_id": chat_id, "message_id": message_id}

        response = requests.post(url, json=payload)
        response.raise_for_status()
        return response.json()