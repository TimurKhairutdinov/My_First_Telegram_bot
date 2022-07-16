
import telebot
from telebot import types
import content
import s_content

token = s_content.token_id
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    content.start(message)


@bot.message_handler(content_types=['text'])
def bot_message(message):

    if message.chat.type == 'private':
        if message.text == 'Знакомство с Python':
            content.start_python(message)

        elif message.text == '1. Введение в Python':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item_back = types.KeyboardButton('Назад')
            markup.add(item_back)

            content.python_one(message)

            if message.text == 'Назад':
                content.python_two(message)

        elif message.text == '2. Данные, функции':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item_back = types.KeyboardButton('Назад')
            markup.add(item_back)

            content.python_two(message)

        elif message.text == ('Гибкие методологии'):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item_back = types.KeyboardButton('Назад')
            markup.add(item_back)

            content.menu_agile(message)

        elif message.text == 'Введение':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item_back = types.KeyboardButton('Назад')
            markup.add(item_back)

            content.start_agile(message)

        elif message.text == 'Agile':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item_back = types.KeyboardButton('Назад')
            markup.add(item_back)
            content.agile(message)

        elif message.text == ('Scrum'):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item_back = types.KeyboardButton('Назад')
            markup.add(item_back)
            content.scrum(message)

        elif message.text == ('Lean'):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item_back = types.KeyboardButton('Назад')
            markup.add(item_back)
            markup.add(item_back)
            content.lean(message)
        
        elif message.text == 'Назад':
            content.back(message)


bot.polling(non_stop=True)
