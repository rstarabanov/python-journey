def yes_no(question):
    print("#####################")
    
    print(question)
    choise = input("Выбор: ").strip().lower()
    
    print("#####################")
    match choise:
        case "Да": return True
        case "Нет": return False
        case _: return yes_no(question)