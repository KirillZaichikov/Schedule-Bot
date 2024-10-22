from Handlers import Reg, Workshedteacher
import asyncio
import logging
import sys
from config import TOKEN
from aiogram import Bot, Dispatcher

# Настройка логирования
logging.basicConfig(level=logging.INFO)

async def main():
    BOT = Bot(token=TOKEN)
    dp = Dispatcher()
    dp.include_router(Reg.router)
    dp.include_router(Workshedteacher.router)
    await dp.start_polling(BOT)

if __name__ == "__main__":
    print("\n\nБот запущен!\n\n")
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())