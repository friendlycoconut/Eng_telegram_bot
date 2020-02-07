import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

import kb

API_TOKEN = ''

# Configure logging
logging.basicConfig(level=logging.INFO)
# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)





@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    print(message.from_user.first_name)
    await message.answer("Привет, " + message.from_user.first_name + "! " + u'\U0001f604'+ " \nВыберите один из вариантов: ", reply_markup=kb.keyboard_markup)

@dp.callback_query_handler(text='test')  # if cb.data == 'no'
@dp.callback_query_handler(text='words')  # if cb.data == 'yes'
async def inline_kb_answer_callback_handler(query: types.CallbackQuery):
    answer_data = query.data

    # always answer callback queries, even if you have nothing to say
    await query.answer(f'You answered with {answer_data!r}')
    kbm = types.InlineKeyboardMarkup()
    if answer_data == 'test':
        kbm = kb.keyboard_markup_2
    elif answer_data == 'words':
        kbm = kb.keyboard_markup_words
    else:
        text = f'Unexpected callback data {answer_data!r}!'

    await query.message.answer("Выберите уровень: \n" , reply_markup=kbm)

@dp.callback_query_handler(text='a2')  # if cb.data == 'no'
@dp.callback_query_handler(text='b1')  # if cb.data == 'yes'
async def inline_kb_answer_callback_handler(query: types.CallbackQuery):
    answer_data = query.data
    # always answer callback queries, even if you have nothing to say
    await query.answer(f'You answered with {answer_data!r}')
    kbm = types.InlineKeyboardMarkup()
    if answer_data == 'test':
        kbm = kb.keyboard_markup_2
    elif answer_data == 'words':
        text = 'Oh no...Why so?'
    else:
        text = f'Unexpected callback data {answer_data!r}!'

    await bot.send_poll(query.from_user.id,'what?', ['yes','no','prob'], True, type ='quiz', correct_option_id=0)



@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.answer("Напиши мне , и я помогу выучить английский!")

@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)


if __name__ == '__main__':
    executor.start_polling(dp)
