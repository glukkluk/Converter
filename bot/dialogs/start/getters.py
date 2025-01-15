from aiogram.types import User

from aiogram_dialog import DialogManager


async def start_getter(dialog_manager: DialogManager, aiogd_event_context, **kwargs):
    return {'user': aiogd_event_context.user}