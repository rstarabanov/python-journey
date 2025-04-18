import os

file_name = "todo.txt"
task_list = []
modified = False

def yes_no(question):
    print("#####################")
    
    print(question)
    choise = input("Выбор: ").strip().lower()
    
    print("#####################")
    match choise:
        case "Да": return True
        case "Нет": return False
        case _: return yes_no(question)
    

def show_menu(): #показывает меню и возвращает результат выбора
    print("#####################")
    
    print("1. Прочитать задачи из файла")
    print("2. Показать список задач")
    print("3. Добавить новую задачу")
    print("4. Удалить задачу (по номеру)")
    print("5. Выход (с сохранением)")

    print("#####################")

    return input("Выбор: ")

def read_file():    #считываем файл
    global task_list
    global modified
    
    #спрашиваем об очистке
    if len(task_list) != 0:
        question = "Для загрузки задач необходимо очистить список существующих задач. Очищаем (Да/Нет)?"
        if yes_no(question):    
            #очищаем список
            task_list.clear()
        else:
            return
    
    #проверяем существоание файла
    if os.path.isfile(file_name):
        with open(file_name, "r") as file:
            task_list.extend(line.strip() for line in file)
    else:
        open(file_name, 'w').close()
        
    modified = False

def show_tasks():
    global task_list
    
    print("#####################")
    
    if len(task_list) == 0:
        print("Список задач пуст")
    else: 
        for i, element in enumerate(task_list, 1):
            print(f"{i}. {element}")
    
    print("#####################")
    
def add_task():
    global modified
    global task_list
    
    print("#####################")
    
    new_line = input("Введите наименование задачи:")
    
    if len(new_line) == 0:
        print("Отмена ввода новой задачи")
    else:
        task_list.append(new_line)
        modified = True
        
    print("#####################")

def delete_task():
    global modified
    global task_list
    
    print("#####################")
    try:
        number_element = int(input("Введите индекс задачи:")) - 1
    except:
        print("Ошибка ввода номера")
        print("#####################")
        return    
    
    if  0 <= number_element <= len(task_list):
        print("Будет удалена следующая задача:")
        print(task_list[number_element])
        
        question = "вы уверены в удалении (Да/Нет)?"
        if yes_no(question):    
            task_list.pop(number_element)
            modified = True
        else:
            print("#####################")
            return
    else:
        print("Не действительный номер задачи")
    print("#####################")
    
def exit_todo():
    global modified
    global task_list
    
    if modified:
        
        print("#####################")
        
        question = "Список задач был изменен. Сохранить в файл (Да/Нет)?"
        if yes_no(question):    
            file = open(file_name, 'w+')
            
            for element in task_list:
                file.writelines(element + "\n")
            
            file.close()
            
            print("#####################")
        else:
            print("#####################")
            return
        
    else:
        return
    
choise = show_menu()
while choise != "5":
    match choise:
        case "1": read_file()   #//Чтение списка задач
        case "2": show_tasks()  #//Показать список задач
        case "3": add_task()    #//Добавить новую задачу
        case "4": delete_task() #//Удалить задачу по номеру
        case "5": exit_todo()   #//Выход с вопросом сохранения
        case _: print("Повторите выбор.")
    choise = show_menu()