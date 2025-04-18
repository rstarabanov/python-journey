import os
from .main_logic import yes_no

def load_tasks(file_name):    #считываем файл
    
    tasks_list = []
    
    #спрашиваем об очистке
    if len(tasks_list) != 0:
        question = "Для загрузки задач необходимо очистить список существующих задач. Очищаем (Да/Нет)?"
        if yes_no(question):    
            #очищаем список
            tasks_list.clear()
        else:
            return
    
    #проверяем существоание файла
    if os.path.isfile(file_name):
        with open(file_name, "r") as file:
            tasks_list.extend(line.strip() for line in file)
    else:
        open(file_name, 'w').close()
        
    return tasks_list
        
        
def save_tasks(tasks_list, file_name):
        
    print("#####################")

    with open(file_name, 'w') as f:
        for task in tasks_list:
            f.write(task + "\n")

    print("Задачи сохранены")    
    print("#####################")
