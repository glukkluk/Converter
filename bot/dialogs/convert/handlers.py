from aiogram.types import Message

from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.input import MessageInput

async def image_handler(
    message: Message,
    widget: MessageInput,
    dialog_manager: DialogManager,
):
    pass