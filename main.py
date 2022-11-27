import telebot
import random
from time import sleep

TOKEN = "5903094799:AAEj0CrNb6hbjBsfiE-uA3yfKGuakWJHyLk"
bot = telebot.TeleBot(TOKEN)
#Команда
@bot.message_handler(commands=["start"])
def start(message):
        bot.send_message(message.chat.id, "Я бот созданный Александром Дерябиным , правда пока без функционала")


#вывести текст в ответ на сообщения
@bot.message_handler(content_types=['text'])
def text(message):
    if message.text.lower() == "привет":
        bot.send_message(message.chat.id, "О привет чувак! ")
    elif message.text == "Аскар":
        bot.send_message(message.chat.id, "Братан я начал писать бота !")






bot.polling()