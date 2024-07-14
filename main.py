

def main():
    greeting = '''Привет! Добро пожаловать в программу работы 
с банковскими транзакциями. 
Выберите необходимый пункт меню:\n
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла'''
    input_user_file = input(f"{greeting}\n")

    while input_user_file not in ["1", "2", "3"]:
        print("\nВвели некорректный символ\nПопробуйте еще раз:")
        input_user_file = input()
    else:
        if input_user_file == "1":
            print("\nДля обработки выбран JSON-файл.")
        elif input_user_file == "2":
            print("\nДля обработки выбран CSV-файл.")
        elif input_user_file == "3":
            print("\nДля обработки выбран XLSX-файл.")

    next_choice_state = '''\nВведите статус, по которому необходимо выполнить фильтрацию. 
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING'''
    input_user_state = input(f"{next_choice_state}\n").upper()

    while input_user_state not in ["EXECUTED", "CANCELED", "PENDING"]:
        print(f"\nСтатус операции {input_user_state} недоступен.\n{next_choice_state}")
        input_user_state = input().upper()
    else:
        if input_user_state == "EXECUTED":
            print('\nОперации отфильтрованы по статусу "EXECUTED"')
        elif input_user_state == "CANCELED":
            print('\nОперации отфильтрованы по статусу "CANCELED"')
        elif input_user_state == "PENDING":
            print('\nОперации отфильтрованы по статусу "PENDING"')

    next_choice_data = '''\nОтсортировать операции по дате? Да/Нет'''
    input_user_data = input(f"{next_choice_data}\n").lower()
    while input_user_data not in ["да", "нет"]:
        print(f"\nВвели некорректный символ\nПопробуйте еще раз:")
        input_user_data = input(f"{next_choice_data}\n").lower()

    next_choice_ascending = '''\nОтсортировать по возрастанию или по убыванию?'''
    input_user_ascending = input(f"{next_choice_ascending}\n").lower()
    while input_user_ascending not in ["по возрастанию", "по убыванию"]:
        print(f"\nВвели некорректную сортировку\nПопробуйте еще раз:")
        input_user_ascending = input(f"{next_choice_ascending}\n").lower()

    next_choice_rub = '''\nВыводить только рублевые тразакции? Да/Нет'''
    input_user_rub = input(f"{next_choice_rub}\n").lower()
    while input_user_rub not in ["да", "нет"]:
        print(f"\nВвели некорректную сортировку\nПопробуйте еще раз:")
        input_user_rub = input(f"{next_choice_rub}\n").lower()

    next_choice_word = '''\nОтфильтровать список транзакций по определенному слову в описании? Да/Нет'''
    input_user_word = input(f"{next_choice_word}\n").lower()
    while input_user_word not in ["да", "нет"]:
        print(f"\nВвели некорректную сортировку\nПопробуйте еще раз:")
        input_user_word = input(f"{next_choice_word}\n").lower()


if __name__ == "__main__":
    print(main())
