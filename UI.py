import SPT
import LocalFirst
import LocalSecond
import Util
import os
import json

strings = json.load(open('strings.json'))

def show_menu():
	
	mode = get_input_mode()

	os.system('cls')

	if mode != strings['input_modes'][0][1]:
		call_functions(handle_input(mode))
	else:
		call_functions(Util.generate_random_case())

def handle_input(mode):
	_list = []
	m = 0
	n = 0

	if mode==strings['input_modes'][1][1]:
	
		is_read = False
		os.system("cls")
		while not is_read:
			in_list = input(strings['iworklist'])
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
				print(strings['input_err'])

		print(strings['fenteredlist'], _list)

		while True:

			try:
				m = int(input(strings['imachines']))
				if m <= 0:
					raise Exception()
				break
			except:
				os.system('cls')
				print (strings['input_err'])

		print(strings['sm'], m)

		n = len(_list)



	return _list, m, n

def get_input_mode():

	mode = 0

	while True:
		try:		
			print(strings['mode_select'])

			for item in strings['input_modes']:
				print('{}. {}'.format(item[0], item[1]))

			mode = strings['input_modes'][int(input())-1][1].strip()
			
			break

		except:
			os.system('cls')
			print(strings['input_err'])

		
	
	print (strings['msel'], mode)
	
	return mode

def print_matrix(matrix, name):
	
	print(strings['omatrix'].format(name))
	
	for i in range(len(matrix)):
		print(strings['fmatrix'].format(i+1, matrix[i]))

def call_functions(ivals):
	_list, m, n = ivals

	print(strings['finitial'], _list)

	print_matrix(SPT.SPT(_list = _list, m = m, n = n), strings['SPT'])
	print_matrix(LocalFirst.local_first(_list = _list, m = m, n = n), strings['lfirst'])
	print_matrix(LocalSecond.local_second(_list = _list, m = m, n = n), strings['lsecond'])

show_menu()

os.system("pause")
