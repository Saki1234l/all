import requests
from collections import namedtuple
from ..Types import Message, Command

class Botics_Dispatcher:
    def __init__(self, bot):
        print(f"Dispatcher has started successfully.")
        self.bot_url = bot.base_url
        self.session = requests.Session()
        self.handlers = []
        self.last_update_id = 0

    def message(self, text=None, command=None):
        def decorator(func):
            def handler(*args, **kwargs):

                if text and text in args[0].text:
                    func(*args, **kwargs)

                elif command and args[0].text.startswith(command):
                    func(*args, **kwargs)

            self.handlers.append(handler)
            return handler

        return decorator

    def get_updates(self, offset=0):
        response = self.session.get(f'{self.bot_url}/getUpdates?offset={offset}')
        if response.status_code == 200:
            return response.json().get('result', [])
        return []

    def process_message(self, message):
        for handler in self.handlers:
            handler(message)

    def main_loop(self):
        while True:
            try:
                updates = self.get_updates(offset=self.last_update_id + 1)
                for update in updates:
                    update_id = update.get('update_id')
                    if update_id > self.last_update_id:
                        self.last_update_id = update_id
                        message_data = update.get('message')
                        if 'text' in message_data:
                            message_text = message_data.get('text')
                            if message_text[0] == '/':
                                command  = Command(
                                    text=message_data.get('text'),
                                    chat_id=message_data['from']['id'],
                                    message_id=message_data['message_id']
                                )
                                self.process_message(command)

                            else:
                                message = Message(
                                    text=message_data.get('text'),
                                    chat_id=message_data['from']['id'],
                                    message_id=message_data['message_id']
                                )
                                self.process_message(message)

            except Exception as error:
                print(f'ошибка: {error}')