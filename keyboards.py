from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup

first_But = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Start')
        ],
    ], resize_keyboard=True
)
login_But = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Login')
        ],
        [
            KeyboardButton(text='Register')
        ]
    ], resize_keyboard=True
)