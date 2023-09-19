from Botics.Types import InlineButton, Web_Info, InlineKeyboard

in_button1 = InlineButton('🧲 Получить ссылку 🧲', callback_data='button1')
in_button2 = InlineButton('❗️ Правилы игры ❗️', callback_data='button2')
in_button2 = Web_Info(url="https://www.mytgbottestsell.pp.ua/")

in_menu1 = InlineKeyboard().add(in_button1).add(in_button2).add(web_app3)