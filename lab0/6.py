birth_date=input("Введите дату ").split(".")
zodiac_dates=(19,18,20,19,20,20,22,22,22,22,21,21)
zodiac=("Козерог", "Водолей", "Рыбы", "Овен", "Телец", "Близнецы", "Рак", "Лев", "Дева", "Весы", "Скорпион", "Стрелец")

day=int(birth_date[0])
month=int(birth_date[1])

if day<=zodiac_dates[month-1]:
    print(zodiac[month-1])

else:
    print(zodiac[month%12])

