class Person:
    def __init__(self, name_pm: str, age_pm: int):
        self.name = name_pm
        self.age = age_pm

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Teacher(Person):
    def __init__(self, name_pm: str, age_pm:  int, subject_pm: str):
        super().__init__(name_pm, age_pm)
        self.subject = subject_pm

    def display_teacher_info(self):
        self.display_info()
        print(f"Subject: {self.subject}")

# Примеры использования классов

# Создаем объект Person
person = Person("Danislan!", 18)
person.display_info()

# Создаем объект Teacher
teacher = Teacher("Жедигер!", 17, "Mathematics")
teacher.display_teacher_info()
