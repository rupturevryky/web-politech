def process_commands():
    # Инициализация пустого списка
    arr = []

    # Чтение количества команд
    n = int(input())

    # Обработка каждой команды
    for _ in range(n):
        # Чтение команды и её аргументов
        command_parts = input().split()

        # Извлечение команды и преобразование числовых аргументов в int
        command = command_parts[0]
        args = [int(x) for x in command_parts[1:] if len(command_parts) > 1]

        # Обработка команды insert
        if command == "insert":
            arr.insert(args[0], args[1])

        # Обработка команды print
        elif command == "print":
            print(arr)

        # Обработка команды remove
        elif command == "remove":
            arr.remove(args[0])

        # Обработка команды append
        elif command == "append":
            arr.append(args[0])

        # Обработка команды sort
        elif command == "sort":
            arr.sort()

        # Обработка команды pop
        elif command == "pop":
            arr.pop()

        # Обработка команды reverse
        elif command == "reverse":
            arr.reverse()


# Запуск обработки команд
process_commands()