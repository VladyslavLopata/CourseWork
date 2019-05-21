import SPT
import LocalFirst
import LocalSecond
import os
input_modes = ['Random', 'Manual']

def _show_menu():


	select_input_type()
	
	'''print('Course Work v0.1a.\nPlease, select the option:\n1. SPT\n2. Local Search 1\n3. Local search 2')

	try:
		response = input()
		response = int(response) 
		if response == 1:
			SPT.SPT(verbose=True)
		elif response == 2:
			LocalFirst.local_first(verbose=True)
		elif response == 3:
			LocalSecond.local_second(verbose=True)
		else:
			show_menu()

	except:
		print('Input is incorrect')
		show_menu()'''

#==================================================================#
#                                                                  #
#==================================================================#
def select_input_type():
	choises = ['How would you like to enter your values?',
			   '1. Random', 
			   '2. Manual']
	selected = try_menu(choises)

	if selected != 0:
		select_algorithm(input_type_list[selected-1])
	else:
		select_input_type()

def select_algorithm(input_type):

	choises = ['Course Work v0.1.\nPlease, select the option:',
				'1. SPT',
				'2. Local Search 1',
				'3. Local search 2']

	selected = try_menu(choises)
	_list = get_list(input_type)

	m = 0
	while m <= 0:
		try:
			m = int(input('Enter m: '))
		except:
			print('incorrect input')


	if selected == 1:
		SPT.SPT(_list = _list, n=len(_list), verbose=True, m = m)
	elif selected == 2:
		LocalFirst.local_first(_list = _list, n=len(_list), verbose=True, m = m)
	elif selected == 3:
		LocalSecond.local_second(_list = _list, n=len(_list), verbose=True, m = m)

#==================================================================#
#                                                                  #
#==================================================================#
def try_menu(choises):
	
	for i in range(len(choises)):
		print(choises[i])

	try:
		response = int(input())
		if response > len(choises) or response <=0:
			return 0
		return response

	except:
		print('Input is incorrect')
		return 0

#==================================================================#
#                                                                  #
#==================================================================#
def get_list(input_type):
	if input_type == 'Random':
		return []
	else:
		try:
			_ls = input('Enter the list of works:')
			_ls = _ls.split()

			_list = []
			for item in _ls:
				_list.append(int(item))
			return _list

		except:
			return get_list(input_type)

def show_menu():
	mode = get_input_mode()

	if mode != 'Random':
		_list, m, n = handle_input(mode)
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