
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
            content.menu_python(message)

        elif message.text == '1. Введение в Python':
            content.get_content(message, s_content.pyth_lec_one,
                                s_content.pyth_sem_one, s_content.pyth_sem_two, pdf=s_content.pyth_pdf_one)

        elif message.text == '2. Данные, функции':
            content.get_content(message, s_content.pyth_lec_two,
                                s_content.pyth_sem_three, pdf=s_content.pyth_pdf_two)

        elif message.text == ('Гибкие методологии'):
            content.menu_agile(message)

        elif message.text == 'Введение':
            content.get_content(message, s_content.agl_lec_one,
                                s_content.agl_sem_one, pdf=s_content.agl_pdf_one)

        elif message.text == 'Agile':
            content.get_content(message, s_content.agl_lec_two,
                                s_content.agl_sem_two, pdf=s_content.agl_pdf_two)

        elif message.text == ('Scrum'):
            content.get_content(message, s_content.agl_lec_scrm,
                                s_content.agl_sem_scrm, pdf=s_content.agl_pdf_scrm)

        elif message.text == ('Lean'):
            content.get_content(
                message, s_content.agl_lec_lean, pdf=s_content.agl_pdf_lean)

        elif message.text == 'Назад':
            content.back(message)


bot.polling(non_stop=True)
