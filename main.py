"""
def task1(a):
    if a % 3 == 0:
        print('Число делится на 3')
    else:
        print('Число не делится на 3')
task1(int(input('Введите число: ')))
"""


def task2(a):
    if a == 0:
        print('Введите число отличное от нуля')
    elif (type(a)==str):
        print('Введите число, не строку')

task2(int(input('Введите число: ')))

