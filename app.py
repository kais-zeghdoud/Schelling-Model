from schelling import Square
from functions import *


choice = 0
menu = "-----------MAIN MENU-----------\n\
        1: Set default threshold\n\
        2: Study of a 2D Square Network\n\
        3: Study of any network\n\
        4: Quit the application\n"

menu1 = "-----------2D Square Network-----------\n\
        1: Plot single dynamic E(i)\n\
        2: Plot for 100 dynamics <E>(i)\n\
        3: Plot <E∞>(n) with n ∈ [10,100]\n\
        4:\n\
        5:\n"

menu2 = "-----------Any Network-----------"


cls()
while choice != 3:
    choice = get_choice(menu, 3)
    match choice:
        case 1:
            threshold = 0
            while threshold<=0 or threshold>=1:
                threshold = float(input("Set default threshold: "))
       
        case 2:
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

        case 3:
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

        case 4:
            print("Closing Schelling Model Application")