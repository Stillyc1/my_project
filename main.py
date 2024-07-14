from src.utils import get_info_transactions, get_info_transactions_csv, get_info_transactions_xlsx
from src.processing import filter_by_state, sort_by_date
from src.generators import filter_by_currency
from src.find_transactions import find_transactions


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
            result = get_info_transactions("../data/operations.json")  # Функция чтения json формата -> list[dict]
        elif input_user_file == "2":
            print("\nДля обработки выбран CSV-файл.")
            result = get_info_transactions_csv("../data/transactions.csv")  # Функция чтения csv формата - -||-
        elif input_user_file == "3":
            print("\nДля обработки выбран XLSX-файл.")
            result = get_info_transactions_xlsx("../data/transactions_excel.xlsx")  # Функция чтения xlsx формата - -||-

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

    result_state = filter_by_state(result, input_user_state)  # Функция фильтрации операций по статусу "state"
    # ->  list[dict]

    next_choice_data = '''\nОтсортировать операции по дате? Да/Нет'''
    input_user_data = input(f"{next_choice_data}\n").lower()
    while input_user_data not in ["да", "нет"]:
        print(f"\nВвели некорректный символ\nПопробуйте еще раз:")
        input_user_data = input(f"{next_choice_data}\n").lower()

    else:

        if input_user_data == "да":
            next_choice_ascending = '''\nОтсортировать по возрастанию или по убыванию?'''
            input_user_ascending = input(f"{next_choice_ascending}\n").lower()

            while input_user_ascending not in ["по возрастанию", "по убыванию"]:
                print(f"\nВвели некорректную сортировку\nПопробуйте еще раз:")
                input_user_ascending = input(f"{next_choice_ascending}\n").lower()

            else:

                if input_user_ascending == "по убыванию":
                    result_asceding = sort_by_date(result_state)  # функция сортирует операции по дате (по убыванию)
                    # -> list[dict]
                elif input_user_ascending == "по возрастанию":
                    result_asceding = sort_by_date(result_state, False)  # функция сортирует операции
                    # по дате (по возрастанию) -> list[dict]

    next_choice_rub = '''\nВыводить только рублевые тразакции? Да/Нет'''
    input_user_rub = input(f"{next_choice_rub}\n").lower()
    while input_user_rub not in ["да", "нет"]:
        print(f"\nВвели некорректную сортировку\nПопробуйте еще раз:")
        input_user_rub = input(f"{next_choice_rub}\n").lower()

    else:

        if input_user_rub == "да":
            result_rub = filter_by_currency(result_asceding, "RUB")  # Функция-генератор
            # фильтрует операции по ["currency"] ["RUB"] -> возвращает по одной транзакции

    next_choice_word = '''\nОтфильтровать список транзакций по определенному слову в описании? Да/Нет'''
    input_user_word = input(f"{next_choice_word}\n").lower()
    while input_user_word not in ["да", "нет"]:
        print(f"\nВвели некорректную фильтрацию\nПопробуйте еще раз:")
        input_user_word = input(f"{next_choice_word}\n").lower()
    else:
        if input_user_word == "да":
            word_filter = input("Введите слово для поиска:\n")

            if input_user_rub == "да":
                result_word = find_transactions(list(*result_rub), word_filter)  # функция фильтрует операции
                    # по слову word_filter в описании ["description"] -> list[dict]
            else:
                result_word = find_transactions(result_asceding, word_filter)  # функция фильтрует операции
                    # по слову word_filter в описании ["description"] -> list[dict]

    print("Распечатываю итоговый список транзакций...\n")
    print(f"Всего банковских операций в выборке: {len(result_word)}")



if __name__ == "__main__":
    print(main())
