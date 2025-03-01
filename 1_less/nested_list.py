# Получаем количество студентов
n = int(input())

# Создаем пустой список для записей
students = []

# Получаем данные от пользователя
for q in range(n):
    # Считываем имя
    name = input().strip()
    # Считываем оценку и преобразуем в float
    score = float(input())
    # Добавляем запись в список
    students.append([name, score])

# Получаем уникальные оценки и сортируем их по возрастанию
unique_scores = sorted(set(score for q, score in students))

# Если меньше двух разных оценок, выход
if len(unique_scores) < 2:
    exit()

# Берём вторую по величине оценку
second_highest = unique_scores[-2]

# Находим всех студентов с второй по величине оценкой
second_highest_students = [
    name for name, score in students 
    if score == second_highest
]

# Сортируем имена по алфавиту
sorted_names = sorted(second_highest_students)

# Выводим результат
for name in sorted_names:
    print(name)