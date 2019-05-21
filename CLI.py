import SPT
import LocalFirst
import LocalSecond
import Util
import os
import json

strings = json.load(open('strings.json'))
file = open('input.txt').readlines()

def show_menu():
	
	mode = get_input_mode()

	if mode != strings['input_modes'][0][1]:
		call_functions(handle_input(mode))
	else:
		call_functions(Util.generate_random_case())

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

def handle_input(mode):
	_list = []
	m = 0
	n = 0

	#functions corresponding to input methods
	fn = {strings['input_modes'][1][1]:[manual_list_input, manual_machines_input],
		  strings['input_modes'][2][1]:[list_from_file, machines_from_file]}

	fn[mode][0](_list)
	print(strings['fenteredlist'], _list)
	m = fn[mode][1]()
	print(strings['sm'], m)
	n = len(_list)

	return _list, m, n

def print_matrix(matrix, name):
	
	print('\n\n', strings['omatrix'].format(name))
	
	for i in range(len(matrix)):
		print(strings['fmatrix'].format(i+1, matrix[i]))

	print(strings['festimates'].format(Util.target_C_max(matrix), Util.target_C_macron(matrix)))

def call_functions(ivals):
	
	os.system("cls")

	_list, m, n = ivals

	print('{}\n{}'.format(strings['finitial'], _list))

	print_matrix(SPT.SPT(_list = _list, m = m, n = n), strings['SPT'])
	print_matrix(LocalFirst.local_first(_list = _list, m = m, n = n), strings['lfirst'])
	print_matrix(LocalSecond.local_second(_list = _list, m = m, n = n), strings['lsecond'])

def manual_list_input(_list):

	is_read = False
	
	os.system("cls")
	
	while not is_read:
		
		str_values = input(strings['iworklist']).strip()
		
		parse_string_to_list(str_values, _list)
			
		if not (len(_list) == 0):
			is_read = True
		else:
			os.system("cls")
			print(strings['input_err'])

def manual_machines_input():
	while True:
		try:
			m = int(input(strings['imachines']))
			if m <= 0:
				raise Exception()
			break
		except:
			os.system('cls')
			print (strings['input_err'])
	return m

def list_from_file(_list):
	strval = file[0]
	parse_string_to_list(strval, _list)

def machines_from_file():
	is_read = False
	while not is_read:
		try:
			m = int(file[1])
			is_read=True
		except:
			print('Critical error')
			exit(0)
	return m

def parse_string_to_list(lstring, _list):
	
	str_values = lstring.split()

	try:
		for it in str_values:

			ivalue = int(it)

			if ivalue < 0:
				raise Exception()

			_list.append(ivalue)
	
	except:
		_list.clear()

show_menu()

os.system("pause")
