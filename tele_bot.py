import telebot
#import config
import random
import json
from telebot import types
from firebase_admin import db
import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("olimp.json")
firebase_admin.initialize_app(cred,{'databaseURL':'https://olimp-7f50b-default-rtdb.firebaseio.com/'})
ref = db.reference('/')
with open("1.json", "r") as f:
	file_contents = json.load(f)

bot = telebot.TeleBot('5562799797:AAF-KC1dtROvrzgsVR4aYHbQOj-xPWjo0Sk')

@bot.message_handler(commands=['start'])
def welcome(message):
	# keyboard
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1 = types.KeyboardButton("🎲 Рандомное число")
	item2 = types.KeyboardButton("😊 Как дела?")
	item3 = types.KeyboardButton("Занести в базу")

	markup.add(item1, item2,item3)

	bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот созданный чтобы быть подопытным кроликом.".format(message.from_user, bot.get_me()),
		parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def lalala(message):
	if message.chat.type == 'private':
		if message.text == '🎲 Рандомное число':
			bot.send_message(message.chat.id, str(random.randint(0,100)))
		elif message.text == '😊 Как дела?':

			markup = types.InlineKeyboardMarkup(row_width=2)
			item1 = types.InlineKeyboardButton("Хорошо", callback_data='good')
			item2 = types.InlineKeyboardButton("Не очень", callback_data='bad')

			markup.add(item1, item2)

			bot.send_message(message.chat.id, 'Отлично, сам как?', reply_markup=markup)
		elif message.text == 'Занести в базу':
			chislo = random.randint(0,100)
			ref.set({
						'User2':
								{
								 	'login' : 'Leonid',
									'pasword' : '123456789'
								}
					}
					)

		else:
			bot.send_message(message.chat.id, 'Я не знаю что ответить 😢')

# RUN
bot.polling(none_stop=True)
