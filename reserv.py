import telebot
from telebot import types


# ARA_HppyBot
bot = telebot.TeleBot('1233673851:AAGsrdlN5LjaRnL_Eea5Pc3bEdCyBZfddbg')


# Меню тестов
keyboard2 = telebot.types.InlineKeyboardMarkup(True)
keyboard2.add(types.InlineKeyboardButton(text='Шкала субъективного благополучия Динера', callback_data='start_diner'))
keyboard2.add(
    types.InlineKeyboardButton(text='Шкала субъективной оценки жизненной энергии', callback_data='start_vital'))

# ТЕСТ ДИНЕРА

# Меню ответов теста Динера (1-7)
keyboard3 = telebot.types.InlineKeyboardMarkup(True)
keyboard3.add(types.InlineKeyboardButton(text='1', callback_data='sel1'))
keyboard3.add(types.InlineKeyboardButton(text='2', callback_data='sel2'))
keyboard3.add(types.InlineKeyboardButton(text='3', callback_data='sel3'))
keyboard3.add(types.InlineKeyboardButton(text='4', callback_data='sel4'))
keyboard3.add(types.InlineKeyboardButton(text='5', callback_data='sel5'))
keyboard3.add(types.InlineKeyboardButton(text='6', callback_data='sel6'))
keyboard3.add(types.InlineKeyboardButton(text='7', callback_data='sel7'))

# Вопросы к тесту Динера
dyn_qst = [
    '1. В целом моя жизнь близка к идеалу.',
    '2. Условия моей жизни прекрасные.',
    '3.	Я удовлетворен жизнью.',
    '4.	К настоящему моменту я уже получил от жизни всё, чего хотел.',
    '5.	Если я мог прожить жизнь заново, то не изменил бы почти ничего.'
]
qn = 0


@bot.message_handler(commands=['start', 'tests', 'practices'])
def start_message(message):
    if message.text == '/start':
        # Меню первого уровня
        keyboard1 = types.InlineKeyboardMarkup()
        key1 = types.InlineKeyboardButton(text='Тесты', callback_data='starttests')
        keyboard1.add(key1)
        key2 = types.InlineKeyboardButton(text='Практики', callback_data='startpract')
        keyboard1.add(key2)
        bot.send_message(message.from_user.id, 'Привет, ты написал мне /start', reply_markup=keyboard1)
        print(message)
    elif message.text == '/tests':
        bot.send_message(message.from_user.id, 'Выполним тесты', reply_markup=keyboard2)
    elif message.text == '/practices':
        bot.send_message(message.from_user.id, 'Перейдём к практикам', reply_markup=keyboard3)
    else:
        print(message)


# Обработчики нажатий на кнопки
# @bot.callback_query_handler(func=lambda call: call.data == 'start_diner')
# def callback_diner(call):
#    msg = 'Тест Динера показывает уровень субъективного благополучия.\n' + 'Тест содержит 5 вопросов'
#    bot.send_message(call.message.chat.id, msg)

# @bot.callback_query_handler(func=lambda call: call.data == 'start_vital')
# def callback_vital(call):
#    msg = 'Шкала субъективной оценки жизненной энергии Subjective Vitality Scale (Ryan, R. M., & Frederick, C. M., 1997).\n' + 'Тест содержит 6 вопросов'
#    bot.send_message(call.message.chat.id, msg)

# @bot.callback_query_handler(func=lambda call: call.data == 'start_test')
# def callback_tests(call):
#    bot.send_message(call.message.chat.id, 'Вы перешли в раздел с тестами', reply_markup=keyboard2)

# @bot.callback_query_handler(func=lambda call: call.data == 'start_pract')
# def callback_pract(call):
#    bot.send_message(call.message.chat.id, 'Вы перешли в раздел с практиками', reply_markup=keyboard2)


