import subprocess
import pytest
import os
import csv

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
    ],
    'metro': [
        (["1", "10 20", "15"], "1"),
        (["2", "10 20", "20 30", "20"], "2"),
        (["2", "10 20", "30 40", "25"], "0"),
        (["5", "1 10", "2 9", "3 8", "4 7", "5 6", "5"], "5"),
        (["3", "10 20", "15 25", "5 15", "15"], "3"),
        ([], "0"),
        (["2", "10 20"], "0"),
        (["abc", "10 20", "15"], "0"),
        (["1", "10 abc", "15"], "0")
    ],
    'minion_game': [
        (['BANANA'],['Stuart 12']),
        (['AAAA'],['Kevin 10']),
        (['B'],['Stuart 1']),
        (['A'],['Kevin 1']),
    ],
    'is_leap': [
        (['2000'],['True']),
        (['1900'],['False']),
        (['1899'],['Error!']),
        (['100001'],['Error!']),
    ],
    'happiness': [
        (['3 2','1 2 3','1 2','3 4'],['1']),
        (['3 1','1 1 1','1','2'],['3']),
        (['3','1 2 3','',''],['']),
    ],
    'pirate_ship': [
        (['50 3','Gold 10 60','Silver 20 100','Copper 30 120'],['Gold 10 60.00','Silver 20 100.00','Copper 20.00 80.00']),
    ],
    'matrix_mult': [
        (['2','1 2','3 4','5 6','7 8'],['19 22','43 50']),
        (['2','0 0','0 0','1 1','1 1'],['0 0','0 0']),
        (['2','-1 2','3 -4','5 -6','-7 8'],['-19 22','43 -50']),
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

def run_price_sum_script(input_file=None):
    """Запускает price_sum.py с указанным файлом"""
    cmd = [INTERPRETER, 'price_sum.py']
    if input_file:
        cmd.append(input_file)
    
    result = subprocess.run(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        encoding='utf-8'
    )
    return result.stdout.strip()

def create_test_file(content, filename='test_products.csv'):
    """Создает временный CSV файл"""
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    return filename

def remove_test_file(filename):
    """Удаляет временный файл"""
    if os.path.exists(filename):
        os.remove(filename)

def test_with_test_data():
    """Тест с временными данными"""
    test_content = """Продукт,Взрослый,Пенсионер,Ребенок
яблоки,100.50,200.25,300.75
хлеб,50.25,75.50,100.75"""
    
    test_file = create_test_file(test_content)
    try:
        output = run_price_sum_script(test_file)
        # Разбиваем вывод на числа и проверяем каждое
        nums = output.split()
        assert len(nums) == 3
        assert float(nums[0]) == pytest.approx(150.75)
        assert float(nums[1]) == pytest.approx(275.75)
        assert float(nums[2]) == pytest.approx(401.50)
    finally:
        remove_test_file(test_file)

def test_with_rounding():
    """Тест с округлением"""
    test_content = """Продукт,Взрослый,Пенсионер,Ребенок
товар1,10.555,20.555,30.555
товар2,15.555,25.555,35.555"""
    
    test_file = create_test_file(test_content)
    try:
        output = run_price_sum_script(test_file)
        nums = output.split()
        assert len(nums) == 3
        assert float(nums[0]) == pytest.approx(26.11, abs=0.01)
        assert float(nums[1]) == pytest.approx(46.11, abs=0.01)
        assert float(nums[2]) == pytest.approx(66.11, abs=0.01)
    finally:
        remove_test_file(test_file)

def test_with_original_file():
    """Тест с оригинальным файлом"""
    if not os.path.exists('products.csv'):
        pytest.skip("Файл products.csv не найден")
    
    # Рассчитаем ожидаемый результат
    adult = pensioner = child = 0.0
    with open('products.csv', 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            adult += float(row['Взрослый'])
            pensioner += float(row['Пенсионер'])
            child += float(row['Ребенок'])
    
    # Запустим скрипт без аргументов
    output = run_price_sum_script()
    nums = output.split()
    assert len(nums) == 3
    assert float(nums[0]) == pytest.approx(round(adult, 2), abs=0.01)
    assert float(nums[1]) == pytest.approx(round(pensioner, 2), abs=0.01)
    assert float(nums[2]) == pytest.approx(round(child, 2), abs=0.01)

def test_with_missing_file():
    """Тест с отсутствующим файлом"""
    result = subprocess.run(
        [INTERPRETER, 'price_sum.py', 'nonexistent.csv'],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        encoding='utf-8'
    )
    assert result.returncode != 0
    assert "не найден" in result.stderr or "No such file" in result.stderr or "FileNotFoundError" in result.stderr

@pytest.mark.parametrize("input_data, expected", test_data['metro'])
def test_metro(input_data, expected):
    result = run_script('metro.py', input_data)
    assert result == expected

@pytest.mark.parametrize("input_data, expected", test_data['minion_game'])
def test_minion_game(input_data, expected):
    assert run_script('minion_game.py', input_data).split('\n') == expected

@pytest.mark.parametrize("input_data, expected", test_data['is_leap'])
def test_is_leap(input_data, expected):
    assert run_script('is_leap.py', input_data).split('\n') == expected

@pytest.mark.parametrize("input_data, expected", test_data['happiness'])
def test_happiness(input_data, expected):
    assert run_script('happiness.py', input_data).split('\n') == expected

@pytest.mark.parametrize("input_data, expected", test_data['pirate_ship'])
def test_pirate_ship(input_data, expected):
    assert run_script('pirate_ship.py', input_data).split('\n') == expected

@pytest.mark.parametrize("input_data, expected", test_data['matrix_mult'])
def test_matrix_mult(input_data, expected):
    assert run_script('matrix_mult.py', input_data).split('\n') == expected