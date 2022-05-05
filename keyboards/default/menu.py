from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Toukas"),
        ],
        [
            KeyboardButton(text="Tarantello"),
        ],
        [
            KeyboardButton(text="Shavenil"),
        ],
    ],
    resize_keyboard=True
)