'''
4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
многочлена и записать в файл многочлен степени k.
Пример:
k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
'''
import random

def write_file(st):
    with open('file_task4.txt', 'w') as data:
        data.write(st)

def rnd():
    return random.randint(0,101)

def create_mn(k):
    lst = [rnd() for i in range(k+1)]
    return lst

def create_polynom(sp):
    lst= sp[::-1]
    pn = ''
    if len(lst) < 1:
        pn = 'x = 0'
    else:
        for i in range(len(lst)):
            if i != len(lst) - 1 and lst[i] != 0 and i != len(lst) - 2:
                pn += f'{lst[i]}x^{len(lst)-i-1}'
                if lst[i+1] != 0:
                    pn += ' + '
            elif i == len(lst) - 2 and lst[i] != 0:
                pn += f'{lst[i]}x'
                if lst[i+1] != 0:
                    pn += ' + '
            elif i == len(lst) - 1 and lst[i] != 0:
                pn += f'{lst[i]} = 0'
            elif i == len(lst) - 1 and lst[i] == 0:
                pn += ' = 0'
    return pn

k = int(input("Введите натуральную степень k: "))
coeff = create_mn(k)
write_file(create_polynom(coeff))