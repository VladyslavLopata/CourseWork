import SPT

def show_menu():
    print('Course Work v0.1a.\nPlease, select the option:\n1. SPT')
    
    try:
        response = input()
        if int(response) == 1:
            SPT.SPT(verbose=True)
    except:
        print('Input is incorrect')
        show_menu()

show_menu()
