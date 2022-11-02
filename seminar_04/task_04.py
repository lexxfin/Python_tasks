# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# k=2 => 2x^2 + 4x + 5 = 0 или x^2 + 5 = 0 или 10x^2 = 0

from sympy import random_poly
from sympy.abc import x

k = int(input('k: '))
with open('task_04_poly.txt', 'w') as f:
    f.write(str(random_poly(x, k, -100, 100)).replace('**', '^').replace('*', '') + ' = 0')
