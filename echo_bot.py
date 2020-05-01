import telebot

bot = telebot.TeleBot("956859724:AAGKGD4ljSOEKlbYoC3H6BMMLDqVCCCEVGE")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Hello! How are you doing?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.polling()