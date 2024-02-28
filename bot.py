import os
import asyncio
import logging

from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext

from keyboards import first_But, login_But
from steps import Steps

from conection import Password, session

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

logging.basicConfig(level=logging.INFO)
bot = Bot(token=os.getenv('Token'))
dp = Dispatcher()

@dp.message(Command('start'))
async def start(message: types.Message, state: FSMContext):
    await message.answer('Привіт!\n'
                         'Це бот для зберігання паролів😃', reply_markup=first_But)
    await state.set_state(Steps.start)

@dp.message(F.text == 'Start')
async def send_answer(message: types.Message, state: FSMContext):
    await message.answer('Для того, щоб перейти до паролів потрібно зареєструватися', reply_markup=login_But)
    await state.set_state(Steps.login)

@dp.message(F.text == 'Register')
async def send_answer(message: types.Message, state: FSMContext):
    await message.answer('Для реєстрації придумайте пароль')
    password = message.text
    new_password = Password(id=message.chat.id, password=message.text)
    session.add(new_password)
    session.commit()
    # await state.set_state(Steps.test)

@dp.message(F.text == 'Login')
async def send_answer(message: types.Message, state: FSMContext):
    await message.answer('Для входу введіть пароль')
    await state.set_state(Steps.test)

@dp.message(F.text)
async def test(message: types.Message, state: FSMContext):
    password = message.text
    password_check = 'test'
    tel_id = 983210261
    id = message.chat.id
    if password == password_check and tel_id == id:
        await message.answer('Пароль і логін вірні')
    else:
        await message.answer('Error')


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
