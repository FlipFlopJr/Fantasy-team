from aiogram import Bot, types, Dispatcher
from config_data.config import Config, load_config


# Загружаем конфиг в переменную config
config: Config = load_config()

# Инициализируем бот и диспетчер
bot = Bot(token=config.tg_bot.token, 
    #   parse_mode='HTML'
        )
dp = Dispatcher()