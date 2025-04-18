from .main_logic import yes_no

def add_task(tasks_list, new_task):
    tasks_list.append(new_task)
    
def delete_task(tasks_list, index_task):
    print("#####################")
    
    if  0 <= index_task < len(tasks_list):
        print("Будет удалена следующая задача:")
        print(tasks_list[index_task])
        
        question = "вы уверены в удалении (Да/Нет)?"
        if yes_no(question):    
            tasks_list.pop(index_task)
            modified = True
        else:
            print("#####################")
            return
    else:
        print("Не действительный номер задачи")
        
    print("#####################")

def show_tasks(tasks_list):
    print("#####################")
    
    if len(tasks_list) == 0:
        print("Список задач пуст")
    else: 
        for i, element in enumerate(tasks_list, 1):
            print(f"{i}. {element}")
    
    print("#####################")