from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.text import Format

from dialogs.start.getters import start_getter
from states.user import StartSG

start_dialog = Dialog(
    Window(
        Format(
            "Привіт {user.first_name}!"
            "\nЯ бот для конвертації зображень."
            "\nЩоб розпочати використовуй команду /convert"
        ),
        state=StartSG.start_st,
        getter=start_getter,
    ),
)
