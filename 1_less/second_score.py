# Считываем количество участников
n = int(input())
# Считываем список результатов
results = list(map(int, input().split()))
# Инициализируем переменные для хранения максимального и второго по величине значений
max_val = float('-inf')  # Начинаем с отрицательной бесконечности
second_max = float('-inf')
# Проходим по всем результатам один раз
for result in results:
    # Если текущий результат больше максимального
    if result > max_val:
        # Старое максимальное значение становится вторым максимумом
        second_max = max_val
        # Обновляем максимальное значение
        max_val = result
    # Если текущий результат меньше максимального, но больше второго максимума
    elif result > second_max and result != max_val:
        # Обновляем второе максимальное значение
        second_max = result
# Выводим второй максимум, если он существует
if second_max != float('-inf'):
    print(second_max)
else:
    print('')