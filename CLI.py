import os

import algorithms.LocalFirst as LocalFirst
import algorithms.LocalSecond as LocalSecond
import algorithms.SPT as SPT
import utility.Util
from utility.Strings import strings


def show_menu():

    while True:

        os.system('cls')

        mode = get_input_mode()

        if mode == strings['input_modes'][3][1]:
            break
        elif mode != strings['input_modes'][0][1]:
            call_functions(handle_input(mode))
        else:
            call_functions(utility.Util.generate_random_case())

        os.system('pause')


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

    print(strings['msel'], mode)

    return mode


def handle_input(mode):
    _list = []
    m = 0
    n = 0

    import utility.CLIUtil as clu
    # functions corresponding to input methods
    fn = {strings['input_modes'][1][1]: [clu.manual_list_input, clu.manual_machines_input],
          strings['input_modes'][2][1]: [clu.list_from_file, clu.machines_from_file]}

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

    print(strings['festimates'].format(
        utility.Util.target_C_max(matrix), utility.Util.target_C_macron(matrix)))


def call_functions(ivals):

    os.system("cls")

    _list, m, n = ivals

    print('{}\n{}'.format(strings['finitial'], _list))

    print_matrix(SPT.SPT(_list=_list, m=m, n=n), strings['SPT'])
    print_matrix(LocalFirst.local_first(
        _list=_list, m=m, n=n), strings['lfirst'])
    print_matrix(LocalSecond.local_second(
        _list=_list, m=m, n=n), strings['lsecond'])


def suspend_app():
    os.system("cls")
    os.system("pause")
