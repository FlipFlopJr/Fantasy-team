import asyncio
import logging

from aiogram import Bot, Dispatcher
from config_data.config import Config, load_config
from handlers import other_handlers, start_handlers, choose_players
from config_data.dispatcher import dp, bot




# Функция конфигурирования и запуска бота
async def main():

    dp.include_router(start_handlers.router)
    dp.include_router(choose_players.router)
    dp.include_router(other_handlers.router)

    # Пропускаем накопившиеся апдейты и запускаем polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


asyncio.run(main())