# -*- coding: utf-8 -*-
import logging
import ssl
import telebot
from telebot import types
from aiohttp import web
import const

API_TOKEN = const.TOKEN

WEBHOOK_HOST = 'ip/domen' #Подставьте IP/domen вашего сервера
WEBHOOK_PORT = 8443 #Вебхуки используют один из портов: 8443, 443, 80, 88. Используемый порт должен быть открыт.
WEBHOOK_LISTEN = '0.0.0.0' #При использовании некоторых VPS серверов нужно указать свой IP

WEBHOOK_SSL_CERT = './webhook_cert.pem' #Путь до SSL сертификата.
WEBHOOK_SSL_PRIV = './webhook_pkey.pem' #Путь до приватного SSL ключа.

#Если у вас нет SSL сертификата, его можно создать (самоподписанный), команды:
#openssl genrsa -out webhook_pkey.pem 2048
#openssl req -new -x509 -days 3650 -key webhook_pkey.pem -out webhook_cert.pem
#В поле "Common Name (e.g. server FQDN or YOUR name)" укажите такое же значение как и в WEBHOOK_HOST

WEBHOOK_URL_BASE = "https://{}:{}".format(WEBHOOK_HOST, WEBHOOK_PORT)
WEBHOOK_URL_PATH = "/{}/".format(API_TOKEN)

logger = telebot.logger
telebot.logger.setLevel(logging.INFO)

bot = telebot.TeleBot(API_TOKEN)

app = web.Application()

bot = telebot.TeleBot(API_TOKEN)

async def handle(request):
    if request.match_info.get('token') == bot.token:
        request_body_dict = await request.json()
        update = telebot.types.Update.de_json(request_body_dict)
        bot.process_new_updates([update])
        return web.Response()
    else:
        return web.Response(status=403)

app.router.add_post('/{token}/', handle)

@bot.message_handler(content_types=["text"])
def send_welcome(message):
    markup_inline_main = types.InlineKeyboardMarkup(row_width=1)
    btn_rus = types.InlineKeyboardButton('🇷🇺 Россия', callback_data='rus')
    btn_ukr = types.InlineKeyboardButton('🇺🇦 Украина', callback_data='ukr')
    btn_kz = types.InlineKeyboardButton('🇰🇿 Казахстан', callback_data='kz')

    markup_inline_main.add(btn_rus, btn_ukr, btn_kz)

    bot.send_message(
        chat_id=message.chat.id,
        text= "*Привет, " + message.from_user.first_name + "!*"+ const.main_text,
        reply_markup=markup_inline_main,
        parse_mode="Markdown"
    )


@bot.callback_query_handler(func=lambda call: True)
def call_back_main(call):
    if call.data == 'back':  # Кнопка назад
        markup_inline_main = types.InlineKeyboardMarkup(row_width=1)
        btn_rus = types.InlineKeyboardButton('🇷🇺 Россия', callback_data='rus')
        btn_ukr = types.InlineKeyboardButton('🇺🇦 Украина', callback_data='ukr')
        btn_kz = types.InlineKeyboardButton('🇰🇿 Казахстан', callback_data='kz')

        markup_inline_main.add(btn_rus, btn_ukr, btn_kz)

        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text= const.main_text,
            reply_markup=markup_inline_main,
            parse_mode="Markdown"
        )

    elif call.data == 'rus':  # Кнопка RUS
        keyboard = types.InlineKeyboardMarkup()

        back_button = types.InlineKeyboardButton('⏪ Назад', callback_data='back')
        sup_button = types.InlineKeyboardButton('⁉ Поддержка', "https://t.me/@byware")
        zaim0_button = types.InlineKeyboardButton('🔥 Займы под 0%', callback_data='zaim')
        nojob_button = types.InlineKeyboardButton('📓 Безработным и с просрочкой', callback_data='nojob')
        firstzaim_button = types.InlineKeyboardButton('🆕 Первый займ', callback_data='firstzaim')

        keyboard.row(zaim0_button)
        keyboard.row(nojob_button)
        keyboard.row(firstzaim_button)
        keyboard.row(back_button, sup_button)

        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text=const.country_text,
            reply_markup=keyboard,
            parse_mode="Markdown"
        )

    elif call.data == 'ukr':  # Кнопка UKR
        keyboard = types.InlineKeyboardMarkup()

        back_button = types.InlineKeyboardButton('⏪ Назад', callback_data='back')
        sup_button = types.InlineKeyboardButton('⁉ Поддержка', "https://t.me/@byware")
        zaim0_button = types.InlineKeyboardButton('🔥 Займы под 0%', callback_data='zaim')
        nojob_button = types.InlineKeyboardButton('📓 Безработным и с просрочкой', callback_data='nojob')
        firstzaim_button = types.InlineKeyboardButton('🆕 Первый займ', callback_data='firstzaim')

        keyboard.row(zaim0_button)
        keyboard.row(nojob_button)
        keyboard.row(firstzaim_button)
        keyboard.row(back_button, sup_button)

        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text=const.country_text,
            reply_markup=keyboard,
            parse_mode="Markdown"
        )

    elif call.data == 'kz':  # Кнопка KZ
        keyboard = types.InlineKeyboardMarkup()

        back_button = types.InlineKeyboardButton('⏪ Назад', callback_data='back')
        sup_button = types.InlineKeyboardButton('⁉ Поддержка', "https://t.me/@byware")
        zaim0_button = types.InlineKeyboardButton('🔥 Займы под 0%', callback_data='zaim')
        nojob_button = types.InlineKeyboardButton('📓 Безработным и с просрочкой', callback_data='nojob')
        firstzaim_button = types.InlineKeyboardButton('🆕 Первый займ', callback_data='firstzaim')

        keyboard.row(zaim0_button)
        keyboard.row(nojob_button)
        keyboard.row(firstzaim_button)
        keyboard.row(back_button, sup_button)

        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text=const.country_text,
            reply_markup=keyboard,
            parse_mode="Markdown"
        )

bot.remove_webhook()

bot.set_webhook(url=WEBHOOK_URL_BASE + WEBHOOK_URL_PATH,
                certificate=open(WEBHOOK_SSL_CERT, 'r'))

context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
context.load_cert_chain(WEBHOOK_SSL_CERT, WEBHOOK_SSL_PRIV)

web.run_app(
    app,
    host=WEBHOOK_LISTEN,
    port=WEBHOOK_PORT,
    ssl_context=context,
)