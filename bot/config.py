from dataclasses import dataclass

from environs import Env

@dataclass
class Bot:
    """
    Bot configuration class.

    Attributes
    ----------
    token : str
        The token used to connect to the telegram bot.
    """
    token: str

    @staticmethod
    def from_env(env: Env) -> "Bot":
        """
        Creates the Bot object from environment variables.

        Parameters
        ----------
        env : Env
            The environment variables.

        Returns
        -------
        Bot
            The Bot object.
        """

        token: str = env.str("BOT_TOKEN")

        return Bot(token=token)

@dataclass
class Config:
    """
    The main configuration class that integrates all the other configuration classes.

    This class holds the other configuration classes, providing a centralized point of access for all settings.

    Attributes
    ----------
    bot : Bot
        Holds the settings related to the Telegram Bot.
    """
    bot: Bot


def load_config(path: str) -> Config:
    """
    Loads the configuration from an environment file.

    Parameters
    ----------
    path : str
        The path of env file from where to load the configuration variables.

    Returns
    -------
    Config
        The loaded configuration.
    """

    env = Env()
    env.read_env(path)

    return Config(bot=Bot.from_env(env))