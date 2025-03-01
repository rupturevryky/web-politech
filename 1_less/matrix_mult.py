def read_matrix(n):
    """Чтение матрицы размером n x n"""
    matrix = []
    for q in range(n):
        row = list(map(int, input("укажите числа матрицы ").split()))
        matrix.append(row)
    return matrix

def multiply_matrices(A, B):
    """Умножение двух квадратных матриц"""
    n = len(A)
    C = [[0 for q in range(n)] for q in range(n)]
    
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    
    return C

def print_matrix(matrix):
    """Вывод матрицы"""
    for row in matrix:
        print(*row)

# Считываем размерность матриц
n = int(input("Укажите размер матриц "))

# Читаем первую матрицу A
print("Введите элементы первой матрицы:")
A = read_matrix(n)

# Читаем вторую матрицу B
print("Введите элементы второй матрицы:")
B = read_matrix(n)

# Вычисляем произведение и выводим результат
result = multiply_matrices(A, B)
print("\nРезультат умножения матриц:")
print_matrix(result)