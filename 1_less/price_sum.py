import csv
import sys

def calculate_totals(filename):
    adult_total = 0.0
    pensioner_total = 0.0
    child_total = 0.0
    
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                adult_total += float(row['Взрослый'])
                pensioner_total += float(row['Пенсионер'])
                child_total += float(row['Ребенок'])
    except FileNotFoundError:
        print(f"Ошибка: Файл {filename} не найден", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Ошибка при обработке файла: {str(e)}", file=sys.stderr)
        sys.exit(1)
    
    # Форматируем с двумя знаками после запятой
    return (f"{round(adult_total, 2):.2f}", 
            f"{round(pensioner_total, 2):.2f}", 
            f"{round(child_total, 2):.2f}")

if __name__ == "__main__":
    filename = sys.argv[1] if len(sys.argv) > 1 else 'products.csv'
    adult, pensioner, child = calculate_totals(filename)
    print(f"{adult} {pensioner} {child}")