# 3 Вывод рассписания с корриктеровками
# 4 Сделать кнопки перемещения в неделях


from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.filters import Command
from aiogram.types import Message, KeyboardButton, CallbackQuery
from aiogram import Router, F
from openpyxl import load_workbook
import sqlite3
from scraper.shedule import ReadGroupShedule, WorkWithFile

init_class = WorkWithFile()
init_class.find_excel_file()
path = init_class.path_to_file
router = Router()

def GetGroupUser(id):
    con = sqlite3.connect("Test_db.db")
    cur = con.cursor()
    user_group = cur.execute("""SELECT group_student FROM student WHERE user_id = ?""",
                          (id,)).fetchone()
    return user_group

# Вызов клавиатуры для просмотра рассписания
@router.message(Command("Shedule"))
async def show_schedule(message: Message):
    builder = ReplyKeyboardBuilder()
    builder.add(KeyboardButton(text="Посмотреть рассписание на неделю"))
    builder.add(KeyboardButton(text="Посмотреть рассписание на сегодня"))
    await message.answer("Для просмотра рассписание нажмите кнопку ниже",
                         reply_markup=builder.as_markup(resize_keyboard=True, one_time_keyboard=True, selective=True))

# Ответ на кнопку "Просмотреть расписание"
@router.message(F.text == "Посмотреть расписание на неделю")
async def get_schedule(message: Message):
    answer = ""
    user_group = GetGroupUser(message.from_user.id)
    shedule = ReadGroupShedule(path_to_file=path, group=user_group[0])
    for rows in shedule.iter_rows(min_row=16):
        for row in rows:
            if row.value != None:
                answer += row.value + "\n"
    await message.answer(answer)

@router.message(F.text == "Посмотреть расписание на сегодня")
async def get_shedule_today(message: Message):
    user_group = GetGroupUser(message.from_user.id)
