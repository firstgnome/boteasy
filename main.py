import telebot

bot = telebot.TeleBot('5880558659:AAFawynnjD0fEDXibgSe_Ym-QIBsWbMH0eU')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Hello, I am your Telegram Bot!')

bot.polling()