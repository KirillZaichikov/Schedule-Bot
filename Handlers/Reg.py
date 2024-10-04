from aiogram import Router, F
from aiogram.filters import Command, CommandStart, StateFilter
from aiogram.types import Message, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

router = Router()

endl = "\n"


class Reg_user(StatesGroup):
    name_user = State()
    student_or_teacher = State()  # Добавлено следующее состояние
    group = State()


@router.message(StateFilter(None),CommandStart)
async def start(message: Message, state: FSMContext):
    await message.answer(
        "Здравствуйте! \nДавайте пройдем регистрацию. \nДля начала давайте познакомимся, как вас зовут")
    await state.set_state(Reg_user.name_user)


@router.message(Reg_user.name_user)
async def Reg(message: Message, state: FSMContext):
    await state.update_data(name_user=message.text)
    data = await state.get_data()
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(
        text="Я студент",
        callback_data="Student")
    )
    builder.add(InlineKeyboardButton(
        text="Я преподаватель",
        callback_data="Teacher")
    )
    await message.answer(f"Приятно познакомиться, {data['name_user']}! \nВы студент или преподаватель?",
                         reply_markup=builder.as_markup())
    await state.set_state(Reg_user.student_or_teacher)


@router.callback_query(F.data == "Teacher")
async def send_random_value(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer("тест пройден")


@router.callback_query(F.data == "Student", Reg_user.student_or_teacher)
async def send_random_value(callback: CallbackQuery, state: FSMContext):
    await state.update_data(student_or_teacher=callback.data)
    await callback.message.answer("Так и запишем! \nНа последок я хотел бы узнать вашу группу?")
    await state.set_state(Reg_user.group)

@router.message(Reg_user.group)
async def Reg(message: Message, state: FSMContext):
    await state.update_data(group=message.text)
    data = await state.get_data()
    await message.answer(f"Приятно познакомиться, {data['name_user']}! \nВаша группа: {data['group']}")
    print(data.get('name_user'), endl, data.get('student_or_teacher'), endl, data.get('group'))
    await state.clear()
