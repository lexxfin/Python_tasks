# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся
# элементов исходной последовательности.

lst = [3, 1, 3, 5, 2, 6, 2, 9, 5]  # 1, 6, 9
print(lst, '->', [i for i in set(lst) if lst.count(i) == 1])