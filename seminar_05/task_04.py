# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

from itertools import groupby

'''Через строки'''
# def code(data):
#     result = ''
#     tmp = data
#     while tmp:
#         result += str(len(tmp) - len(tmp.lstrip(tmp[0]))) + tmp[0]
#         tmp = tmp.lstrip(tmp[0])
#     return result

'''Через генератор с использованием itertools.groupby'''


def code(data):
    return ''.join(f'{sum(1 for _ in y)}{x}' for x, y in groupby(data))


def decode(data):
    result = ''
    tmp = data
    while tmp:
        result += tmp[1] * int(tmp[0])
        tmp = tmp[2::]
    return result


txt = 'aaaaa555bbbbbbccd'
print(f'{txt} -> {code(txt)}')
print(f'{code(txt)} -> {decode(code(txt))}')
