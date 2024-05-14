from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, ReplyKeyboardMarkup

from lexicon.lexicon_ru import LEXICON_RU


# Кнопка старт
start_button = KeyboardButton(
    text = 'Старт'
)
start_keyboard = ReplyKeyboardMarkup(
    keyboard=[[start_button]],
    resize_keyboard=True, 
    one_time_keyboard=True
)

#WELCOME KEYBOARD
point_guard_button = InlineKeyboardButton(
    text = 'Разыгрывающий PG',
    callback_data= 'PG' 
)
shooting_guard_button = InlineKeyboardButton(
    text = 'Атакующий защитник SG',
    callback_data= 'SG' 
)
small_forward_button = InlineKeyboardButton(
    text = 'Легкий форвард SF',
    callback_data= 'SF' 
)
power_forward_button = InlineKeyboardButton(
    text = 'Мощный форвард PF',
    callback_data= 'PF' 
)
center_button = InlineKeyboardButton(
    text = 'Центровой C',
    callback_data= 'C' 
)
welcome_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[point_guard_button,shooting_guard_button],
                     [small_forward_button],
                     [power_forward_button,center_button]]
)