from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart, Command

from aiogram_dialog import DialogManager, StartMode

from states.user import StartSG, ConvertSG

router = Router()


@router.message(CommandStart())
async def bot_start(message: Message, dialog_manager: DialogManager):
    await dialog_manager.start(StartSG.start_st, mode=StartMode.RESET_STACK)


@router.message(Command("convert"))
async def convert(message: Message, dialog_manager: DialogManager):
    await dialog_manager.start(ConvertSG.convert_st, mode=StartMode.RESET_STACK)

@router.message(F.document)
async def not_defined(message: Message):
    pass