import subprocess
import pytest
import os

INTERPRETER = 'python3'

def run_script(filename, input_data=None):
    proc = subprocess.run(
        [INTERPRETER, filename],
        input='\n'.join(input_data if input_data else []),
        capture_output=True,
        text=True,
        check=False
    )
    return proc.stdout.strip()

test_data = {
    'python_if_else': [
        ('1', 'Weird'),
        ('4', 'Not Weird'),
        ('3', 'Weird'),
        ('6','Weird'),
        ('22', 'Not Weird')
    ],
    'arithmetic_operators': [
        (['1', '2'], ['3', '-1', '2']),
        (['10', '5'], ['15', '5', '50'])
    ],
    'division': [
        (['10', '2'], ['5', '5.0']),  # Обычное деление
        (['10', '0'], ['Ошибка: деление на ноль!']),  # Деление на ноль
        (['15', '4'], ['3', '3.75'])  # Деление с остатком
    ],
    'loops': [  # Новые тестовые данные для циклов
        ('3', ['0', '1', '4']),  # Для n = 3
        ('5', ['0', '1', '4', '9', '16']),  # Для n = 5
        ('1', ['0']),  # Для n = 1
        ('0', [''])  # Для n = 0 (граничный случай)
    ],
    'print_function': [
        ('1', '1'),  # Граничный случай: n = 1
        ('3', '123'),  # Пример из логики
        ('5', '12345'),  # Пример из логики
        ('10', '12345678910'),  # Большее число
        ('0', '')  # Граничный случай: n = 0
    ],
    'second_score': [  # Тестовые данные для second_score.py
        (['5', '2 3 6 6 5'], '5'),  # Пример из логики
        (['4', '1 2 3 4'], '3'),  # Упорядоченный список
        (['4', '4 4 4 4'], ''),  # Все баллы одинаковые (нет второго места)
        (['2', '10 20'], '10'),  # Два участника
        (['1', '5'], ''),  # Один участник (нет второго места)
        (['6', '10 20 20 30 30 40'], '30'),  # Повторяющиеся баллы
        (['3', '-1 -2 -3'], '-2')  # Отрицательные баллы
    ],
    'nested_list': [  # Тестовые данные для nested_list.py
        (['5', 'Гарри', '37.21', 'Берри', '37.21', 'Тина', '37.2', 'Акрити', '41', 'Харш', '39'], 'Харш'),  # Пример из логики
        (['3', 'Алиса', '50.0', 'Боб', '50.0', 'Чарли', '60.0'], 'Алиса\nБоб'),  # Несколько студентов с одинаковой второй оценкой
        (['2', 'Давид', '30.0', 'Ева', '40.0'], 'Давид'),  # Два студента
        (['4', 'Фред', '20.0', 'Джордж', '20.0', 'Гарри', '30.0', 'Рон', '30.0'], 'Джордж\nФред'),  # Повторяющиеся оценки
        (['3', 'Альфа', '10.0', 'Бета', '20.0', 'Гамма', '20.0'], 'Альфа')  # Один студент с уникальной второй оценкой
    ],
    'list': [
        (['12', 'insert 0 5', 'insert 1 10', 'insert 0 6', 'print', 'remove 6', 'append 9', 'append 1', 'sort', 'print', 'pop', 'reverse', 'print'],
         '[6, 5, 10]\n[1, 5, 9, 10]\n[9, 5, 1]'),
        (['5', 'append 1', 'append 2', 'insert 1 3', 'print', 'pop'],
         '[1, 3, 2]'),
        (['3', 'append 10', 'append 20', 'print'],
         '[10, 20]'),
        (['4', 'append 5', 'append 5', 'remove 5', 'print'],
         '[5]'),
        (['6', 'append 1', 'append 2', 'append 3', 'reverse', 'print', 'sort'],
         '[3, 2, 1]')
    ],
    'swap_case': [
        ('Hello World!', 'hELLO wORLD!'),  # Пример из логики
        ('Python 3.9', 'pYTHON 3.9'),  # Строка с цифрами
        ('12345', '12345'),  # Строка без букв
        ('aBcDeF', 'AbCdEf'),  # Чередование регистров
        ('@#$%^', '@#$%^'),  # Строка с символами
        ('', '')  # Пустая строка
    ],
    'split_and_join': [
        ("Hello world", "Hello-world"),  # Пример из логики
        ("Python is fun", "Python-is-fun"),  # Несколько слов
        ("One", "One"),  # Одно слово
        ("", ""),  # Пустая строка
        ("   Multiple   spaces   ", "Multiple-spaces"),  # Множественные пробелы
        ("Special-characters @#$%^&*()", "Special-characters-@#$%^&*()"),  # Специальные символы
    ],
    'max_word': [
        ('', "сосредоточенности")
    ]
}

def test_hello_world():
    assert run_script('hello_world.py') == 'Hello, world!'

@pytest.mark.parametrize("input_data, expected", test_data['python_if_else'])
def test_python_if_else(input_data, expected):
    assert run_script('python_if_else.py', [input_data]) == expected

@pytest.mark.parametrize("input_data, expected", test_data['arithmetic_operators'])
def test_arithmetic_operators(input_data, expected):
    assert run_script('arithmetic_operators.py', input_data).split('\n') == expected

@pytest.mark.parametrize("input_data, expected", test_data['division'])
def test_division(input_data, expected):
    assert run_script('division.py', input_data).split('\n') == expected

@pytest.mark.parametrize("input_data, expected", test_data['loops'])
def test_loops(input_data, expected):
    assert run_script('loops.py', [input_data]).split('\n') == expected

@pytest.mark.parametrize("input_data, expected", test_data['print_function'])
def test_print_function(input_data, expected):
    assert run_script('print_function.py', [input_data]) == expected

@pytest.mark.parametrize("input_data, expected", test_data['second_score'])
def test_second_score(input_data, expected):
    assert run_script('second_score.py', input_data) == expected

@pytest.mark.parametrize("input_data, expected", test_data['nested_list'])
def test_nested_list(input_data, expected):
    assert run_script('nested_list.py', input_data) == expected

@pytest.mark.parametrize("input_data, expected", test_data['list'])
def test_lists(input_data, expected):
    assert run_script('list.py', input_data) == expected

@pytest.mark.parametrize("input_data, expected", test_data['swap_case'])
def test_swap_case(input_data, expected):
    assert run_script('swap_case.py', [input_data]) == expected

@pytest.mark.parametrize("input_data, expected", test_data['split_and_join'])
def test_split_and_join(input_data, expected):
    assert run_script('split_and_join.py', [input_data]) == expected

@pytest.mark.parametrize("input_data, expected", test_data['max_word'])
def test_max_word(input_data, expected):
    assert run_script('max_word.py', [input_data]) == expected