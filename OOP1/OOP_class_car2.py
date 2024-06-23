class Car:
    def __init__(self, mark_pm: str, model_pm: int, year_pm: int,  price_pm: int):
        self.mark = mark_pm
        self.model = model_pm
        self.year = year_pm
        self.price = price_pm

# Создаем три объекта класса Car
car1 = Car("Toyota", "Camry", 2020, 24000)
car2 = Car("Honda", "Accord", 2019, 22000)
car3 = Car("Ford", "Mustang", 2021, 35000)

# Вычисляем общую сумму стоимости автомобилей
total_price = car1.price + car2.price + car3.price

# Выводим результат
print(f"Общая стоимость автомобилей: ${total_price}")


