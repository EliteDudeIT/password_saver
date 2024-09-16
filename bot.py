import os
import bcrypt
import asyncio
import logging

from aiogram import Bot, Dispatcher, types, F, Router
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext

from keyboards import first_But, login_But, mes
from steps import Steps

from conection import Password, session

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

logging.basicConfig(level=logging.INFO)
bot = Bot(token=os.getenv('Token'))
dp = Dispatcher()
router = Router()

dp.include_router(router)

@router.message(Command('start'))
async def start(message: types.Message, state: FSMContext):
    await message.answer('Привіт!\n'
                         'Це бот для зберігання паролів😃', reply_markup=first_But)
    await state.set_state(Steps.start)

@router.message(F.text == 'Start')
async def send_answer(message: types.Message, state: FSMContext):
    await message.answer('Для того, щоб перейти до паролів потрібно зареєструватися або залогінитися', reply_markup=login_But)
    await state.set_state(Steps.register_login)

@router.message(Steps.register_login, F.text)
async def register_login(message: types.Message, state: FSMContext):
    if message.text == 'Register':
        await message.answer('Для реєстрації придумайте пароль')
        await state.set_state(Steps.register)
    if message.text == 'Login':
        await message.answer('Для входу введіть пароль')
        await state.set_state(Steps.login)

@router.message(Steps.register, F.text)
async def register(message: types.Message, state: FSMContext):
    # new_password = Password(id=message.chat.id, password=message.text)
    # session.add(new_password)
    # session.commit()

    hash_password = bcrypt.hashpw(message.text.encode(), bcrypt.gensalt())
    new_password = Password(id=message.chat.id, password=hash_password)
    print(hash_password)
    session.add(new_password)
    session.commit()

@router.message(Steps.login, F.text)
async def login(message: types.Message, state: FSMContext):
    password_check = session.query(Password).filter(Password.id == message.chat.id).first()
    if password_check:
        if bcrypt.checkpw(message.text.encode(), password_check.password):
            await message.answer('Пароль і логін вірні')
            await message.answer('Обирайте Кнопку для зберігання паролю', reply_markup=mes)
            await state.set_state(Steps.messengers)
        else:
            await message.answer('Error')

@router.callback_query(Steps.messengers, F.data)
async def messengers(callback: types.CallbackQuery, state: FSMContext):
    if callback.data == 'git':
        await callback.message.answer('Введіть логін для GitHub')
        await state.set_state(Steps.git)

@router.message(Steps.git, F.text)
async def git(message: types.Message, state: FSMContext):
    git_login = message.text
    print(git_login)
    await message.answer('Введіть пароль')
    await state.set_state(Steps.git_password)
@router.message(Steps.git_password, F.text)
async def git_password(message: types.Message, state: FSMContext):
    git_password = message.text
    print('git password', git_password)
@router.callback_query(Steps.messengers, F.data)
async def messengers2(callback: types.CallbackQuery, state: FSMContext):
    if callback.data == 'dis':
        await callback.message.answer('Введіть логін для Discord')
        await state.set_state(Steps.git)

@router.callback_query(Steps.messengers, F.data)
async def messengers3(callback: types.CallbackQuery, state: FSMContext):
    if callback.data == 'gygl':
        await callback.message.answer('Введіть логін для Google')
        await state.set_state(Steps.git)

@router.callback_query(Steps.messengers, F.data)
async def messengers4(callback: types.CallbackQuery, state: FSMContext):
    if callback.data == 'fb':
        await callback.message.answer('Введіть логін для FoceBook')
        await state.set_state(Steps.git)

@router.callback_query(Steps.messengers, F.data)
async def messengers5(callback: types.CallbackQuery, state: FSMContext):
    if callback.data == 'stm':
        await callback.message.answer('Введіть логін для Steam')
        await state.set_state(Steps.git)

@router.callback_query(Steps.messengers, F.data)
async def messengers6(callback: types.CallbackQuery, state: FSMContext):
    if callback.data == 'tvtw':
        await callback.message.answer('Введіть логін для Twitch')
        await state.set_state(Steps.git)

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
