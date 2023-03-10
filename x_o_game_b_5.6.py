def greet():
	"""Функция приветсвия"""
	print("_______________________")
	print("Добро пожаловать в игру")
	print("	Крестики - нолики ")
	print("_______________________")
	print("Вводите координаты клетки")
	print("в виде xy без пробела")
	print("x - это номер строки")
	print("y - это номер столбца")
	print("Для корректной работы вводите")
	print("целые числа от 0 до 2")
	print("_______________________")
	print("Приятной игры!")
	print("_______________________")


def show(): 
	"""Функция создает игровое поле"""
	print(f'  0 1 2') #верхняя строка со столбцами 0 1 2
	for i in range(3):
		print(f'{i} {field[i][0]} {field[i][1]} {field[i][2]}')

def ask():
		"""Функция запрашивает координаты и проверяет их на принадлежность 
		к диапазону, и не занята ли клетка под этими координатами"""
		while True:
			x, y = map(int, input('Ваш ход: '))
			if 0 <= x <= 2 and 0 <= y <= 2:
				if field[x][y] == ' ':
					# list_x_y = []
					# list_x_y.append(x)
					# list_x_y.append(y)
					return x, y
				else:
					print('Клетка занята, введите координаты другой клетки от 0 до 2')
			else:
				print('Вы ввели координаты, находящиеся вне диапазона поля, введите от 0 до 2')

def check_win():
	"""Функция проверки выйгрышной комбинации"""
	win_comb = [((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), 
	((2, 0), (2, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)), 
	((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)), 
	((0, 0), (1, 1), (2, 2)), ((0, 2), (1, 1), (2, 0))]

	for comb in win_comb:
		 win_list = []

		 for c in comb:
		 	win_list.append(field[c[0]][c[1]])
		 if win_list == ["X", "X", "X"]:
		 	print('Выйграл крестик')
		 	return True
		 if win_list == ["O", "O", "O"]:
		 	print('Выйграл нолик')
		 	return True
	return False

def game():
		"""Функция присваивает Х или О ячейке по кооринатам """
		step_cout = 0
		while True:
			show() #запускает игровое поле 
			step_cout += 1
			if step_cout % 2 == 1:
				print('Ходит крестик')
			else:
				print('Ходит нолик')

			a = ask()
			x = a[0]# присваиваю x, y значения из списка по индексам
			y = a[1]

			if step_cout % 2 == 1:
				field[x][y] = 'X'
			else:
				field[x][y] = 'O'

			if check_win():
				break

			if step_cout == 9:
				print('Ничья')
				break

greet()
field = [[' ', ' ', ' '] for i in range(3)] 
game()
"""P.S. Писал код частично сам, частично подсматривал в вебинаре,
не понимал, как правильно выполнить проверку выйграшных комбинаций,
а так же сначала написал функцию, которая по полученным значениям запрашивает 
у игрока какой символ он хочет поместить в эту клетку, так как не понимал, как 
реализовать ходы двух разных игроков. Получалось коряво, но что-то получалось.
Ошибки знаю: нет проверки на isdigit, нет проверки на количество
введенных координат. Не исправлял эти ошибки потому что это был бы
полностью скопированный код из вебинара, а тут хотя бы частично написан
лично мною. Изначально был ступор как вообще это реализовывать.
Посмотрел как объясняет Егор логику написания что за чем и начинал пробовать
писать код сам. Когда не понимал как реализовать что-то обращлся к вебинару.
Но по крайней мере было понимание что бы игра работала надо все вложить в 
цкл while, что нужно создать базу выйграшных значений и сверять заполненные
клетки с ней и тд. Было тяжело, с тем учетом, что в принципе понял весь модуль,
кроме рекурсии, но хотя бы появилось понимание, как это вообще можно реализовать."""