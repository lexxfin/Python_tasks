# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

# Первый вариант через factorint
from sympy import factorint

n = int(input('N: '))
print(f'{n} = {" * ".join(map(str, factorint(n, multiple=True)))}')

# Второй вариант через функцию генератор
# def factors(num, d=2):
#     while num > 1:
#         n1, n2 = divmod(num, d)
#         if n2:
#             d += 1
#         else:
#             yield d
#             num = n1
#
#
# n = int(input("N: "))
# print(f'{n} = {" * ".join(map(str, factors(n)))}')
