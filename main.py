import asyncio
import logging
import sys
import sqlite3
from config import TOKEN
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command, CommandObject
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import ContentType, Message, CallbackQuery, KeyboardButton, InlineKeyboardButton
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.methods import DeleteMessage


# Config logging
logging.basicConfig(level=logging.INFO)

# BOt token and dispatcher
BOT = Bot(token=TOKEN)
dp = Dispatcher()



async def main():
    await dp.start_polling(BOT)

if __name__ == "__main__":
    print("\n\nBot started!\n\n")
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())