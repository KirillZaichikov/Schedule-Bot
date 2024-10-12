# 2 Вывод рассписания без корриктеровок
# 3 Сделать кнопки перемещения в неделях
# 4 Вывод рассписания с корриктеровками
from aiogram.utils.keyboard import ReplyKeyboardBuilder, ReplyKeyboardMarkup
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, KeyboardButton
from aiogram import Router, F

router = Router()

@router.message(Command("Shedule"))
async def show_schedule(message: Message):
    builder = ReplyKeyboardBuilder()
    builder.add(KeyboardButton(text="Посмотреть рассписание"))
    await message.answer("Для просмотра най рассписание нажмите кнопку ниже",
                         reply_markup=builder.as_markup(resize_keyboard=True, one_time_keyboard=True, selective=True))


@router.message(F.text == "Посмотреть рассписание")
async def get_schedule(message: Message):
    await message.answer("Рассписание")