# 2 Вывод рассписания без корриктеровок
# 3 Сделать кнопки перемещения в неделях
# 4 Вывод рассписания с корриктеровками
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.filters import Command
from aiogram.types import Message, KeyboardButton
from aiogram import Router, F
from openpyxl import load_workbook
import sqlite3
from datetime import datetime
from scraper.shedule import ReadExcel, WorkWithFile

init_class = WorkWithFile()
init_class.find_excel_file()
path = init_class.path_to_file
router = Router()
today = datetime.now()
day_week = ["ПН", "ВТ", "СР", "ЧТ", "ПТ", "СБ",]

# Вызов клавиатуры для просмотра рассписания
@router.message(Command("Shedule"))
async def show_schedule(message: Message):
    builder = ReplyKeyboardBuilder()
    builder.add(KeyboardButton(text="Посмотреть рассписание"))
    await message.answer("Для просмотра рассписание нажмите кнопку ниже",
                         reply_markup=builder.as_markup(resize_keyboard=True, one_time_keyboard=True, selective=True))

# Ответ на кнопку "Просмотреть рассписание"
@router.message(F.text == "Посмотреть рассписание")
async def get_schedule(message: Message):
    con = sqlite3.connect("Test_db.db")
    cur = con.cursor()
    answer = ""
    user_group = cur.execute("""SELECT group_student FROM student WHERE user_id = ?""",
                          (message.from_user.id,)).fetchone() # информация о группе студента
    shedule = ReadExcel.Read(path_to_file=path, group=user_group[0])
    for rows in shedule.iter_rows(min_row=16):
        for row in rows:
            if row.value != None:
                answer += row.value + "\n"
    await message.answer(answer)