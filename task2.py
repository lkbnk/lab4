def div100(x):
    try:
        y = 100 / int(x)
        print(y)
    except ValueError:
        print("Вы ввели буквы")
    except ZeroDivisionError:
        print("Попытка деления числа на ноль, введите число отличное от нуля")

div100(input('Введите число: '))
