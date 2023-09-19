from Botics import Botics_Dispatcher 
from Botics import Botics
from Botics import Methods
from config import api_token
from modules import keyboards

bot = Botics(token=api_token)
dp = Botics_Dispatcher(bot)
sp = Methods(bot)

@dp.message(text="/start")
def handle_start_command(message):
    sp.send_message(message.chat_id, 'привет', keyboard=keyboards.in_menu1)

@dp.message(command='/help')
def handle_command(message):
    sp.send_message(message.chat_id, message.text)

@dp.message(text='hello')
def handle_command(message):
    sp.send_message(message.chat_id, message.text, reply_ma)

if __name__ == "__main__":
    dp.main_loop()