# Команда /help
@bot.message_handler(commands=['help'])
def help_command(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(
        telebot.types.InlineKeyboardButton(
            'Связаться с автором', url='telegram.me/Foodfox_Andrey_Ralko'
        )
    )
    bot.send_message(
        message.chat.id,
        'Этот бот содержит тесты и практики для самоисследования и самопомощи. \n' +
        '1) Чтобы перейти к тестам, введите "/tests"\n' +
        '2) Чтобы перейти к практикам, введите "/practices"',
        reply_markup=keyboard
    )


@bot.callback_query_handler(func=lambda call: True)
def test_callback(call):
    bot.send_message(call.message.chat.id, 'WIN!')
    print(call.message)
#    print(call)
#    print(call.data)
#    logger.info(call)


# обработка кнопок выбора
# @bot.message_handler(content_types=['text'])
# def send_text(message):
#    if message.text.lower() == 'тесты':
#        bot.send_message(message.chat.id, 'Выполним тесты')
#    elif message.text.lower() == 'практики':
#        bot.send_sticker(message.chat.id, 'CAADAgADZgkAAnlc4gmfCor5YbYYRAI')

# стикеры
@bot.message_handler(content_types=['sticker'])
def sticker_id(message):
    print(message)

bot.polling(none_stop=True, interval=0)






# Подключаем модуль случайных чисел
import random

# Подключаем модуль для Телеграма

import telebot

# Указываем токен

bot = telebot.TeleBot('1233673851:AAGsrdlN5LjaRnL_Eea5Pc3bEdCyBZfddbg')

# Импортируем типы из модуля, чтобы создавать кнопки

from telebot import types

# Заготовки для трёх предложений

first = ["Сегодня — идеальный день для новых начинаний.",
         "Оптимальный день для того, чтобы решиться на смелый поступок!",
         "Будьте осторожны, сегодня звёзды могут повлиять на ваше финансовое состояние.",
         "Лучшее время для того, чтобы начать новые отношения или разобраться со старыми.",
         "Плодотворный день для того, чтобы разобраться с накопившимися делами."]

second = ["Но помните, что даже в этом случае нужно не забывать про", "Если поедете за город, заранее подумайте про",
          "Те, кто сегодня нацелен выполнить множество дел, должны помнить про",
          "Если у вас упадок сил, обратите внимание на",
          "Помните, что мысли материальны, а значит вам в течение дня нужно постоянно думать про"]

second_add = ["отношения с друзьями и близкими.",
              "работу и деловые вопросы, которые могут так некстати помешать планам.",
              "себя и своё здоровье, иначе к вечеру возможен полный раздрай.",
              "бытовые вопросы — особенно те, которые вы не доделали вчера.",
              "отдых, чтобы не превратить себя в загнанную лошадь в конце месяца."]

third = ["Злые языки могут говорить вам обратное, но сегодня их слушать не нужно.",
         "Знайте, что успех благоволит только настойчивым, поэтому посвятите этот день воспитанию духа.",
         "Даже если вы не сможете уменьшить влияние ретроградного Меркурия, то хотя бы доведите дела до конца.",
         "Не нужно бояться одиноких встреч — сегодня то самое время, когда они значат многое.",
         "Если встретите незнакомца на пути — проявите участие, и тогда эта встреча посулит вам приятные хлопоты."]


# Метод, который получает сообщения и обрабатывает их

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    # Если написали «Привет»

    if message.text == "/start":

        # Меню первого уровня
        keyboard1 = types.InlineKeyboardMarkup()
        key1 = types.InlineKeyboardButton(text='Тесты', callback_data='starttests')
        keyboard1.add(key1)
        key2 = types.InlineKeyboardButton(text='Практики', callback_data='startpract')
        keyboard1.add(key2)
        print(message)


        # Пишем приветствие

        bot.send_message(message.from_user.id, "Привет, сейчас я расскажу тебе гороскоп на сегодня.")

        # Готовим кнопки

        keyboard = types.InlineKeyboardMarkup()

        # По очереди готовим текст и обработчик для каждого знака зодиака

        key_oven = types.InlineKeyboardButton(text='Овен', callback_data='zodiac')

        # И добавляем кнопку на экран

        keyboard.add(key_oven)

        key_telec = types.InlineKeyboardButton(text='Телец', callback_data='zodiac')

        keyboard.add(key_telec)

        key_bliznecy = types.InlineKeyboardButton(text='Близнецы', callback_data='zodiac')

        keyboard.add(key_bliznecy)

        key_rak = types.InlineKeyboardButton(text='Рак', callback_data='zodiac')

        keyboard.add(key_rak)

        key_lev = types.InlineKeyboardButton(text='Лев', callback_data='zodiac')

        keyboard.add(key_lev)

        key_deva = types.InlineKeyboardButton(text='Дева', callback_data='zodiac')

        keyboard.add(key_deva)

        key_vesy = types.InlineKeyboardButton(text='Весы', callback_data='zodiac')

        keyboard.add(key_vesy)

        key_scorpion = types.InlineKeyboardButton(text='Скорпион', callback_data='zodiac')

        keyboard.add(key_scorpion)

        key_strelec = types.InlineKeyboardButton(text='Стрелец', callback_data='zodiac')

        keyboard.add(key_strelec)

        key_kozerog = types.InlineKeyboardButton(text='Козерог', callback_data='zodiac')

        keyboard.add(key_kozerog)

        key_vodoley = types.InlineKeyboardButton(text='Водолей', callback_data='zodiac')

        keyboard.add(key_vodoley)

        key_ryby = types.InlineKeyboardButton(text='Рыбы', callback_data='zodiac')

        keyboard.add(key_ryby)

        # Показываем все кнопки сразу и пишем сообщение о выборе

        bot.send_message(message.from_user.id, text='Выбери свой знак зодиака', reply_markup=keyboard1)

    elif message.text == "/help":

        bot.send_message(message.from_user.id, "Напиши Привет")

    else:

        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")


# Обработчик нажатий на кнопки

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    # Если нажали на одну из 12 кнопок — выводим гороскоп
    print(call.message)

    if call.data == "zodiac":
        # Формируем гороскоп

        msg = random.choice(first) + ' ' + random.choice(second) + ' ' + random.choice(
            second_add) + ' ' + random.choice(third)

        # Отправляем текст в Телеграм

        bot.send_message(call.message.chat.id, msg)

    if call.data == "starttests":
      bot.send_message(call.message.chat.id, 'Ну наконец-то!')

    if call.data == "startpract":
      bot.send_message(call.message.chat.id, 'Спать!')

# Запускаем постоянный опрос бота в Телеграме

bot.polling(none_stop=True, interval=0)

