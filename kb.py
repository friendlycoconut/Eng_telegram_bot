from aiogram import types
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from slugify import slugify


button_hi = KeyboardButton('Привет! 👋')

greet_kb = ReplyKeyboardMarkup()
greet_kb.add(button_hi)

keyboard_markup = types.InlineKeyboardMarkup(row_width=3, one_time_keyboard=True)
# default row_width is 3, so here we can omit it actually
# kept for clearness
variant_1_text = 'Я хочу пройти тест'
variant_1_text_slug = slugify(variant_1_text)
variant_2_text = 'Я хочу выучить слова'
variant_2_text_slug = slugify(variant_2_text)

text_and_data = (
    (variant_1_text, variant_1_text_slug),
    (variant_2_text, variant_2_text_slug),
)
# in real life for the callback_data the callback data factory should be used
# here the raw string is used for the simplicity
row_btns = (types.InlineKeyboardButton(text, callback_data=data) for text, data in text_and_data)

keyboard_markup.row(*row_btns)
keyboard_markup.add(
    # url buttons have no callback data
    types.InlineKeyboardButton('Статистика', url='https://github.com/aiogram/aiogram'),
)


keyboard_markup_2 = types.InlineKeyboardMarkup(one_time_keyboard=True)
text_and_data_2 = (
    ('A2 level', 'a2'),
)
row_btns_2=(types.InlineKeyboardButton(text, callback_data=data) for text, data in text_and_data_2)
keyboard_markup_2.add(*row_btns_2)

keyboard_markup_words = types.InlineKeyboardMarkup(one_time_keyboard=True)
text_and_data_words = (
    ('A2 words', 'a2_w'),
)
row_btns_words=(types.InlineKeyboardButton(text, callback_data=data) for text, data in text_and_data_words)
keyboard_markup_words.add(*row_btns_words)