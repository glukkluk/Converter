from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart

from aiogram_dialog import DialogManager, StartMode

from states.user import StartSG

from core.api.api_helper import user_repository

router = Router()


@router.message(CommandStart())
async def bot_start(message: Message, dialog_manager: DialogManager):
    data = {
        "user_id": message.from_user.id,
        "first_name": message.from_user.first_name,
        "last_name": message.from_user.last_name
    }

    user_repository.create_user(data=data)

    await dialog_manager.start(state=StartSG.start_st, mode=StartMode.RESET_STACK)

