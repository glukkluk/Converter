from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.text import Const, Format
from aiogram_dialog.widgets.kbd import Start

from states.user import StartSG, ConvertSG

from .getters import start_getter

start_dialog = Dialog(
    Window(
        Format(
            text="<b>Привіт {user.first_name}!</b>"
            "\nЯ бот для конвертації зображень."
        ),
        Start(
            text=Const("🚩 Розпочати"),
            id="convert",
            state=ConvertSG.image_input_st,
        ),
        state=StartSG.start_st,
        getter=start_getter,
    ),
)
