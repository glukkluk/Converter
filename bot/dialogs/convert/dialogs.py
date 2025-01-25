import operator

from aiogram.enums import ContentType

from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.text import Const, Format
from aiogram_dialog.widgets.kbd import Button, Radio
from aiogram_dialog.widgets.input import MessageInput

from states.user import ConvertSG

from .handlers import image_handler, convert
from .getters import get_photo_conversion_formats


convert_dialog = Dialog(
    Window(
        Const("Надішліть ваше зображення"),
        MessageInput(
            func=image_handler,
            content_types=[ContentType.DOCUMENT, ContentType.PHOTO],
        ),
        state=ConvertSG.image_input_st,
    ),
    Window(
        Const("Виберіть формат"),
        Radio(
            checked_text=Format("🔘 {item[0]}"),
            unchecked_text=Format("⚪️ {item[0]}"),
            id="select_format",
            item_id_getter=operator.itemgetter(0),
            items="formats",
        ),
        Button(
            text=Const("Конвертувати"),
            id="run_conversion",
            on_click=convert,
        ),
        state=ConvertSG.select_format_st,
        getter=get_photo_conversion_formats
    )
)