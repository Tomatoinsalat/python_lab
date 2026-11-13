import random

def play_guess_game() -> None:
    secret_code = random.randint(0, 100)
    print(f"Загадано число от 0 до 100.")

    while True:
        user_input = input("Введите код: ").strip()

        user_input = input("Введите код: ").strip()

        if not user_input.isdigit():
            print("Ошибка: введите целое неотрицательное число.")
            continue

        attempt = int(user_input)

        if attempt < secret_code:
            print("Больше")
        elif attempt > secret_code:
            print("Меньше")
        else:
            print("Код подобран!")
            break


if __name__ == "__main__":
    play_guess_game()