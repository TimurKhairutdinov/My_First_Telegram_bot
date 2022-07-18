import telebot
from telebot import types
import s_content

token = s_content.token_id
bot = telebot.TeleBot(token)


def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Знакомство с Python')
    item2 = types.KeyboardButton('Гибкие методологии')
    markup.add(item1, item2)
    bot.send_message(
        message.chat.id, f'Привет, {message.from_user.first_name}!', reply_markup=markup)


def back(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Знакомство с Python')
    item2 = types.KeyboardButton('Гибкие методологии')
    markup.add(item1, item2)
    bot.send_message(message.chat.id, 'Назад', reply_markup=markup)


def menu_python(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('1. Введение в Python')
    item2 = types.KeyboardButton('2. Данные, функции')
    item_back = types.KeyboardButton('Назад')
    markup.add(item1, item2, item_back)
    bot.send_message(message.chat.id, 'Знакомство с Python',
                     reply_markup=markup)


def menu_agile(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Введение')
    item2 = types.KeyboardButton('Agile')
    item3 = types.KeyboardButton('Scrum')
    item4 = types.KeyboardButton('Lean')
    item_back = types.KeyboardButton('Назад')
    markup.add(item1, item2, item3, item4,  item_back)
    bot.send_message(message.chat.id, 'Гибкие методологии',
                     reply_markup=markup)


def get_content(message, lec, sem1 = 'Отсутствует', sem2 = 'Отсутствует', pdf = 'Отсутствует'):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item_back = types.KeyboardButton('Назад')
    markup.add(item_back)
    bot.send_message(
        message.chat.id, f'Лекция: {lec}',
        reply_markup=markup)

    bot.send_message(
        message.chat.id, f'Семинар 1: {sem1}',
        reply_markup=markup)

    bot.send_message(message.chat.id, f'Семинар 2: {sem2}',
                     reply_markup=markup)

    bot.send_message(
        message.chat.id, f'Лекционный материал: {pdf}',
        reply_markup=markup)
