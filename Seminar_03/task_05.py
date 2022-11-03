# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
from math import sqrt


def fib(n):
    sqrt5 = sqrt(5)
    phi = (sqrt5 + 1) / 2
    result = int(phi ** abs(n) / sqrt5 + 0.5)
    return result if n >= 0 else (-1) ** (-n + 1) * result


k = int(input('k: '))
print(f'{k=} -> {[fib(i) for i in range(-k, k + 1)]}')
