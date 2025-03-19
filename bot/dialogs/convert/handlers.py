import os

from aiogram.types import Message, CallbackQuery
from aiogram.enums import ContentType

from aiogram_dialog import DialogManager, ShowMode
from aiogram_dialog.widgets.kbd import Button, Radio
from aiogram_dialog.widgets.input import MessageInput

import tinify

from states.user import ConvertSG

from functional import convert_image


async def image_handler(
    message: Message, widget: MessageInput, dialog_manager: DialogManager, **kwargs
):
    if not os.path.exists("media"):
        os.mkdir("media")

    match message.content_type:
        case ContentType.DOCUMENT:
            filename = message.document.file_name

            dialog_manager.dialog_data.update(filename=filename)

            await message.bot.download(
                file=message.document,
                destination=os.path.join("media", filename),
            )

        case ContentType.PHOTO:
            filename = f"{message.photo[-1].file_unique_id}.jpeg"

            dialog_manager.dialog_data.update(filename=filename)

            await message.bot.download(
                file=message.photo[-1],
                destination=os.path.join("media", filename),
            )

    await dialog_manager.switch_to(ConvertSG.select_format_st, show_mode=ShowMode.SEND)


async def converting(
    callback: CallbackQuery, widget: Button, dialog_manager: DialogManager, **kwargs
):
    image_path = f"media/{dialog_manager.dialog_data.get("filename")}"
    image_format = dialog_manager.find("select_format").get_checked()

    is_resize_image = dialog_manager.find("resize").is_checked()

    convert_image(path=image_path, new_format=image_format)

    new_image_path = f"{os.path.splitext(image_path)[0]}.{image_format.lower()}"

    if is_resize_image:
        source = tinify.from_file(new_image_path)
        image_optimized_path = (
            f"{os.path.splitext(new_image_path)[0]}_optimized.{image_format.lower()}"
        )

        source.to_file(f"{image_optimized_path}")
        new_image_path = image_optimized_path

    dialog_manager.dialog_data.update(
        image_path=new_image_path,
    )

    await dialog_manager.switch_to(ConvertSG.upload_photo_st, show_mode=ShowMode.SEND)
