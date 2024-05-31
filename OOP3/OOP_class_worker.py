class Worker:
    def __init__(self, name_pm: str, age_pm: int):
        self.name = name_pm
        self.age = age_pm

    def introduce(self):
        print(f"Меня Зовут {self.name}")

    def introduce1(self):
        print(f"My age{self.age}")





# Мое использования:
work1 = Worker("Danislan!", 17)
work1.introduce()
work1.introduce1()
