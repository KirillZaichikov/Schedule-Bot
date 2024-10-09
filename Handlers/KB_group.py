from aiogram import types
from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from scraper.shedule import WorkWithFile, GroupOfFiles

#files = GroupOfFiles()
Init_class = WorkWithFile()
Init_class.find_excel_file()
groups = Init_class.get_groups()



def kb():
    builder = ReplyKeyboardBuilder()
    for group in groups:
        builder.add(KeyboardButton(text=group))
    builder.adjust(4)
    return builder.as_markup(resize_keyboard=True)