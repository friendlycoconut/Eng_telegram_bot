import logging
import os
from aiogram import Bot, Dispatcher, executor, types

import audios
import kb

API_TOKEN = os.getenv("API_TOKEN")

# Configure logging
logging.basicConfig(level=logging.INFO)
# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    print(message.from_user.first_name)
    await message.answer(
        "Привет, " + message.from_user.first_name + "! " + u'\U0001f604' + " \nВыберите один из вариантов: ",
        reply_markup=kb.keyboard_markup)


@dp.callback_query_handler(text=kb.variant_1_text_slug)  # if cb.data == 'no'
@dp.callback_query_handler(text=kb.variant_2_text_slug)  # if cb.data == 'yes'
async def inline_kb_answer_callback_handler(query: types.CallbackQuery):
    answer_data = query.data

    # always answer callback queries, even if you have nothing to say
    await query.answer(f'You answered with {answer_data!r}')
    kbm = types.InlineKeyboardMarkup()
    if answer_data == kb.variant_1_text_slug:
        kbm = kb.keyboard_markup_2
    elif answer_data == kb.variant_2_text_slug:
        kbm = kb.keyboard_markup_words
    else:
        text = f'Unexpected callback data {answer_data!r}!'

    await query.message.answer("Выберите уровень: \n", reply_markup=kbm)


@dp.callback_query_handler(text='a2')
@dp.callback_query_handler(text='b1')
async def inline_kb_answer_callback_handler(query: types.CallbackQuery):
    for test in polls.pollColection:
        await bot.send_poll(query.from_user.id, question=test.question, options=test.options,
                            is_anonymous=test.is_anonymous, type=test.type,
                            correct_option_id=test.correct_option_id,
                            allows_multiple_answers=test.allows_multiple_answers)


@dp.callback_query_handler(text='a2_w')
@dp.callback_query_handler(text='b1_w')
async def inline_kb_answer_callback_handler(query: types.CallbackQuery):
    for word in audios.Words:
        if word in audios.Words:
            await bot.send_message(query.from_user.id, word)
            await bot.send_audio(query.from_user.id, audio=open(audios.Audios[word], 'rb'))


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.answer("Напиши мне , и я помогу выучить английский!")


@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)


if __name__ == '__main__':
    executor.start_polling(dp)
