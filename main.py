import telebot
from telebot import types

import Invasion
import Liberator
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

Check1 = "Ты ступаешь на запретную территорию. Уверен, что твоя мать шлюха не сдохнет от спида после такого?"

Check2 = '''Ну как скажешь, петушара ебаный, ты сам нахуй напросился.

Добро пожаловать в сборник моих самых ебанутых новелл.

📌 Здесь ты будешь проходить самые ахуенные интерактивные истории, отсасывая хуй и принимая в жопу на каждом шаге.

С какой хуйни желаешь начать?)'''

End_Check = '''🏁 Ебанутая хуйня подошла к концу.

Но этот пиздец ещё не кончился — другие ебанутые новеллы готовы порвать тебе анал в любой момент.

Какую хуйню желаешь проходить теперь?)'''

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
bot_last_message = {}

keyboard = types.InlineKeyboardMarkup()

def buttons_novellas(adequacy): # Кнопки с новеллами
    if adequacy:
        keyboard.add(btn_Mystical_Hotel, btn_Invasion)
    elif not adequacy:
        keyboard.add(btn_Liberator)

def option_novellas(chat_data, user_id): # Выбранная новелла
    if chat_data == 'Mystical_Hotel':
        users_step[user_id] = "0"
        users_option_novella[user_id] = Mystical_Hotel.Mystical_Hotel
    elif chat_data == 'Invasion':
        users_step[user_id] = "0"
        users_option_novella[user_id] = Invasion.Invasion
    elif chat_data == 'Liberator':
        users_step[user_id] = "0"
        users_option_novella[user_id] = Liberator.Liberator

def options(chat_data, option): # Выбор варианта шага
    if chat_data == '1':
        option = 0
    elif chat_data == '2':
        option = 1
    elif chat_data == '3':
        option = 2
    return option

def buttons(buttons, keyboard, btn1, btn2, btn3): # Ввод кнопок с вариантами шагов
    if buttons == 1:
        keyboard.add(btn1)
    elif buttons == 2:
        keyboard.add(btn1, btn2)
    elif buttons == 3:
        keyboard.add(btn1, btn2, btn3)

def sending_message(chat, chat_id, Text, keyboard = None): # Отправка сообщения
    user_id = chat.from_user.id
    if user_id in bot_last_message: # Удаляем кнопки у предыдущего сообщения
        try:
            Kvestbot.edit_message_reply_markup(
                chat_id=chat_id,
                message_id=bot_last_message[user_id],
                reply_markup=None
            )
        except:
            pass
    if keyboard != None: # вывод сообщения пользователю(в зависимости от надобности клавы)
        message = Kvestbot.send_message(chat.from_user.id, Text, reply_markup = keyboard)
        keyboard.keyboard.clear()
    else:
        message = Kvestbot.send_message(chat.from_user.id, Text)
    if user_id != Admin_id: # Дублирование сообщений админу
        Kvestbot.send_message(Admin_id, f'Пользователь {chat.from_user.first_name} {chat.from_user.last_name} '
                            f'({chat.from_user.username}, {chat.from_user.language_code}) Получил сообщение: \n '
                            f'\n {Text}')
    bot_last_message[user_id] = message.message_id # Сохранение id сообщений бота, чтобы удалять кнопки

@Kvestbot.message_handler(commands = ["start", "menu", "stop"]) # Обработка команд
def commands(chat):
    adequacy = True
    buttons_novellas(adequacy)
    if chat.text in ["/start", "/menu"]:
        sending_message(chat, chat.chat.id, Start_Menu, keyboard)
    elif chat.text == '/stop':
        sending_message(chat, chat.chat.id, Stop_Menu, keyboard)

@Kvestbot.message_handler(func = lambda chat: chat.text == "моя мать шлюха твоя мать спидозная сука") # Проверка 1
def secret1(chat):
    keyboard.add(btn_cocal1, btn_cocal2)
    sending_message(chat, chat.chat.id, Check1, keyboard)

@Kvestbot.message_handler(func = lambda chat: chat.text == "сто жирных армянских хуев тебе в жопу") # Проверка 2
def secret2(chat):
    user_id = chat.from_user.id
    if user_id not in users_check: # Если чел не прошел 1 этап
        users_check[user_id] = False
    if users_check[user_id] == True: # Проверка прошел ли 1 этап
        adequacy = False
        buttons_novellas(adequacy)
        sending_message(chat, chat.chat.id, Check2, keyboard)
    else:
        sending_message(chat, chat.chat.id, "Ты ввел какую то хуйню, иди нахуй")

@Kvestbot.callback_query_handler(func=lambda call: call.data == "cocal") # Выдача доступа и смешнявка
def cocal(chat):
    user_id = chat.from_user.id
    users_check[user_id] = True
    sending_message(chat, chat.message.chat.id, "АХАХАХАХАХААХ, ебать ты лошара, каким же надо быть "
                                                         "долбаебом, чтобы кликнуть на такую хуйню?))")

@Kvestbot.callback_query_handler(func=lambda call: True) # Прохождение новелл
def passage_novellas(chat):
    user_id = chat.from_user.id # Сбор данных и обьявление переменных
    option = None
    chat_data = chat.data
    option_novellas(chat_data, user_id) # Проверка выбора новеллы
    option_novella = users_option_novella[user_id]
    option = options(chat_data, option) # Перевод шага на выбранный вариант
    if option != None:
        users_step[user_id] = option_novella[users_step[user_id]]["options"][option]
    buttons_1 = option_novella[users_step[user_id]]["buttons"] #Добавляем кнопки
    buttons(buttons_1, keyboard, btn1, btn2, btn3)
    sending_message(chat, chat.message.chat.id, option_novella[users_step[user_id]]["Text"], keyboard) #отправляем сообщение
    if buttons_1 == 0: # Вывод сообщения о конце новеллы(разделение по адекватности)
        if users_option_novella[user_id] != Liberator.Liberator: # Сюда добавлять ебанутые новеллы!!!!
            adequacy = True
            buttons_novellas(adequacy)
            sending_message(chat, chat.message.chat.id, End_Novella, keyboard)
        else:
            adequacy = False
            buttons_novellas(adequacy)
            sending_message(chat, chat.message.chat.id, End_Check, keyboard)

Kvestbot.polling(none_stop = True)