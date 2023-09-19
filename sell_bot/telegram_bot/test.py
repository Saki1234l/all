import requests

# Замените на свой токен бота
bot_token = '5880554308:AAEwK5ePaVVvlGNBLzeXbXPce2RsQgJI5Os'

# Замените на chat_id, куда вы хотите отправить сообщение
chat_id = '5978553388'

# URL вашего веб-приложения
web_app_url = "https://www.instagram.com"

# Создание объекта WebAppInfo
web_app_info = {
    "url": web_app_url
}


# Текст сообщения
message_text = 'Выберите действие:'

# URL для отправки сообщения через API Telegram
url = f'https://api.telegram.org/bot{bot_token}/sendMessage'

# Клавиатура с инлайн-кнопкой
keyboard = {
    'inline_keyboard': [[{'text': 'Нажми меня', 'web_app': web_app_info}]]
}

# Опции сообщения, включая клавиатуру
message_options = {
    'chat_id': chat_id,
    'text': message_text,
    'reply_markup': keyboard
}

print(message_options)

# Отправляем запрос на отправку сообщения
response = requests.post(url, json=message_options)

# Печатаем результат запроса
print(response.text)
