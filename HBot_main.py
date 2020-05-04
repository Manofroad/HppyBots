import telebot
from telebot import types
import datetime

# ARA_HppyBot
bot = telebot.TeleBot('1233673851:AAGsrdlN5LjaRnL_Eea5Pc3bEdCyBZfddbg')

# БД

import sqlite3
from sqlite3 import Error
# создание базы
def sql_connection():
    try:
        con = sqlite3.connect('hppy.db')
        print("Connection is established")
        print (con)
        return con
    except Error:
        print(Error)

# создание таблиц
def sql_table(con):
    cursorObj = con.cursor()
    cursorObj.execute('CREATE TABLE if not exists uinfo(id integer primary key, username text, pract_state integer)')
    cursorObj.execute('CREATE TABLE if not exists results(dt text, id integer, username text, type integer, rec text)')
    con.commit()

# вставка записи
def sql_insert(con, entities):
    cursorObj = con.cursor()
    cursorObj.execute('INSERT INTO uinfo(id, pract_state) VALUES(?, ?)', entities)
    con.commit()

# вставка записи
def sql_update(con, dataset):
    cursorObj = con.cursor()
    cursorObj.execute('SELECT * FROM uinfo '+' WHERE id = '+str(dataset[0]))
    rows = cursorObj.fetchall()
    if len(rows) == 0:
        sql_insert(con, dataset)
    else:
        cursorObj.execute('UPDATE uinfo SET pract_state = '+str(dataset[1])+' WHERE id = '+str(dataset[0]))
    con.commit()

# выполняем
con = sql_connection()
sql_table(con)

def set_pract_state(id, state):
    con = sql_connection()
    entities = (id, state)
    sql_update(con, entities)
    return

def get_pract_state(id):
    con = sql_connection()
    cursorObj = con.cursor()
    cursorObj.execute('SELECT * FROM uinfo '+' WHERE id = '+str(id))
    row = cursorObj.fetchone()
    if row:
        return row[2]

def insert_rec(dt, id, username, type, rec):
    con = sql_connection()
    cursorObj = con.cursor()
    qry = 'INSERT INTO results(dt, id, username, type, rec) VALUES("'+dt+'",'+str(id)+',"'+username+'",'+str(type)+',"'+rec+'")'
    print(qry)
    cursorObj.execute(qry)
    con.commit()

# Меню первого уровня
keyboard1 = types.InlineKeyboardMarkup()
key1 = types.InlineKeyboardButton(text='Тесты', callback_data='start_tests')
keyboard1.add(key1)
key2 = types.InlineKeyboardButton(text='Практики', callback_data='start_pract')
keyboard1.add(key2)

# Меню тестов
keyboard2 = telebot.types.InlineKeyboardMarkup(True)
keyboard2.add(types.InlineKeyboardButton(text='Шкала субъективного благополучия Динера', callback_data='start_diner'))
keyboard2.add(
    types.InlineKeyboardButton(text='Шкала оценки жизненной энергии', callback_data='start_vital'))
keyboard2.add(types.InlineKeyboardButton(text='Назад', callback_data='to_level_1'))

# Меню практик
keyboard21 = telebot.types.InlineKeyboardMarkup(True)
keyboard21.add(types.InlineKeyboardButton(text='Три хороших события дня', callback_data='start_3things'))
keyboard21.add(
    types.InlineKeyboardButton(text='Практика благодарности', callback_data='start_thanks'))
keyboard21.add(types.InlineKeyboardButton(text='Назад', callback_data='to_level_1'))

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

diner_qn = []
diner_ans = []

diner_descr = 'Шкала субъективного психологического благополучия (SWLS). '\
'Методика предложена ' \
'E. Diener, R.A. Emmons, R.J. Larsen и S. Griffin в 1985 году, адаптирована и валидизирована Д.А. ' \
'Леонтьевым и Е.Н. Осиным в 2003 году на русском языке.\n\n' + 'Тест содержит пять высказываний. Пожалуйста, ответьте ' \
'на них, используя 7-балльную шкалу:\n' \
'=======================\n' \
'1. Определенно не согласен\n' \
'2. Не согласен\n' \
'3. До определенной степени не согласен\n' \
'4. Ни то, ни другое\n' \
'5. До определенной степени согласен\n' \
'6. Согласен\n' \
'7. Определенно согласен\n' \
'======================='

# Вопросы к тесту Динера
diner_qst = [
    '1. В целом моя жизнь близка к идеалу.',
    '2. Условия моей жизни прекрасные.',
    '3.	Я удовлетворен жизнью.',
    '4.	К настоящему моменту я уже получил от жизни всё, чего хотел.',
    '5.	Если я мог прожить жизнь заново, то не изменил бы почти ничего.'
]


