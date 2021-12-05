from ast import parse
import telebot
from telebot.types import Update
from constants import API_KEY


bot= telebot.TeleBot(API_KEY, parse_mode=None)


@bot.message_handler(commands=["hello","start","hi"])
def send_help_message(Update,message):
    bot.reply_to(message, "Type in your reply")



bot.polling()

if __name__ == '__bot__':
    bot()




