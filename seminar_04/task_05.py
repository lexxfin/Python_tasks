# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

from sympy import sympify

with open('task_05_poly_1.txt', 'r') as f1, \
        open('task_05_poly_2.txt', 'r') as f2, \
        open('task_05_poly_3.txt', 'w') as f3:
    p1 = sympify(f1.read().removesuffix('= 0').replace('^', '**').replace('x', '*x'))
    p2 = sympify(f2.read().removesuffix('= 0').replace('^', '**').replace('x', '*x'))
    f3.write(str(p1 + p2).replace('**', '^').replace('*', '') + ' = 0')
