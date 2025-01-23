import os

from aiogram.types import Message
from aiogram.enums import ContentType

from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.input import MessageInput


async def image_handler(message: Message, dialog_manager: DialogManager, widget: MessageInput):
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
