import telebot
from telebot import types

import Invasion
import Mystical_Hotel

Kvestbot = telebot.TeleBot('8752020452:AAFefZcxitQDYn9fqaOq0_86h4uKZd4o-QA')

Start_Menu = '''Добро пожаловать в сборник моих новелл.

📌 Здесь ты будешь проходить интерактивные истории, принимая решения на каждом шаге.

С какой новеллы желаешь начать?)'''

Stop_Menu = '''🛑 История остановлена.

Какую новеллу желаешь проходить теперь?)'''

End_Novella = '''🏁 История подошла к концу.

Но это ещё не всё — другие новеллы ждут тебя.

Какую новеллу желаешь проходить теперь?)'''

btn1 = types.InlineKeyboardButton('1', callback_data = '1')
btn2 = types.InlineKeyboardButton('2', callback_data = '2')
btn3 = types.InlineKeyboardButton('3', callback_data = '3')
btn_Mystical_Hotel = types.InlineKeyboardButton('Мистический отель', callback_data = 'Mystical_Hotel')
btn_Invasion = types.InlineKeyboardButton('Вторжение', callback_data = 'Invasion')

users_option_novella = {}
users_step = {}

keyboard = types.InlineKeyboardMarkup()

def options(chat_data, option):
    if chat_data == '1':
        option = 0
    elif chat_data == '2':
        option = 1
    elif chat_data == '3':
        option = 2
    return option

def option_novellas(chat_data, option_novella):
    if chat_data == 'Mystical_Hotel':
        option_novella = 0
    elif chat_data == 'Invasion':
        option_novella = 1
    return option_novella

def buttons(buttons, keyboard, btn1, btn2, btn3):
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

@Kvestbot.message_handler(commands = ["menu"])
def Menu(chat):
    user_id = chat.from_user.id
    users_step[user_id] = "0"
    users_option_novella[user_id] = None
    keyboard.keyboard.clear()
    keyboard.add(btn_Mystical_Hotel, btn_Invasion)
    Kvestbot.send_message(chat.from_user.id, Start_Menu, reply_markup=keyboard)

@Kvestbot.message_handler(commands = ["stop"])
def stop(chat):
    user_id = chat.from_user.id
    users_step[user_id] = "0"
    users_option_novella[user_id] = None
    keyboard.keyboard.clear()
    keyboard.add(btn_Mystical_Hotel, btn_Invasion)
    Kvestbot.send_message(chat.from_user.id, Stop_Menu, reply_markup=keyboard)


@Kvestbot.callback_query_handler(func=lambda call: True)
def Cocal(chat):
    user_id = chat.from_user.id
    option = None
    option_novella = None
    chat_data = chat.data
    users_option_novella[user_id] = option_novellas(chat_data, users_option_novella[user_id])
    if users_option_novella[user_id] == 0:
        option_novella = Mystical_Hotel.Mystical_Hotel
    elif users_option_novella[user_id] == 1:
        option_novella = Invasion.Invasion
    option = options(chat_data, option)
    if option != None:
        users_step[user_id] = option_novella[users_step[user_id]]["options"][option]
    Kvestbot.edit_message_reply_markup(
        chat_id=chat.message.chat.id,
        message_id=chat.message.message_id,
        reply_markup=None
    )
    buttons_1 = option_novella[users_step[user_id]]["buttons"]
    buttons(buttons_1, keyboard, btn1, btn2, btn3)
    Kvestbot.send_message(chat.from_user.id, option_novella[users_step[user_id]]["Text"], reply_markup=keyboard)
    if buttons_1 == 0:
        users_step[user_id] = "0"
        keyboard.add(btn_Mystical_Hotel, btn_Invasion)
        Kvestbot.send_message(chat.from_user.id, End_Novella, reply_markup=keyboard)
    print(users_step[user_id])


Kvestbot.polling(none_stop = True)

# @Kvestbot.message_handler(commands = ["start"])
# def start(chat):
#     user_id = chat.chat.id
#     users[user_id] = 0
#     keyboard.add(btn1, btn2, btn3)
#     Kvestbot.send_message(chat.chat.id, f'{user_id}dfs{users}', reply_markup=keyboard)
#
# @Kvestbot.callback_query_handler(func=lambda call: True)
# def Cocal(chat):
#     user_id = chat.from_user.id
#     var = None
#     if chat.data == '1':
#         var = 0
#     if chat.data == '2':
#         var = 1
#     if chat.data == '3':
#         var = 2
#     Kvestbot.edit_message_reply_markup(
#         chat_id=chat.message.chat.id,
#         message_id=chat.message.message_id,
#         reply_markup=None
#     )
#     if Invasion.Invasion[users[user_id]][-1] == 2:
#         keyboard.keyboard.clear()
#         keyboard.add(btn1, btn2)
#     elif Invasion.Invasion[users[user_id]][-1] == 3:
#         keyboard.keyboard.clear()
#         keyboard.add(btn1, btn2, btn3)
#     Kvestbot.send_message(chat.from_user.id, Invasion.Invasion[users[user_id]][var], reply_markup=keyboard)
#     users[user_id] += 1
