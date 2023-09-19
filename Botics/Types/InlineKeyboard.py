class InlineKeyboard:
    def __init__(self, buttons=None):
        self.Keyboard = []
        if buttons:
            self.Keyboard.append(buttons)

    def add(self, button):
        self.Keyboard.append(button)