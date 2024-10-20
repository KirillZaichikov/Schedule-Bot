from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from scraper.shedule import WorkWithFile, GroupOfFiles


Init_class = WorkWithFile() # Инициализация класса
Init_class.find_excel_file() # Поиск файла
groups = Init_class.get_groups() # берём названия групп


# Функция создания клавиатуры
def kb():
    builder = ReplyKeyboardBuilder()
    for group in groups[0:-1:]:
        builder.add(KeyboardButton(text=group))
    builder.adjust(4)
    return builder.as_markup(resize_keyboard=True,
                             one_time_keyboard=True,
                             input_field_placeholder="Выберите группу",
                             selective=True
                             ) # Настройка клавиатуры