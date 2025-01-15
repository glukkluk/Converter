from aiogram.fsm.state import State, StatesGroup


class StartSG(StatesGroup):
    start_st = State()


class ConvertSG(StatesGroup):
    convert_st = State()