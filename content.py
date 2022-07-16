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


def start_python(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('1. Введение в Python')
    item2 = types.KeyboardButton('2. Данные, функции')
    item_back = types.KeyboardButton('Назад')
    markup.add(item1, item2, item_back)
    bot.send_message(message.chat.id, 'Знакомство с Python',
                     reply_markup=markup)


def back(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Знакомство с Python')
    item2 = types.KeyboardButton('Гибкие методологии')
    markup.add(item1, item2)
    bot.send_message(message.chat.id, 'Назад', reply_markup=markup)


def python_one(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bot.send_message(
        message.chat.id, f'Лекция: {s_content.pyth_lec_one}',
        reply_markup=markup)

    bot.send_message(
        message.chat.id, f'Семинар 1: {s_content.pyth_sem_one}',
        reply_markup=markup)

    bot.send_message(message.chat.id, f'Семинар 2: {s_content.pyth_sem_two}',
                     reply_markup=markup)

    bot.send_message(
        message.chat.id, f'Лекционный материал: {s_content.pyth_pdf_one}',
        reply_markup=markup)


def python_two(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bot.send_message(
        message.chat.id, f'Лекция: {s_content.pyth_lec_two}',
        reply_markup=markup)

    bot.send_message(
        message.chat.id, f'Семинар 1: {s_content.pyth_sem_three}',
        reply_markup=markup)

    bot.send_message(
        message.chat.id, f'Семинар 2: {s_content.empty_content}',
        reply_markup=markup)

    bot.send_message(
        message.chat.id, f'Лекционный материал: {s_content.pyth_pdf_two}',
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


def start_agile(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bot.send_message(
        message.chat.id, f'Лекция: {s_content.agl_lec_one}',
        reply_markup=markup)

    bot.send_message(
        message.chat.id, f'Семинар: {s_content.agl_sem_one}',
        reply_markup=markup)

    bot.send_message(
        message.chat.id, f'Лекционный материал: {s_content.agl_pdf_one}',
        reply_markup=markup)


def agile(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bot.send_message(
        message.chat.id, f'Лекция: {s_content.agl_lec_two}',
        reply_markup=markup)

    bot.send_message(
        message.chat.id, f'Семинар: {s_content.agl_sem_two}',
        reply_markup=markup)

    bot.send_message(
        message.chat.id, f'Лекционный материал: {s_content.agl_sem_two}',
        reply_markup=markup)


def scrum(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bot.send_message(
        message.chat.id, f'Лекция: {s_content.agl_lec_scrm}',
        reply_markup=markup)

    bot.send_message(
        message.chat.id, f'Семинар: {s_content.agl_sem_scrm}',
        reply_markup=markup)

    bot.send_message(
        message.chat.id, f'Лекционный материал: {s_content.agl_pdf_scrm}',
        reply_markup=markup)


def lean(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bot.send_message(
        message.chat.id, f'Лекция: {s_content.agl_lec_lean}',
        reply_markup=markup)

    bot.send_message(
        message.chat.id, f'{s_content.empty_content}',
        reply_markup=markup)

    bot.send_message(
        message.chat.id, f'Лекционный материал: {s_content.agl_pdf_lean}',
        reply_markup=markup)
