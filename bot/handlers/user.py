from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart

from aiogram_dialog import DialogManager, StartMode

from states.user import StartSG

router = Router()


@router.message(CommandStart())
async def bot_start(message: Message, dialog_manager: DialogManager):
    await dialog_manager.start(state=StartSG.start_st, mode=StartMode.RESET_STACK)

