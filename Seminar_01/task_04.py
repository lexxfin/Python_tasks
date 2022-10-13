# Напишите программу, которая по заданному номеру четверти, показывает диапазон
# возможных координат точек в этой четверти (x и y).
quarter = input('Введите номер четверти: ').strip()
match quarter:
	case '1':
		print(f'В {quarter} четверти x>0 и y>0')
	case '2':
		print(f'В {quarter} четверти x<0 и y>0')
	case '3':
		print(f'В {quarter} четверти x<0 и y<0')
	case '4':
		print(f'В {quarter} четверти x>0 и y<0')
	case _:
		print('Не верный ввод')