# ТЕСТ СУБЪЕКТИВНОЙ ВИТАЛЬНОСТИ

vital_qn = 0
vital_ans = [0,0,0,0,0,0]

vital_descr = 'Шкала субъективной оценки жизненной энергии Subjective Vitality Scale (Ryan, R. M., & Frederick, ' \
'C. M., 1997).\n\n' + 'Тест содержит 6 утверждений. Пожалуйста, оцените их в отношении того, насколько они подходят' \
' вам и вашей жизни в настоящее время, от 1 до 7, где:  ' \
'=======================\n' \
'1. Абсолютно неверно\n' \
'2. \n' \
'3. \n' \
'4. До нкоторой степени\n' \
'5. \n' \
'6. \n' \
'7. Абсолютно верно\n' \
'======================='

# Вопросы к тесту субъективной оценки жизненной энергии
vital_qst = [
    '1. Я чувствую себя бодрым и энергичным.',
    '2.	Иногда я чувствую себя настолько бодрым, что меня разрывает от этого чувства.',
    '3.	У меня есть энергия и настроение.',
    '4.	Я с нетерпением ожидаю каждый новый день.',
    '5.	Я почти всегда нахожусь в режиме готовности и в активном состоянии.',
    '6.	Я чувствую в себе много энергии.'
]

# Меню ответов теста витальности (1-7)
keyboard31 = telebot.types.InlineKeyboardMarkup(True)
keyboard31.add(types.InlineKeyboardButton(text='1', callback_data='vit1'))
keyboard31.add(types.InlineKeyboardButton(text='2', callback_data='vit2'))
keyboard31.add(types.InlineKeyboardButton(text='3', callback_data='vit3'))
keyboard31.add(types.InlineKeyboardButton(text='4', callback_data='vit4'))
keyboard31.add(types.InlineKeyboardButton(text='5', callback_data='vit5'))
keyboard31.add(types.InlineKeyboardButton(text='6', callback_data='vit6'))
keyboard31.add(types.InlineKeyboardButton(text='7', callback_data='vit7'))

#Меня возврата из тестов
keyboard3end = telebot.types.InlineKeyboardMarkup(True)
keyboard3end.add(types.InlineKeyboardButton(text='Назад к тестам', callback_data='start_tests'))
keyboard3end.add(types.InlineKeyboardButton(text='В главное меню', callback_data='to_level_1'))

keyboard4end = telebot.types.InlineKeyboardMarkup(True)
keyboard4end.add(types.InlineKeyboardButton(text='Назад к практикам', callback_data='start_pract'))
keyboard4end.add(types.InlineKeyboardButton(text='В главное меню', callback_data='to_level_1'))

# ПРАКТИКИ

# ПРАКТИКА ТРИ ХОРОШИХ СОБЫТИЯ
good3_descr = 'Практика "Три хороших события" (Three good things in life), Seligman, M. E. P. Steen, T. A., Park, N.,'
'& Peterson, C. (2005). Positive psychology progress: Empiricalvalidation of interventions. American Psychologist. '
'Рекомендуется уделять этой практике не менее 10 минут в день. Эффект от практики начинает быть заметен через '
'неделю регулярных занятий.\n\n'

# ПРАКТИКА БЛАГОДАРНОСТИ
thanks_descr = 'Практика багодарности.'
'Рекомендуется выполнять эту практику еженедельно\n\n'


# Обработчик текстовых команд
@bot.message_handler(commands=['start', 'tests', 'practices'])
def start_message(message):
    if message.text == '/start':
        bot.send_message(message.chat.id, 'Этот бот содержит психологические тесты, и '
                                               'психологические практики для самоисследовния и самоподдержки.')
        bot.send_message(message.chat.id, 'Выберите раздел:', reply_markup=keyboard1)
        set_pract_state(message.chat.id, -1)
        print(message)
    elif message.text == '/tests':
        bot.send_message(message.chat.id, 'Вы перешли в раздел с тестами')
        bot.send_message(message.chat.id, 'Выберите тест:', reply_markup=keyboard2)
    elif message.text == '/practices':
        bot.send_message(message.chat.id, 'Вы перешли в раздел с практиками')
        bot.send_message(message.chat.id, 'Выберите практику:', reply_markup=keyboard21)
        set_pract_state(message.chat.id, -1)
    else:
        print(message)


