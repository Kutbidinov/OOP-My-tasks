class Country:
    def __init__(self, population_pm, Climat_pm, Locationcountry_pm, Themonetarycurrencyoftheod_pm, Language_pm):
        self.populataion = population_pm
        self.Climat = Climat_pm
        self.Locationcountry = Locationcountry_pm
        self.Themonetarycurrencyoftheod = Themonetarycurrencyoftheod_pm
        self.Language = Language_pm


Kyrgyzstan = Country(population_pm="Kyrgyzstan - Population = 7 000_000", Climat_pm="continental",
                     Locationcountry_pm="Central Asia",
                     Themonetarycurrencyoftheod_pm="SOM",
                     Language_pm="National Kyrgyz language")

Country1 = Kyrgyzstan.populataion
print(Country1)


Russia = Country(population_pm="Russia - Population = 146_203_613",
                 Climat_pm="Муссонный климат",
                 Locationcountry_pm="Россия Находиться в Юго Восточной Азии",
                 Themonetarycurrencyoftheod_pm="Российский Рубль, Государственная Валюта",
                 Language_pm='"Русский Язык" Официально Является языком "Российской Федерации"')

Country2 = Russia.populataion
print(Country2)



China = Country(population_pm="China - Population = 2_334_344_323_322", Climat_pm="climate is continental with cold, dry winters and hot, humid summers.",
                Locationcountry_pm="China is Located in 'East Asia.'",
                Themonetarycurrencyoftheod_pm="Oficial Valute in China,this 'Юань'",
                Language_pm="Language in China 'Language China!")

Country3 = China.populataion
print(Country3)