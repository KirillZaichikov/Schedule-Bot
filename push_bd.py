from scraper.shedule import *


def main():
    group_of_files = GroupOfFiles()
    file_handler = WorkWithFile()
    file_handler.find_excel_file()

    # Получаем название групп (имен листов) из файла
    groups = file_handler.get_groups()
    if not groups:
        print("Нет доступных групп.")
        return

    # Получаем сегодняшнюю дату
    date = Date()
    today_info = date.TodayDate()
    print("Сегодняшняя дата:", today_info)

    # Обрабатываем расписание для каждой группы
    for group in groups:
        print(f"Чтение расписания для группы: {group}")

        # Читаем расписание и обрабатываем текст
        schedule = WorkWithText(group, file_handler.path_to_file)

        # Если расписание пустое, пропускаем
        if not schedule:
            print(f"Нет расписания для группы: {group}")
            continue

        # Сохраняем расписание в базу данных
        table(schedule, group)


if __name__ == "__main__":
    main()