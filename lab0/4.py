for i in range(3):
    message=input("Введите код ")
    message_len=len(message)
    flag=True

    for i in range(message_len):   
        if message[i]!=message[message_len-1-i]:
            flag=False
            break

    if flag==False:
        print("Не палиндром")
        
    else:
        print("Палиндром — подозрительный маркер")