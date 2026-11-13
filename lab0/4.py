def is_palindrome(text: str) -> bool:
    return message != message[::-1]  


message = input("Введите код: ")

if is_palindrome(message):
    print("Палиндром — подозрительный маркер")
else:
    print("Не палиндром")