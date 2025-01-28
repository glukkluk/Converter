import os

from aiogram.types import Message, CallbackQuery
from aiogram.enums import ContentType

from aiogram_dialog import DialogManager, ShowMode
from aiogram_dialog.widgets.kbd import Button, Radio
from aiogram_dialog.widgets.input import MessageInput

from states.user import ConvertSG

from functional import convert_image


async def image_handler(
    message: Message, widget: MessageInput, dialog_manager: DialogManager, **kwargs
):
    if not os.path.exists("bot/media"):
        os.mkdir("bot/media")

    match message.content_type:
        case ContentType.DOCUMENT:
            filename = message.document.file_name

            dialog_manager.dialog_data.update(filename=filename, is_file=True)

            await message.bot.download(
                file=message.document,
                destination=os.path.join("bot/media", filename),
            )

        case ContentType.PHOTO:
            filename = f"{message.photo[-1].file_unique_id}.jpeg"

            dialog_manager.dialog_data.update(filename=filename, is_file=False)

            await message.bot.download(
                file=message.photo[-1],
                destination=os.path.join("bot/media", filename),
            )

    await dialog_manager.switch_to(ConvertSG.select_format_st, show_mode=ShowMode.SEND)


async def converting(
    callback: CallbackQuery, widget: Button, dialog_manager: DialogManager, **kwargs
):
    image_format = dialog_manager.find("select_format").get_checked()
    image_path = f"bot/media/{dialog_manager.dialog_data.get("filename")}"

    convert_image(path=image_path, new_format=image_format)
