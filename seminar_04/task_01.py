# Вычислить число c заданной точностью d
# Пример: при d = 0.001, π = 3.142 10^(-1) ≤ d ≤10^(-10)

from math import pi

d = input('d = ').strip()
print('d =', d, 'π =', round(pi, len(d.split(".")[1])))
