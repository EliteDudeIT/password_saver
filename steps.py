from aiogram.fsm.state import StatesGroup, State

class Steps(StatesGroup):
    start = State()
    login = State()
    test = State()