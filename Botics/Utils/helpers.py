import requests
from datetime import datetime

class Helpers:
    def __init__(self, bot):
        self.bot = bot

    # 1. Функция для валидации данных
    def is_valid_chat_id(self, chat_id):
        try:
            chat_id = int(chat_id)
            return chat_id > 0
        except ValueError:
            return False

    # 2. Утилиты для работы с временем и датой
    def get_current_timestamp(self):
        return int(datetime.now().timestamp())

    # 3. Функции для форматирования данных
    def format_message(self, user_name, text):
        return f"{user_name}: {text}"

    # 4. Функции для отправки уведомлений или сообщений (пример отправки уведомления)
    def send_notification(self, chat_id, message):
        try:
            url = f"https://api.telegram.org/bot{self.bot.BOT_TOKEN}/sendMessage"
            payload = {"chat_id": chat_id, "text": message}
            response = requests.post(url, json=payload)
            response.raise_for_status()
            print(f"Sent message to {chat_id}: {message}")
        except Exception as e:
            self.handle_error(f"Failed to send message: {str(e)}")

    # 5. Утилиты для обработки ошибок и исключений
    def handle_error(self, error_message):
        print(f"Error: {error_message}")
