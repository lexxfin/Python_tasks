# Вычислить число c заданной точностью d
# Пример: при d = 0.001, π = 3.142 10^(-1) ≤ d ≤10^(-10)

d, num = input('d = ').strip(), float(input('num = '))
print(f'{d = }, num = {round(num, len(d.split(".")[1]))}')
