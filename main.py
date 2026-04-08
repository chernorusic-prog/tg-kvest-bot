import telebot
from telebot import types

import Invasion
import Liberator
import Mystical_Hotel

Kvestbot = telebot.TeleBot('8355491412:AAEOfsPuvGZxZpSTFP6Gy1AhUBJJvn_gK1Q')

Start_Menu = '''Добро пожаловать в сборник моих новелл.

📌 Здесь ты будешь проходить интерактивные истории, принимая решения на каждом шаге.

С какой новеллы желаешь начать?)'''

Stop_Menu = '''🛑 История остановлена.

Какую новеллу желаешь проходить теперь?)'''

End_Novella = '''🏁 История подошла к концу.

Но это ещё не всё — другие новеллы ждут тебя.

Какую новеллу желаешь проходить теперь?)'''

Check1 = "Ты ступаешь на запретную территорию. Уверен, что твоя мать шлюха не сдохнет от спида после такого?"

Check2 = ('''Ну как скажешь, петушара ебаный, ты сам нахуй напросился.

Добро пожаловать в сборник моих самых ебанутых новелл.

📌 Здесь ты будешь проходить самые ахуенные интерактивные истории, отсасывая хуй и принимая в жопу на каждом шаге.

С какой хуйни желаешь начать?)''')

btn1 = types.InlineKeyboardButton('1', callback_data = '1')
btn2 = types.InlineKeyboardButton('2', callback_data = '2')
btn3 = types.InlineKeyboardButton('3', callback_data = '3')
btn_cocal1 = types.InlineKeyboardButton('Отсосать', callback_data = 'cocal')
btn_cocal2 = types.InlineKeyboardButton('Подрочить', callback_data = 'cocal')
btn_Mystical_Hotel = types.InlineKeyboardButton('Мистический отель', callback_data = 'Mystical_Hotel')
btn_Invasion = types.InlineKeyboardButton('Вторжение', callback_data = 'Invasion')
btn_Liberator = types.InlineKeyboardButton('Асвабадитель', callback_data = 'Liberator')

Admin_id = 882977571
users_option_novella = {}
users_step = {}
users_check = {}

keyboard = types.InlineKeyboardMarkup()

def options(chat_data, option): # Выбор варианта
    if chat_data == '1':
        option = 0
    elif chat_data == '2':
        option = 1
    elif chat_data == '3':
        option = 2
    return option

def option_novellas(chat_data, option_novella): # Выбранная новелла
    if chat_data == 'Mystical_Hotel':
        option_novella = 0
    elif chat_data == 'Invasion':
        option_novella = 1
    elif chat_data == 'Liberator':
        option_novella = 25
    return option_novella

def buttons(buttons, keyboard, btn1, btn2, btn3): # Ввод клавы
    if buttons == 1:
        keyboard.keyboard.clear()
        keyboard.add(btn1)
    elif buttons == 2:
        keyboard.keyboard.clear()
        keyboard.add(btn1, btn2)
    elif buttons == 3:
        keyboard.keyboard.clear()
        keyboard.add(btn1, btn2, btn3)
    elif buttons == 0:
        keyboard.keyboard.clear()

@Kvestbot.message_handler(commands = ["start"])
def start(chat):
    user_id = chat.from_user.id
    users_step[user_id] = "0"
    users_option_novella[user_id] = None
    keyboard.keyboard.clear()
    keyboard.add(btn_Mystical_Hotel, btn_Invasion)
    Kvestbot.send_message(chat.from_user.id, Start_Menu, reply_markup=keyboard)

@Kvestbot.message_handler(func = lambda chat: chat.text == "моя мать шлюха твоя мать спидозная сука")
def sicret1(chat):
    keyboard.keyboard.clear()
    keyboard.add(btn_cocal1, btn_cocal2)
    Kvestbot.send_message(chat.from_user.id, Check1, reply_markup=keyboard)

