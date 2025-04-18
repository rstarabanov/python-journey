def yes_no(question):
    print("#####################")

    print(question)
    choise = input("Выбор: ").strip().lower()

    print("#####################")
    match choise:
        case "да":
            return True
        case "нет":
            return False
        case _:
            return yes_no(question)
