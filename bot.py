import const
import telebot
from telebot import types
# from telebot import apihelper

# apihelper.proxy = {'http':'http://109.70.189.56:48774'}

bot = telebot.TeleBot(const.TOKEN)

@bot.message_handler(content_types=["text"])
def send_welcome(message):
	markup_inline_main = types.InlineKeyboardMarkup(row_width=1)
	btn_can = types.InlineKeyboardButton('💎 Что я умею? 💎', callback_data='can')
	btn_work = types.InlineKeyboardButton('💵 Начать зарабатывать 💵', callback_data='work')
	btn_friends = types.InlineKeyboardButton('👥 Пригласить друзей 👥', "https://t.me/share/url?url=t.me/breadheadbot?start=" + str(message.from_user.id) + "&text=#хлебушкахочешь?")
	btn_balance = types.InlineKeyboardButton('💲 Проверить баланс 💲', callback_data='balance')

	markup_inline_main.add(btn_can, btn_work, btn_friends, btn_balance)

	bot.send_message(
		chat_id=message.chat.id, 
		text="*Привет, "+ message.from_user.first_name + "!*\nТы можешь выполнять задания, либо приглашать друзей и зарабатывать на этом 💸\n*Используй навигационное меню ниже⬇️*", 
		reply_markup=markup_inline_main,
		parse_mode = "Markdown"
	)

@bot.callback_query_handler(func=lambda call:True)
def call_back_main(call):
	if call.data == 'back': #Кнопка назад
		markup_inline_main = types.InlineKeyboardMarkup(row_width=1)
		btn_can = types.InlineKeyboardButton('💎 Что я умею? 💎', callback_data='can')
		btn_work = types.InlineKeyboardButton('💵 Начать зарабатывать 💵', callback_data='work')
		btn_friends = types.InlineKeyboardButton('👥 Пригласить друзей 👥', "https://t.me/share/url?url=t.me/breadheadbot?start=" + str(call.message.from_user.id) + "&text=#хлебушкахочешь?")
		btn_balance = types.InlineKeyboardButton('💲 Проверить баланс 💲', callback_data='balance')

		markup_inline_main.add(btn_can, btn_work, btn_friends, btn_balance)

		bot.edit_message_text(
			chat_id=call.message.chat.id,
			message_id=call.message.message_id, 
			text="Ты можешь выполнять задания, либо приглашать друзей и зарабатывать на этом 💸\n*Используй навигационное меню ниже⬇️*", 
			reply_markup=markup_inline_main,
			parse_mode = "Markdown"
		)

	elif call.data == 'can': #Кнопка что я умею
		keyboard = types.InlineKeyboardMarkup(row_width=1)

		back_button = types.InlineKeyboardButton('⏪ Назад', callback_data='back')

		keyboard.add(back_button)

		bot.edit_message_text(
			chat_id=call.message.chat.id,
			message_id=call.message.message_id,
			text="_Средняя стоимость буханки хлеба 30 рублей - именно столько я выплачиваю своим партнёрам за одного приглашенного друга!\nСколько хлеба ты сможешь унести? Проверим?_\n*Твоя ссылка для приглашения:* t.me/breadheadbot?start=" + str(call.message.from_user.id),
			reply_markup=keyboard,
			parse_mode="Markdown"
		)

	elif call.data == 'work': #Кнопка начать зарабатывать
		keyboard = types.InlineKeyboardMarkup(row_width=1)

		back_button = types.InlineKeyboardButton('⏪ Назад', callback_data='back')

		keyboard.add(back_button)

		bot.edit_message_text(
			chat_id=call.message.chat.id,
			message_id=call.message.message_id,
			text="*К сожалению, на данный момент нет актуальных заданий. Попробуй позже😔*",
			reply_markup=keyboard,
			parse_mode="Markdown"
		)

	elif call.data == 'balance': #Кнопка проверить баланс
		keyboard = types.InlineKeyboardMarkup(row_width=1)

		back_button = types.InlineKeyboardButton('⏪ Назад', callback_data='back')

		keyboard.add(back_button)

		bot.edit_message_text(
			chat_id=call.message.chat.id,
			message_id=call.message.message_id,
			text="*К сожалению, на данный момент нет актуальных заданий. Попробуй позже😔*",
			reply_markup=keyboard,
			parse_mode="Markdown"
		)

	

# @bot.message_handler(commands=['start', 'help'])
# def send_welcome(message):
# 	bot.send_message(message.chat.id, 'Привет, я бот интернет-магазина Эталон-БТ', reply_markup=markup_menu)

# @bot.message_handler(content_types=['text'])
# def answer_types(message):
# 	if 'О нас' in message.text:
# 		bot.send_message(message.chat.id, const.about_text)
# 		return
# 	elif 'Способы оплаты' in message.text:
# 		bot.send_message(message.chat.id, const.pay_text)
# 		return
# 	elif 'Способы доставки' in message.text:
# 		bot.send_message(message.chat.id, const.delivery_text)
# 		return
# 	elif 'Пункты самовывоза' in message.text:
# 		bot.send_message(message.chat.id, const.pickup_text)
# 		return

bot.polling()