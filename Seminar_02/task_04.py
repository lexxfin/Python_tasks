# 4 – Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt
# в одной строке одно число.
from random import randint

exists, prod, N = False, 1, int(input('N: '))
lst = [randint(-N, N) for _ in range(N)]
with open('file.txt', 'r') as file:
    for line in file:
        if -N <= int(line) < N:
            exists = True
            prod *= lst[int(line)]
print(prod if exists else 'Позиции вне списка')
