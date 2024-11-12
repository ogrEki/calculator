print("Привіт, це простий калькулятор")


def get_num(prompt):
    while True:
        try:
            return float(input(prompt))  # Перетворюємо введене значення на число (тип float)
        except ValueError:
            print("Помилка: Введено некоректне число. Спробуйте ще раз.")


NUM1 = get_num("Введіть перше число: ")
NUM2 = get_num("Введіть друге число: ")


Deystvie = input("Введіть дію, яку вам потрібна (+, -, *, /): ").strip()


if Deystvie == "+":
    result = NUM1 + NUM2
    print(f"Результат: {NUM1} + {NUM2} = {result}")
elif Deystvie == "-":
    result = NUM1 - NUM2
    print(f"Результат: {NUM1} - {NUM2} = {result}")
elif Deystvie == "*":
    result = NUM1 * NUM2
    print(f"Результат: {NUM1} * {NUM2} = {result}")
elif Deystvie == "/":
    if NUM2 != 0:
        result = NUM1 / NUM2
        print(f"Результат: {NUM1} / {NUM2} = {result}")
    else:
        print("Помилка: Ділення на нуль!")
else:
    print("Помилка: Невідома операція!")
