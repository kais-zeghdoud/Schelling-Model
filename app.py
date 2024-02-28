from schelling import Square
from functions import *


choice = 0
menu = "-----------MAIN MENU-----------\n\
        1: Study of a 2D Square Network\n\
        2: Study of any network\n\
        3: Quit the application\n"

menu1 = "-----------2D Square Network-----------"

menu2 = "-----------Any Network-----------"


cls()
while choice != 3:
    choice = get_choice(menu, 3)
    match choice:
        case 1:
            choice1 = get_choice(menu1, 4, True)
            match choice1:
                case 1:
                    pass
                case 2:
                    pass
                case 3:
                    pass
                case 4:
                    pass

        case 2:
            choice2 = get_choice(menu2, 5, True)
            match choice2:
                case 1:
                    pass
                case 2:
                    pass
                case 3:
                    pass
                case 4:
                    pass
                case 5:
                    pass

        case 3:
            print("Closing Schelling Model Application")