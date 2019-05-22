from Strings import strings
import os

file = ''


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
            print(strings['input_err'])
    return m


def list_from_file(_list):

    global file
    if not file:
        file = init_file()

    strval = file[0]
    parse_string_to_list(strval, _list)


def machines_from_file():

    global file
    if file == None:
        file = init_file()

    is_read = False
    while not is_read:
        try:
            m = int(file[1])
            is_read = True
        except:
            print(strings['input_err'])
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


def init_file():

    file_read = False

    _file = ""

    while not file_read:

        try:
            _file = open('input.txt').readlines()
            assert_file_format(_file)
            file_read = True
        except IOError:
            os.system('cls')
            print(strings['eiofnotfound'])
            input()

    return _file


def assert_file_format(_file):

    if len(_file) != 2:
        raise IOError()
    elif len(_file[1].strip().split()) != 1 or len(_file[0].strip().split()) < 1:
        raise IOError()

    for st in _file[0].strip().split():
        if not st.isnumeric():
            raise IOError
