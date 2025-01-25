import os

from aiogram.types import Message, CallbackQuery
from aiogram.enums import ContentType

from aiogram_dialog import DialogManager, ShowMode
from aiogram_dialog.widgets.kbd import Button, Radio
from aiogram_dialog.widgets.input import MessageInput

from states.user import ConvertSG


async def image_handler(
    message: Message, widget: MessageInput, dialog_manager: DialogManager, **kwargs
):
    if not os.path.exists("bot/media"):
        os.mkdir("bot/media")

    match message.content_type:
        case ContentType.DOCUMENT:
            await message.bot.download(
                file=message.document,
                destination=os.path.join("bot/media", message.document.file_name),
            )

        case ContentType.PHOTO:
            await message.bot.download(
                file=message.photo[-1],
                destination=f"{os.path.join("bot/media", message.photo[-1].file_unique_id)}.jpg",
            )

    await dialog_manager.switch_to(ConvertSG.select_format_st, show_mode=ShowMode.SEND)


async def convert(
    callback: CallbackQuery, widget: Button, dialog_manager: DialogManager, **kwargs
):
    image_format = dialog_manager.find("select_format").get_checked()
    print(image_format)
