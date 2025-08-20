from processing import filter_by_state, sort_by_date
from reading_fin_trans import reading_csv, reading_excel
from transaction_filters import process_bank_search, process_bank_operations
from utils import convector_json
from widget import get_date



base_data = {
    'hello_print': 'Привет! Добро пожаловать в программу работы с банковскими транзакциями.\n'
                   '\n'
                   'Выберите необходимый пункт меню:',
    'type_file': '\n'
                 '1. Получить информацию о транзакциях из JSON-файла\n'
                 '2. Получить информацию о транзакциях из CSV-файла\n'
                 '3. Получить информацию о транзакциях из XLSX-файла',

    'state_operacion': 'Введите статус, по которому необходимо выполнить фильтрацию.\n'
                       'Доступные для фильтровки статусы:'
                       ' EXECUTED,'
                       ' CANCELED,'
                       ' PENDING',

    'user_type_file': {1: 'JSON-файл\n',
                       2: 'CSV-файл\n',
                       3: 'XLSX-файл\n'},

    'filter_by_date': {   'readiness': 'Отсортировать операции по дате? Да/Нет',
                          'sort order': 'Отсортировать по возрастанию или по убыванию?'},

    'currency': 'Выводить только рублевые транзакции? Да/Нет',

    'word position' : { 'filter_word': 'Отфильтровать список транзакций по определенному слову в описании? Да/Нет',
                        'selected word' : 'Слово: '},

    'result': 'Распечатываю итоговый список транзакций...'}

q1 = {      'type_file': 3,                      # Выбор файла и формата
            'state_operacion': 'CANCELED',       # Фильтрация по статусу операции
            'readiness': True,                   #  Сортировка по дате (вкл\выкл)
            'sort order': False,                  # Сортировка по убыванию\возрастанию (если readiness True)
            'currency': True,                   # Фильтрация по валюте RUB по умолчанию (вкл\выкл)
            'filter_word': True,                 # Фильтрация по слову (вкл\выкл)
            'selected word': 'карт'              # Фильтрация по конкретному слову (если True = filters word)
}

q2 = {      1 : r'C:\PythonProgramm\PROJECT\homework\data\operations.json',
            2 : r'C:\PythonProgramm\PROJECT\homework\transactions.csv',
            3 : r'C:\PythonProgramm\PROJECT\homework\transactions_excel.xlsx',}



def true_answer(dict_key):
    while True:
        user_input = input('--> ').lower()
        answer = {}

        if dict_key in ("currency", "filter_word", "readiness"):
            if user_input == "да" or user_input == "нет":
                answer[dict_key] = (user_input == "да")
                return answer
            else:
                print("Пожалуйста, введите 'да' или 'нет'")

        elif dict_key == "type_file":
            if user_input in ["1", "2", "3"]:
                answer[dict_key] = int(user_input)
                return answer
            else:
                print("Пожалуйста, введите 1, 2 или 3")

        elif dict_key == "sort order":
            if user_input == "по возрастанию":
                answer[dict_key] = True
                return answer
            elif user_input == "по убыванию":
                answer[dict_key] = False
                return answer
            else:
                print("Пожалуйста, введите 'по возрастанию' или 'по убыванию'")

        elif dict_key == "state_operacion":
            if user_input in ["executed", "canceled", "pending"]:
                answer[dict_key] = user_input.upper()
                print(f'Операции отфильтрованы по статусу: {answer[dict_key]}')
                return answer
            else:
                print('Пожалуйста, введите один из предложенных вариантов')

        elif dict_key == 'selected word':
            words_search = ('открытие', 'перевод', 'карт', 'счет')
            if user_input in words_search:
                answer[dict_key] = user_input
                return answer
            else:
                print('Доступные слова:', words_search)


def choice_of_question(questions):
    answer = {}
    print(questions["hello_print"])

    for key, value in questions.items():

        if key == "filter_by_date" or key == 'word position':
            for k, v in value.items():
                print(v)
                answer.update(true_answer(k))

                if k == 'readiness' and not answer.get('readiness'):
                    break
                if k == 'filter_word' and not answer.get('filter_word'):
                    break
                continue


        if key in ("hello_print", "user_type_file", "filter_by_date", "result", 'word position'):
            continue

        print(value)
        answer.update(true_answer(key))

        if key == 'type_file':
            print(f"Для обработки выбран {questions['user_type_file'][answer['type_file']]}")

    print(questions["result"])
    return answer


def output_formatting(data_base):

    score = process_bank_operations(data_base)
    finally_result = []

    if int(score['score']) > 0:
        for data_dict in data_base:
            if data_dict.get("to") is None or data_dict.get("from") is None:

                finally_result.append(
                    f"\n{get_date(data_dict['date'])} {data_dict['description']}\n"
                    f"{data_dict.get('from') + ' ' if data_dict.get('from') else ''}"
                    f"{data_dict.get('to')}\n"
                    f"Сумма {data_dict['operationAmount'].get('amount')} "
                    f"{data_dict['operationAmount']['currency']['name']}\n"
                )
            else:
                finally_result.append(
                    f"\n{get_date(data_dict['date'])} {data_dict['description']}\n"
                    f"{data_dict.get('from')} -> {data_dict.get('to')}\n"
                    f"Сумма {data_dict['operationAmount'].get('amount')} "
                    f"{data_dict['operationAmount']['currency']['name']}\n"
                )
        print(f'\nВсего банковских операций в выборке: {score['score']}')
        return finally_result

    else:
        return 'Не найдено ни одной транзакции, подходящей под ваши условия фильтрации'


def search_result_from_type_file(parameters, file):

    state_filter = filter_by_state(file, parameters['state_operacion'])
    date_filter = sort_by_date(state_filter, parameters.get('sort order'))

    result = date_filter

    if parameters['filter_word'] and parameters.get('selected word'):
        result = process_bank_search(result, parameters['selected word'])

    if parameters['currency']:
        result = process_bank_search(result, 'RUB')

    return output_formatting(result)


def single_format(parameters, file):

    type_read_file = {  1: convector_json,
                        2: reading_csv,
                        3: reading_excel}

    reader_function = type_read_file[parameters['type_file']]

    reading = reader_function(file[parameters['type_file']])
    transformed = []

    if parameters['type_file'] in [3, 2]:

        for transform in reading:

            new_dict = {
                'id' : transform.get('id'),
                'state' : transform.get('state'),
                'date' : transform.get('date'),
                'operationAmount' : {'amount' : transform.get('amount'),
                                     'currency' :  {'name': transform.get('currency_name'),
                                                    'code': transform.get('currency_code')}},
                'description' : transform.get('description'),
                'from' : transform.get('from'),
                'to' : transform.get('to')
            }

            if new_dict['from'] is None:
                del new_dict['from']
            if new_dict['to'] is None:
                del new_dict['to']

            transformed.append(new_dict)

        return search_result_from_type_file(parameters, transformed)
    else:
        return search_result_from_type_file(parameters, reading)


if __name__ == '__main__':

    func_2 = single_format(q1, q2)
    print(''.join(func_2))

