from aiogram import Router, F
from aiogram.filters import Command, StateFilter
from aiogram.types import Message, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from Handlers.KB_group import groups, kb

password=["123"]#Пароль от Преподовательского аккаунта!!

router = Router()

endl = "\n"

class Reg_user(StatesGroup):
    student_or_teacher = State()  # Добавлено следующее состояние
    name_user = State()
    group = State()
    access_code = State()


@router.message(StateFilter(None),Command("start"))
async def start(message: Message, state: FSMContext):
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
    await callback.message.answer("Для продолжения введите ваш индивидуальный код")
    await state.set_state(Reg_user.access_code)  # Устанавливаем состояние для ввода кода доступа

@router.message(Reg_user.access_code)
async def process_access_code(message: types.Message, state: FSMContext):
    if message.text in password:
        await message.answer("Код принят!")
        await state.update_data(student_or_teacher="Teacher")  # Сохраняем данные
        await state.set_state(Reg_user.group)  # Переход к следующему состоянию
        await state.update_data(group="all")
        await state.set_state(Reg_user.name_user)  # Переход к следующему состоянию
        await message.answer("Отлично! \nТеперь давайте познакомимся, как вас зовут?")
    else:
        await message.answer("Код не принят. Попробуйте еще раз.")



@router.message(Reg_user.name_user)
async def set_name_user(message: Message, state: FSMContext):
    await state.update_data(name_user=message.text)  # Сохраняем имя пользователя
    data = await state.get_data()  # Получаем данные из состояния
    student_or_teacher = data.get("student_or_teacher")  # Получаем информацию о роли пользователя


    if student_or_teacher == "Student":
        await message.answer("И на последок я хотел бы узнать вашу группу.", reply_markup=kb())
        await state.set_state(Reg_user.group)
    else:
        await message.answer("Отлично!! \nТеперь вы можете посмотреть расписание любой группы, при помощи команды /Couples")
        print(data.get("student_or_teacher"), "\n", data.get("name_user"))  # Используем \n для новой строки
        await state.clear()


@router.message(Reg_user.group)
async def Reg(message: Message, state: FSMContext):
    if message.text in groups:
        await state.update_data(group=message.text)
        data = await state.get_data()
        await message.answer(f"Будем знакомы {data.get("name_user")}! \nТеперь вы можете запрашивать расписание всего лишь одной кнопкой.")
        print(data.get('student_or_teacher'), endl, data.get('name_user'), endl, data.get('group'))
        await state.clear()
    else:
        pass
