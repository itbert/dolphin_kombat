import asyncio
import logging
from typing import Coroutine, Any

from aiogram import Bot, Dispatcher

from configuration.config_secret_data import TOKEN

from app_bot.handlers import router

bot = Bot(token=TOKEN)
dp = Dispatcher()


async def main_function():
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)  # УБРАТЬ ПОСЛЕ ТЕСТИРОВАНИЯ
    try:
        asyncio.run(main_function())
    except KeyboardInterrupt:
        print('Бот остановлен')
