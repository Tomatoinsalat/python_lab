import random

code=random.randint(0,100)

while True:

    attempt=int(input("Введите код "))

    if attempt<code:
        print("Больше")

    elif attempt>code:
        print("Меньше")

    else:
        print("Код подобран!")
        break
