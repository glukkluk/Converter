from aiogram.enums import ContentType

from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.text import Const
from aiogram_dialog.widgets.input import MessageInput

from states.user import ConvertSG

from dialogs.convert.handlers import image_handler

convert_dialog = Dialog(
    Window(
        Const("Надішліть зображення (бажано як файл)"),
        MessageInput(
            func=image_handler,
            content_types=[ContentType.DOCUMENT, ContentType.PHOTO],
        ),
        state=ConvertSG.convert_st,
    ),
)