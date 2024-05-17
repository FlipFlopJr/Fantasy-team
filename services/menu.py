from config_data.dispatcher import bot
from aiogram import F, Router
from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


router = Router()


async def set_commands(bot: Bot):
    commands = [
        BotCommand(
            command='start',
            description='Запускаем бота'
        ),
        BotCommand(
            command='team',
            description='Собираем команду'
        ),
        BotCommand(
            command='show_team',
            description="Показываем состав команды"
        )
    ]

    await bot.set_my_commands(commands, BotCommandScopeDefault())