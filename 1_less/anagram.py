def are_anagrams(str1, str2):
    # Если длины строк разные, они не могут быть анаграммами
    if len(str1) != len(str2):
        return False
    
    # Создаем словарь для подсчета частоты символов в первой строке
    char_count = {}
    
    # Подсчитываем частоту символов в первой строке
    for char in str1:
        char_count[char] = char_count.get(char, 0) + 1
    
    # Вычитаем частоту символов второй строки
    for char in str2:
        if char not in char_count:
            return False
        char_count[char] -= 1
        if char_count[char] == 0:
            del char_count[char]
    
    # Если все счетчики стали нулями, строки являются анаграммами
    return len(char_count) == 0

# Получаем входные данные от пользователя
str1 = input("Введите первую строчку ")
str2 = input("Введите вторую строчку ")

# Проверяем и выводим результат
if are_anagrams(str1, str2):
    print("YES")
else:
    print("NO")