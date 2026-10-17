name=input("Введите имя").lower()

name_splited=name.split()

print(name_splited[0][0].upper()+name_splited[0][1:],name_splited[1][:1].upper()+"."+name_splited[2][:1].upper()+".")
