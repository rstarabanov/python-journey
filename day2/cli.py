import argparse  # 1. Подключаем модуль
from todo import add_task, delete_task, show_tasks, load_tasks, save_tasks  #Подключаем наши функции

file_name = "todo.txt"

parser = argparse.ArgumentParser(description="ToDo CLI — управление задачами из терминала")  # 2. Создаём парсер
parser.add_argument("command", help="Команда: show / add / delete")  # 3. Добавляем аргументы (или подкоманды)
parser.add_argument("param", nargs="?", help="Параметр команды. Используется с командами add / delete")  # 3. Добавляем аргументы (или подкоманды)

args = parser.parse_args()  # 4. Парсим аргументы (анализируем, что ввёл пользователь)

# 5. Используем результат
match args.command:
    case "show":
        print("Показать список задач") #show_tasks()
        show_tasks(load_tasks(file_name))
    case "add":
        print("Добавить задачу") #add_task(args.text)
        tasks_list = load_tasks(file_name)
        add_task(tasks_list, args.param)
        save_tasks(tasks_list, file_name)
        tasks_list.clear()
    case "delete":
        print("Удалить задачу") #delete_task(args.number)
        tasks_list = load_tasks(file_name)
        modified = delete_task(tasks_list, int(args.param)-1)
        if not modified:
            save_tasks(tasks_list, file_name)
        tasks_list.clear()
    case _:
        print("Неверная команда")