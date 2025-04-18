from aiogram.fsm.state import State, StatesGroup


class StartSG(StatesGroup):
    start_st = State()


class ConvertSG(StatesGroup):
    image_input_st = State()
    select_format_st = State()
    upload_photo_st = State()