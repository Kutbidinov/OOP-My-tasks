import math

class Triangle:
    def __init__(self, a_pm: int, b_pm: int, c_pm: int):
        self.a = a_pm
        self.b = b_pm
        self.c = c_pm

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

# Примеры использования класса

# Создаем объект Triangle
triangle = Triangle(3, 4, 5)

# Вычисляем периметр
perimeter = triangle.perimeter()
print(f"Perimeter: {perimeter}")

# Вычисляем площадь
area = triangle.area()
print(f"Area: {area}")
