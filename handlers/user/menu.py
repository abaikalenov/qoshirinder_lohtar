from aiogram.dispatcher.filters import Command, Text

from keyboards.default import menu
from aiogram.types import Message, CallbackQuery

from keyboard.inline.callback_datas import buy_callback
from keyboard.inline.choice_buttons import choice, pear_keyboard, apples_keyboard
from loader import dp, bot

@dp.message_handler(Command("menu"))
async def shoew_menu(message: Message):
    await message.answer("choose one wine for order", reply_markup=menu)

@dp.message_handler(Text(equals=["Toukas", "Shavenil", "Tarantello"]))
async def get_food(message: Message):
    await message.answer(f"Choosen {message.text}. Thanks for order", reply_markup=choice)

@dp.callback_query_handler(buy_callback.filter(item_name="alphaestate"))
async def buying_apples(call: CallbackQuery, callback_data:dict):
    await call.answer(cache_time=60)

    await call.message.answer(f"You chose Alpha Estate. Good luck.",
                              reply_markup=apples_keyboard)