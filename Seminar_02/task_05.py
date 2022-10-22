# 5 – Реализуйте алгоритм перемешивания списка.
from random import shuffle, randint

lst = [randint(0, 55) for _ in range(5)]
print(lst, end='')
shuffle(lst)
print(f' -> shuffled {lst}')