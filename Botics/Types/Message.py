class Message:
    def __init__(self, message_id, chat_id, text=None, keyboards=None):
        self.message_id = message_id
        self.chat_id = chat_id
        self.text = text
        self.keyboards = keyboards