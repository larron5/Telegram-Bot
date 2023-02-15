import telebot
import re
import random


bot = telebot.TeleBot('1492500655:AAHPIGrmzY-rgT8VlyPzJ1z0SGuZVS-gutU')
@bot.message_handler(commands=['start'])
def start(message):
	bot.reply_to(message, '/AO\nPERMINTAAN: Pelurusan & Asign \nSC: \nNO INET: \nSN ONT: \nSN STB: \nCREW: F5SDAS99 \nNIK: 16972844 \nMitra: PT. CDM\nValins ID: \nTime: \nSummary ODP: \nIP OLT: \nSlot: \nPort: ')

print('bot is running')
bot.polling()