@Kvestbot.message_handler(func = lambda chat: chat.text == "сто жирных армянских хуев тебе в жопу")
def sicret2(chat):
    user_id = chat.from_user.id
    keyboard.keyboard.clear()
    if user_id not in users_check: # Если чел не прошел 1 этап
        users_check[user_id] = False
    users_step[user_id] = "0"
    users_option_novella[user_id] = None
    if users_check[user_id] == True: # Проверка прошел ли 1 этап
        keyboard.add(btn_Liberator)
        Kvestbot.send_message(chat.from_user.id, Check2, reply_markup=keyboard)
    else:
        keyboard.add(btn_cocal1, btn_cocal2)
        Kvestbot.send_message(chat.from_user.id, "Ты ввел какую то хуйню, иди нахуй", reply_markup=keyboard)

@Kvestbot.message_handler(commands = ["menu"])
def Menu(chat):
    user_id = chat.from_user.id
    users_step[user_id] = "0"
    users_option_novella[user_id] = None
    keyboard.keyboard.clear()
    keyboard.add(btn_Mystical_Hotel, btn_Invasion)
    Kvestbot.send_message(chat.from_user.id, Start_Menu, reply_markup=keyboard)
    Kvestbot.send_message(Admin_id, f'Пользователь {chat.from_user.first_name} {chat.from_user.last_name} ({chat.from_user.username}, {chat.from_user.language_code}) Получил сообщение: \n \n {Start_Menu}')

@Kvestbot.message_handler(commands = ["stop"])
def stop(chat):
    user_id = chat.from_user.id
    users_step[user_id] = "0"
    users_option_novella[user_id] = None
    keyboard.keyboard.clear()
    keyboard.add(btn_Mystical_Hotel, btn_Invasion)
    Kvestbot.send_message(chat.from_user.id, Stop_Menu, reply_markup=keyboard)


@Kvestbot.callback_query_handler(func=lambda call: call.data == "cocal")
def Cocal(chat):
    user_id = chat.from_user.id
    Kvestbot.edit_message_reply_markup( # Удаляем кнопки у всех предыдущих сообщений
        chat_id=chat.message.chat.id,
        message_id=chat.message.message_id,
        reply_markup=None
    )
    users_check[user_id] = True
    Kvestbot.send_message(chat.from_user.id, "АХАХАХАХАХААХ, ебать ты лошара, каким же надо быть "
                                                         "долбаебом, чтобы кликнуть на такую хуйню?))")

@Kvestbot.callback_query_handler(func=lambda call: True)
def Cocal(chat):
    user_id = chat.from_user.id # Сбор данных и обьявление переменных
    option = None
    option_novella = None
    chat_data = chat.data
    users_option_novella[user_id] = option_novellas(chat_data, users_option_novella[user_id]) # Проверка выбора новеллы
    if users_option_novella[user_id] == 0:
        option_novella = Mystical_Hotel.Mystical_Hotel
    elif users_option_novella[user_id] == 1: #Вот сюда надо добавить новую новеллу
        option_novella = Invasion.Invasion
    elif users_option_novella[user_id] == 25:
        option_novella = Liberator.Liberator
    option = options(chat_data, option) # Перевод шага на выбранный вариант
    if option != None:
        users_step[user_id] = option_novella[users_step[user_id]]["options"][option]
    Kvestbot.edit_message_reply_markup( # Добавляем клаву
        chat_id=chat.message.chat.id,
        message_id=chat.message.message_id,
        reply_markup=None
    )
    buttons_1 = option_novella[users_step[user_id]]["buttons"]
    buttons(buttons_1, keyboard, btn1, btn2, btn3)
    Kvestbot.send_message(chat.from_user.id, option_novella[users_step[user_id]]["Text"], reply_markup=keyboard) #Вывод сообщения
    if buttons_1 == 0: # Вывод сообщения о конце новеллы
        if option_novella != 25:
            users_step[user_id] = "0"
            keyboard.add(btn_Mystical_Hotel, btn_Invasion)
            Kvestbot.send_message(chat.from_user.id, End_Novella, reply_markup=keyboard)
        else:
            keyboard.add(btn_Mystical_Hotel, btn_Invasion)
            Kvestbot.send_message(chat.from_user.id, End_Novella, reply_markup=keyboard)
    print(users_step[user_id]) # Заменить на отправку сообщений мне

Kvestbot.polling(none_stop = True)