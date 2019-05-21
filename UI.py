import SPT
import LocalFirst
import LocalSecond
import Util
import os

input_modes = ['Random', 'Manual']

def show_menu():
	mode = get_input_mode()

	if mode != 'Random':
		_list, m, n = handle_input(mode)
		SPT.SPT(_list = _list, m = m, n = n, verbose=True)
		LocalFirst.local_first(_list = _list, m = m, n = n, verbose=True)
		LocalSecond.local_second(_list = _list, m = m, n = n, verbose=True)
	else:
		_list, m, n = Util.generate_random_case()
		SPT.SPT(_list = _list, m = m, n = n, verbose=True)
		LocalFirst.local_first(_list = _list, m = m, n = n, verbose=True)
		LocalSecond.local_second(_list = _list, m = m, n = n, verbose=True)

def handle_input(mode):
	_list = []
	m = 0
	n = 0

	if mode=='Manual':
	
		is_read = False
		os.system("cls")
		while not is_read:
			in_list = input("Enter your list of works: ")
			in_list = in_list.split()
			try:
				for it in in_list:
					_list.append(int(it))
					if _list[-1] < 0:
						raise Exception()
				is_read = True
			except:
				read_list = False
				_list.clear()
				os.system("cls")
				print('Incorrect input')

		print("Your list: ", _list)

		while True:

			try:
				m = int(input('Enter number of machines(m): '))
				if m <= 0:
					raise Exception()
				break
			except:
				os.system('cls')
				print ('Input error')

		print("Your m: ", m)

		n = len(_list)



	return _list, m, n

def get_input_mode():

	mode = 0

	try:
		while True:
			mode = input('Select the mode.\n1. Random\n2. Manual\nYour choise: ')
			if mode in ('1', '2'):
				break
			os.system('cls')
			print('Input is incorrect')
	except:
		print('Error!')
	print ('Selected mode: ', mode)
	return input_modes[int(mode)-1]



show_menu()

os.system("pause")
