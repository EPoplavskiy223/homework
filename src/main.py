import pprint

from generators import filter_by_currency
from processing import filter_by_state, sort_by_date
from reading_fin_trans import reading_csv, reading_excel
from transaction_filters import process_bank_search
from utils import convector_json
from widget import get_date, mask_account_card

base_data = {
    "hello_print":  "Привет! Добро пожаловать в программу работы с банковскими транзакциями."
                    "\n\nВыберите необходимый пункт меню:",

    "type_file": "\n1. Получить информацию о транзакциях из JSON-файла"
                 "\n2. Получить информацию о транзакциях из CSV-файла"
                 "\n3. Получить информацию о транзакциях из XLSX-файла",

    "state_operacion":  "Введите статус, по которому необходимо выполнить фильтрацию."
                        "\nДоступные для фильтровки статусы: "
                        "EXECUTED, "
                        "CANCELED, "
                        "PENDING",

    "user_type_file": {1: "JSON-файл",
                       2: "CSV-файл",
                       3: "XLSX-файл"},

    "filter_by_date": {'readiness' : "Отсортировать операции по дате? Да/Нет",
                       'sort order' : 'Отсортировать по возрастанию или по убыванию?'},


    "currency": 'Выводить только рублевые транзакции? Да/Нет',

    "filter_word": "Отфильтровать список транзакций по определенному слову в описании? Да/Нет",

    "result": "Распечатываю итоговый список транзакций...",
}


def choice_of_question(questions):

    answer = {}
    print(base_data["hello_print"])

    for key, value in questions.items():
        if key in {"hello_print", "user_type_file"}:
            continue
        if key == "result":
            print(f'{value}\n')
            break

        while True:
            print(value)

            user_input = input().lower()

            if key in "type_file":
                if user_input in "123":
                    answer[key] = int(user_input)
                    print(f"Для обработки выбран: {questions['user_type_file'][int(user_input)]}")
                    break

            elif key == "state_operacion":
                if user_input in {"executed", "canceled", "pending"}:
                    answer[key] = user_input.upper()
                    break

            else:
                if user_input == "да":
                    answer[key] = True
                    break
                elif user_input == "нет":
                    answer[key] = False
                    break
    return answer


def search_result_from_type_file(parameters, file):
    read = {
        1 : convector_json,
        2 : reading_csv,
        3 : reading_excel
    }

    result_filter = []
    result_format = []

    processor = read[parameters['type_file']]

    if processor:
        read_file = processor(file)

    # if parameters["type_file"] == read:
    #
    #     result_filter.append(
    #         sort_by_date(
    #             filter_by_state(
    #                 convector_json(file),
    #                 parameters["state_operacion"]),
    #             parameters["sorted_by_date"]
    #         )
    #     )

    for result_list in result_filter:
        for result_dict in result_list:

            result_dict["date"] = get_date(result_dict["date"])

            result_dict["to"] = mask_account_card(result_dict["to"])

            if result_dict.get("from"):
                result_dict["from"] = mask_account_card(result_dict["from"])

            result_dict.pop("id")
            result_dict.pop("state")

            result_format.append(result_dict)

    return result_format


def output_formatting(data_base):

    finally_result = []

    for data_dict in data_base:
        if data_dict.get("to") is None or data_dict.get("from") is None:

            finally_result.append(
                f"\n{data_dict['date']} {data_dict['description']}\n"
                f"{data_dict.get('from') + ' ' if data_dict.get('from') else ''}"
                f"{data_dict.get('to')}\n"
                f"Сумма {data_dict['operationAmount'].get('amount')} "
                f"{data_dict['operationAmount']['currency']['name']}\n"
            )
        else:
            finally_result.append(
                f"\n{data_dict['date']} {data_dict['description']}\n"
                f"{data_dict.get('from')} -> {data_dict.get('to')}\n"
                f"Сумма {data_dict['operationAmount'].get('amount')} "
                f"{data_dict['operationAmount']['currency']['name']}\n"
            )

    return finally_result

q = {
    "type_file": 1,
    "state_operacion": "CANCELED",
    "filter_by_date": True,
    "sorted_by_date": True,
    "currency": True,
    "filter_word": True,
}

q1 = [
    "08.12.2019 Открытие вклада "
    "Счет **4321"
    "Сумма: 40542 руб. "
    
    "12.11.2019 Перевод с карты на карту"
    "MasterCard 7771 27** **** 3727 -> Visa Platinum 1293 38** **** 9203"
    "Сумма: 130 USD"
    
    "18.07.2018 Перевод организации "
    "Visa Platinum 7492 65** **** 7202 -> Счет **0034"
    "Сумма: 8390 руб."
    
    "03.06.2018 Перевод со счета на счет"
    "Счет **2935 -> Счет **4321"
    "Сумма: 8200 EUR"
]


# elif parameters['type_file'] == 2:  #csv
#     reading_csv(file)
#
# elif parameters['type_file'] == 3:  #xlsx
#     reading_excel(file)
#     pass

# func3 = output_formatting(search_result_from_type_file(choice_of_question(base_data), "data/operations.json"))

print(''.join(output_formatting(search_result_from_type_file(choice_of_question(base_data), "transactions.csv"))))
