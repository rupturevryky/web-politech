from string import punctuation

def clean_word(word):
    """Очищает слово от знаков препинания"""
    while word and word[-1] in punctuation:
        word = word[:-1]
    while word and word[0] in punctuation:
        word = word[1:]
    return word

def find_longest_words(filename):
    """Находит все слова максимальной длины в файле"""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()
            
        # Разбиваем текст на слова и очищаем их
        words = [clean_word(word) for word in text.split()]
        
        # Находим максимальную длину слова
        max_length = max(len(word) for word in words)
        
        # Сохраняем позиции всех слов максимальной длины
        longest_words_positions = []
        for i, word in enumerate(words):
            if len(word) == max_length:
                longest_words_positions.append((i, word))
        
        # Возвращаем слова в порядке их появления
        return [word for _, word in longest_words_positions]
        
    except FileNotFoundError:
        print(f"Ошибка: Файл {filename} не найден.")
        return []

# Использование функции
filename = 'example.txt'
result = find_longest_words(filename)

# Вывод результатов
for word in result:
    print(word)