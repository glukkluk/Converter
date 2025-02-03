from dataclasses import dataclass

from aiogram.types import BotCommand


@dataclass
class BotCommands:
    start: BotCommand = BotCommand(command="start", description="Розпочати роботу")
