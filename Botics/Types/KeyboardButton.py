class KeyboardButton:
    def __init__(self, text=None, url=None, web_app=None):
        if web_app:
            self.text = text
            self.web_app = web_app
        elif url:
            self.text = text
            self.url = url
        else:
            self.text = text
            self.url = url