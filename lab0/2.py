def check_password(password: str) -> str:
    if len(password) < 16:
        return "Слишком короткий"
    if password.isdigit() or password.isalpha():
        return "Слабый пароль"
    return "Надежный пароль"


user_password = input("Введите пароль: ")
print(check_password(user_password))