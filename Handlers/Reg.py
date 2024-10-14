import sqlite3
from aiogram import Router, F
from aiogram.filters import Command, StateFilter
from aiogram.types import Message, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from Handlers.KB_group import groups, kb

router = Router()

endl = "\n"
global user_id


class Reg_user(StatesGroup):
    student_or_teacher = State()  # Добавлено следующее состояние
    name_user = State()
    group = State()


@router.message(StateFilter(None), Command("start"))
async def start(message: Message, state: FSMContext):
    user_id = message.from_user.id
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(
        text="Я студент",
        callback_data="Student")
    )
    builder.add(InlineKeyboardButton(
        text="Я преподаватель",
        callback_data="Teacher")
    )
    await message.answer("Здравствуйте! Давайте пройдем регистрацию. \nДля начала я бы хотел узнать, вы студент или преподаватель?",
                         reply_markup=builder.as_markup())
    await state.set_state(Reg_user.student_or_teacher)


@router.callback_query(F.data == "Student", Reg_user.student_or_teacher)
async def Reg(callback: CallbackQuery, state: FSMContext):
    await state.update_data(student_or_teacher=callback.data)
    await callback.message.answer(
        "Отлично! \nТеперь давайте познакомимся, как вас зовут?")
    await state.set_state(Reg_user.name_user)


@router.callback_query(F.data == "Teacher")
async def set_test_teacher(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer("тест пройден")


@router.message(Reg_user.name_user)
async def set_name_user(message: Message, state: FSMContext):
    await state.update_data(name_user=message.text)
    await message.answer("И на последок я хотел бы узнать вашу группу.", reply_markup=kb())
    await state.set_state(Reg_user.group)


@router.message(Reg_user.group)
async def Reg(message: Message, state: FSMContext):
    if message.text in groups:
        await state.update_data(group=message.text)
        data = await state.get_data()
        await message.answer(f"Будем знакомы {data.get("name_user")}! \nТеперь вы можете запрашивать расписание всего лишь одной кнопкой. Для продолжения используйте комманду /Shedule")
        data = await state.get_data()
        con = sqlite3.connect("Test_db.db")
        cur = con.cursor()
        if data.get("student_or_teacher") == "Student":
            user = cur.execute("SELECT * FROM student WHERE user_id=?", (message.from_user.id,)).fetchone()
            if user is None:
                cur.execute(""" INSERT INTO student (user_id, NameStudent, group_student) VALUES (?, ?, ?)""",
                            (message.from_user.id, data.get("name_user"), data.get("group"),))
                con.commit()
                con.close()
    else:
        pass