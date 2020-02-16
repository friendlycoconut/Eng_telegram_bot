from aiogram import types
from slugify import slugify


keyboard_markup = types.InlineKeyboardMarkup(row_width=3, one_time_keyboard=True)

variant_1_text = 'Я хочу пройти тест'
variant_2_text = 'Я хочу выучить слова'

text_and_data = [
    [variant_1_text, slugify(variant_1_text)],
    [variant_2_text, slugify(variant_1_text)],
]

row_btns = (types.InlineKeyboardButton(text, callback_data=data) for text, data in text_and_data)

keyboard_markup.row(*row_btns)
keyboard_markup.add(
    types.InlineKeyboardButton('Статистика', url='https://github.com/aiogram/aiogram'),
)


keyboard_markup_2 = types.InlineKeyboardMarkup(one_time_keyboard=True)
text_and_data_2 = (
    ('A2 level', 'a2'),
)
row_btns_2 = (types.InlineKeyboardButton(text, callback_data=data) for text, data in text_and_data_2)
keyboard_markup_2.add(*row_btns_2)

keyboard_markup_words = types.InlineKeyboardMarkup(one_time_keyboard=True)
text_and_data_words = (
    ('A2 words', 'a2_w'),
)
row_btns_words=(types.InlineKeyboardButton(text, callback_data=data) for text, data in text_and_data_words)
keyboard_markup_words.add(*row_btns_words)