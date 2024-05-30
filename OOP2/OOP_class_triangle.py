import math


class Triangle:
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def perimeter(self):
        return self.side1 + self.side2 + self.side3

    def area(self):
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))


# Пример использования
triangle = Triangle(3, 4, 5)
print(f"Периметр треугольника: {triangle.perimeter()}")  # Output: 12
print(f"Площадь треугольника: {triangle.area()}")  # Output: 6.0
