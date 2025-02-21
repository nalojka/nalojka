import random
print("*********** Генератор паролей ***********")
simbol = "+-/*!&$#?=@"
numbers = "1234567890"
word = "abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
simbols = ""
while True:
    print("что вы хотите добавить в пароль. цифры/буквы/символы/ничего")
    choice = input()

    if choice == "цифры":
        simbols += numbers
        print(choice, "добавлены")

    elif choice == "буквы":
        simbols += word
        print(choice, "добавлены")

    elif choice == "символы":
        simbols += simbol
        print(choice, "добавлены")

    elif choice == "ничего":
        break

while True:
    print("------------------------------")
    lenght = int(input("Длина пароля:"))

    password = ""

    for i in range(lenght):
        password += random.choice(simbols)
    print("Ваш пароль:",password)
    