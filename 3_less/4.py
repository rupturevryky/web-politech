from abc import ABC, abstractmethod 
"""это шаблон для создания абстрактных классов и
инструмент для создания методов, которые обязательно
нужно реализовать в дочерних классах"""
import math

class Shape(ABC):
    """абстрактный класс, то есть его нельзя напрямую использовать"""
    @abstractmethod
    def area(self):
        pass 
    """пустой оператор, показывающий, что метод должен быть переопределён в дочерних классах
"""

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width

# Пример использования
circle = Circle(7)
rectangle = Rectangle(6, 10)

print(f"Площадь круга с радиусом {circle.radius}: {circle.area():.2f}")
print(f"Площадь прямоугольника {rectangle.length}x{rectangle.width}: {rectangle.area()}")

# пробуем создать объект базового класса Shape
try:
    shape = Shape()
except TypeError as e:
    print(f"\nОшибка при создании Shape: {e}")