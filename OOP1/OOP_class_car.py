class Car:
    def __init__(self, color_pm, speed_pm, model_pm, value_pm, horsepower_pm):
        self.color = color_pm
        self.speed = speed_pm
        self.model = model_pm
        self.value = value_pm
        self.horsepower = horsepower_pm



millavantgarde = Car(color_pm="Gray", speed_pm=360, model_pm="millavantgarde", value_pm="3.2", horsepower_pm=444)
Mers = Car(color_pm="black", speed_pm=240, model_pm=124, value_pm=2.2, horsepower_pm=300)
Lexus = Car(color_pm="white", speed_pm=360, model_pm="Lexus Lx", value_pm=5.7, horsepower_pm=555)
Bmw = Car(color_pm="blue", speed_pm=240, model_pm="M.5", value_pm=4.5, horsepower_pm=555)
Audi = Car(color_pm="Gray", speed_pm=240, model_pm="Audi 100 electric farsunka", value_pm=2.0, horsepower_pm=300)
Lomborgini = Car(color_pm="Red", speed_pm=1200, model_pm="Lomborgini Urus", value_pm=5.5, horsepower_pm=880)
Seven07 = Car(color_pm="Blue", speed_pm=180, model_pm=0.7, value_pm=1.6, horsepower_pm=200)

print(" The start of the Millennium Avant-Garde class!")

print(millavantgarde.color) # Gray
print(millavantgarde.speed) # 360
print(millavantgarde.model) # mill
print(millavantgarde.value) # 3.2
print(millavantgarde.horsepower) # 444

print("Moving to the next 'Class' Mercedes!")

print(Mers.color) # black
print(Mers.speed) # 240
print(Mers.model) # 124
print(Mers.value) # 2.2
print(Mers.horsepower) # 300

print("Luxury and quality are an environmental responsibility!")

print(Lexus.color) # white
print(Lexus.speed) # 360
print(Lexus.model) # Lexus Lx
print(Lexus.value) # 5.7
print(Lexus.horsepower) # 555


print("Чувство свободы - Только с BMW!!")

print(Bmw.color) # blue
print(Bmw.speed) # 240
print(Bmw.model) # M.5
print(Bmw.value) # 4.5
print(Bmw.horsepower) # 555

print("The well-known Audi Brand!")

print(Audi.color) # Gray
print(Audi.speed) # 240
print(Audi.model) # Audi 100 electric farsunka
print(Audi.value) # 2.0
print(Audi.horsepower) # 300

print("Uniqueness and limited availability - Status and prestige!")

print(Lomborgini.color) # Red
print(Lomborgini.speed) # 350
print(Lomborgini.model) # Lomborginni Urus
print(Lomborgini.value) # 5.5
print(Lomborgini.horsepower) # 8.8

print("Those who do not have the means to tune classics, buy a foreign car( ' 0.7' ")

print(Seven07.color) # Blue
print(Seven07.speed) # 180
print(Seven07.model) # 0.7
print(Seven07.value) # 1.6
print(Seven07.horsepower) # 200

Millennium_distance = 5000
time_hour = Millennium_distance / millavantgarde.speed
print(time_hour)

Mers_distance = 5000
time_hour = Mers_distance / Mers.speed
print(time_hour)

Lexus_distance = 5000
time_hour = Lexus_distance / Lexus.speed
print(time_hour)


Bmw_distance = 5000
time_hour = Bmw_distance / Bmw.speed
print(time_hour)


Audi_distnace = 5000
time_hour = Audi_distnace / Audi.speed
print(time_hour)


Lomborgini_distance = 10000
time_hour = Lomborgini_distance / Lomborgini.speed
print(time_hour)

Seven07_distance = 2000
time_hour = Seven07_distance / Seven07.speed
print(time_hour)