# Обработчики нажатий на кнопки
@bot.callback_query_handler(func=lambda call: True)
def callback_work(call):

    #global diner_qn
    #global diner_ans
    #global diner_qst

    global vital_qn
    global vital_ans
    global vital_descr

    # LEVEL1

    if call.data == 'start_tests':
        bot.send_message(call.message.chat.id, 'Вы перешли в раздел с тестами')
        bot.send_message(call.message.chat.id, 'Выберите тест:', reply_markup=keyboard2)

    if call.data == 'start_pract':
        bot.send_message(call.message.chat.id, 'Вы перешли в раздел с практиками')
        bot.send_message(call.message.chat.id, 'Выберите практику:', reply_markup=keyboard21)
        set_pract_state(call.message.chat.id, -1)

    # LEVEL2.TESTS

    if call.data == 'start_diner':
        diner_qn = 0
        diner_ans = [0,0,0,0,0]
        msg = diner_descr
        bot.send_message(call.message.chat.id, msg)
        bot.send_message(call.message.chat.id, diner_qst[diner_qn], reply_markup=keyboard3)

    if call.data == 'start_vital':
        vital_qn = 0
        vital_ans = [0,0,0,0,0,0]
        msg = vital_descr
        bot.send_message(call.message.chat.id, msg)
        bot.send_message(call.message.chat.id, vital_qst[vital_qn], reply_markup=keyboard31)

    if call.data == 'to_level_1':
        bot.send_message(call.message.chat.id, 'Выберите раздел:', reply_markup=keyboard1)

    # LEVEL2.PACTICES

    if call.data == 'start_3things':
        bot.send_message(call.message.chat.id, good3_descr)
        set_pract_state(call.message.chat.id, 0)
    if call.data == 'start_thanks':
        msg = 'Практика благодарности'
        bot.send_message(call.message.chat.id, msg)
        set_pract_state(call.message.chat.id, 1)

    # LEVEL3.DINER

    if call.data in ['sel1', 'sel2', 'sel3', 'sel4', 'sel5', 'sel6', 'sel7']:
        print(call.data)
        print(diner_qn)
        if diner_qn < 5:
            cdata = call.data
            diner_ans[diner_qn] = int(cdata[3])
            diner_qn += 1
        if diner_qn < 5:
            bot.send_message(call.message.chat.id, diner_qst[diner_qn], reply_markup=keyboard3)
        else:
            ds = sum(diner_ans)
            bot.send_message(call.message.chat.id, "Ваш результат = " + str(ds) + "\nСредний результат ("
                                                                                         "российская выборка) = 21.9",
                             reply_markup=keyboard3end)

    # LEVEL3.VITAL

    if call.data in ['vit1', 'vit2', 'vit3', 'vit4', 'vit5', 'vit6', 'vit7']:
        print(call.data)
        print(vital_qn)
        if vital_qn < 6:
            cdata = call.data
            vital_ans[vital_qn] = int(cdata[3])
            vital_qn += 1
        if vital_qn < 6:
            bot.send_message(call.message.chat.id, vital_qst[vital_qn], reply_markup=keyboard31)
        else:
            vs = sum(vital_ans)
            bot.send_message(call.message.chat.id, "Ваш результат = " + str(vs) + "\nДанные для сравнения: "
                                                                                         "средний результат = 23.53 ("
                                                                                         "португальская выборка, "
                                                                                         "309 пожилых людей)",
                             reply_markup=keyboard3end)



# Обработчиккоманды  /help
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
        'Доступные команы: \n' +
        '1) Чтобы перейти к тестам, введите "/tests"\n' +
        '2) Чтобы перейти к практикам, введите "/practices"',
        reply_markup=keyboard
    )


# @bot.callback_query_handler(func=lambda call: True)
# def test_callback(call):
#    bot.send_message(call.message.chat.id, 'WIN!')
#    print(call.message)
#    print(call)
#    print(call.data)
#    logger.info(call)


# Обработчик текста
@bot.message_handler(content_types=['text'])
def process_text(message):

    # Пришёл текст практики "Три хороших события"
    if get_pract_state(message.chat.id) == 0:
        bot.send_message(message.chat.id, 'Ваши ответы. Сохраните их для истории:')
        dt = datetime.datetime.today().strftime("%d.%m.%Y %H:%M")
        bot.send_message(message.chat.id,
            'Практика "Три хороших события" ('+ dt + ')\n' + message.text,
             reply_markup=keyboard4end)
        set_pract_state(message.chat.id, -1)
        insert_rec(str(dt), message.chat.id, message.chat.username, 0, message.text)

    # Пришёл текст практики благодарности
    if get_pract_state(message.chat.id) == 1:
        bot.send_message(message.chat.id, 'Ваши ответы. Сохраните их для истории.')
        dt = datetime.datetime.today().strftime("%d.%m.%Y %H:%M")
        msg = 'Практика благодарности ('+ dt + '):\n' + message.text
        bot.send_message(message.chat.id, msg, reply_markup=keyboard4end)
        set_pract_state(message.chat.id, -1)
        insert_rec(str(dt), message.chat.id, message.chat.username, 1, message.text)

bot.polling(none_stop=True, interval=0)
