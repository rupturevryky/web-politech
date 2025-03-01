def square(num): return num ** 2

def is_even(num): return num % 2 == 0

def factorial(num):
    if num < 0: raise ValueError("Факториал определен только для неотрицательных чисел.")

    result = 1
    for i in range(1, num + 1): result *= i
    return result

def greet(name): print(f"Привет, {name}")

def add_numbers(a,b): return a + b

def find_max(a,b,c): 
    if a >= b and a >= c: return a
    elif b >= a and b >= c: return b
    return c

def fibonacci(num):
    if num <= 0:
        raise ValueError("The position must be a positive integer.")
    elif num == 1: return 0
    elif num == 2: return 1
    
    a, b = 0, 1
    for _ in range(2, num):
        a, b = b, a + b
    return b

def is_prime(num):
    if num <= 1: return False
    if num == 2: return True 
    if num % 2 == 0: return False
    
    for i in range(3, int(num**0.5) + 1, 2): 
        if num % i == 0: return False
    return True

