def count_passengers():
    import sys
    # Читаем все строки ввода
    lines = []
    for line in sys.stdin:
        line = line.strip()
        if line:  # Игнорируем пустые строки
            lines.append(line)
    
    if not lines:
        print(0)
        return
    
    try:
        n = int(lines[0])
        if len(lines) < n + 2:
            print(0)
            return
        
        passengers = []
        for i in range(1, n + 1):
            a, b = map(int, lines[i].split())
            passengers.append((a, b))
        
        t = int(lines[n + 1])
        
        count = 0
        for a, b in passengers:
            # Учитываем пассажиров, которые вошли до или в момент T
            # и ещё не вышли или выходят в момент T
            if a <= t and b >= t:
                count += 1
        print(count)
    except (ValueError, IndexError):
        print(0)

if __name__ == "__main__":
    count_passengers()