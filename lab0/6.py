ZODIAC_CUTOFF_DAYS = (19, 18, 20, 19, 20, 20, 22, 22, 22, 22, 21, 21)
ZODIAC_SIGNS = (
    "Козерог", "Водолей", "Рыбы", "Овен", "Телец", "Близнецы",
    "Рак", "Лев", "Дева", "Весы", "Скорпион", "Стрелец",
)
MONTH_MAX_DAYS = (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)


def get_zodiac_sign(day: int, month: int) -> str:
    if not (1 <= month <= 12):
        return ValueError("Месяц должен быть от 1 до 12")
        

    if not (1 <= day <= MONTH_MAX_DAYS[month - 1]):
        return ValueError(f"В {month}-м месяце не может быть {day} дн.")
        

    if day <= ZODIAC_CUTOFF_DAYS[month - 1]:
        return ZODIAC_SIGNS[month - 1]
    return ZODIAC_SIGNS[month % 12]


raw_date = input("Введите дату рождения (ДД.ММ): ").strip()
parts = raw_date.split(".")

if len(parts) == 2 and parts[0].isdigit() and parts[1].isdigit():
    birth_day, birth_month = int(parts[0]), int(parts[1])
    print(get_zodiac_sign(birth_day, birth_month))
else:
    print("Ошибка: введите дату в формате ДД.ММ (например, 15.04)")