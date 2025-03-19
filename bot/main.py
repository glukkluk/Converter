import asyncio
import logging
import betterlogging as bl

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from aiogram_dialog import setup_dialogs

import tinify


from handlers.bot_commands import BotCommands
from handlers.user import router as user_router
from dialogs import dialogs_list

from core.config import settings


def setup_logging():
    """
    Set up logging configuration for the application.

    This method initializes the logging configuration for the application.
    It sets the log level to INFO and configures a basic colorized log for
    output. The log format includes the filename, line number, log level,
    timestamp, logger name, and log message.

    Parameters
    ----------
        None

    Returns
    -------
        None

    Example usage:
        setup_logging()
    """
    log_level = logging.INFO
    bl.basic_colorized_config(level=log_level)

    logging.basicConfig(
        level=logging.INFO,
        format="%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s",
    )
    logger = logging.getLogger(__name__)
    logger.info("Starting bot")


async def main():
    setup_logging()

    tinify.key = settings.misc.tinify_api_key

    bot: Bot = Bot(
        settings.bot.bot_token,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )
    dp = Dispatcher(storage=MemoryStorage())

    await bot.set_my_commands(commands=[BotCommands.start])

    dp.include_routers(user_router, *dialogs_list)

    setup_dialogs(dp)

    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logging.error("Bot was stopped!")
