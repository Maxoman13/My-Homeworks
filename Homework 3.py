user_input = input("Введите слово: ")
if user_input == "":
    print("Нужно слово")
if user_input == user_input[::-1]:
    print(f"Обнаружен палиндром: {user_input.capitalize()}")
else:
    print(f"Слово {user_input.capitalize()} - это не палиндром")
