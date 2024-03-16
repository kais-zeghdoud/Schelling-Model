from schelling import Square
from functions import *
import matplotlib.pyplot as plt
import numpy as np


choice = 0
menu = "-----------MAIN MENU-----------\n\
        1: Study of a 2D Square Network\n\
        2: Study of any network\n\
        3: Quit the application\n"

menu1 = "-----------2D Square Network-----------\n\
        1: Plot single dynamic E(i) for n=20 and q=51%\n\
        2: Plot for 100 dynamics <E>(i) for 100 different dynamics (n=20 and q=51%)\n\
        3: Plot <E∞>(n) with n ∈ [10,100]\n\
        4: [Move within 8 of nearby neighbors] Plot single dynamic E(i) for n=20 and q=51%\ \n\
        5: [Move within 8 of nearby neighbors] Plot for 100 dynamics <E>(i) for 100 different dynamics (n=20 and q=51%)\n\
        6: [Move within 8 of nearby neighbors] Plot <E∞>(n) with n ∈ [10,100]\n\
        7: [Move within 24 of nearby neighbors] Plot single dynamic E(i) for n=20 and q=51%\ \n\
        8: [Move within 24 of nearby neighbors] Plot for 100 dynamics <E>(i) for 100 different dynamics (n=20 and q=51%)\n\
        9: [Move within 24 of nearby neighbors] Plot <E∞>(n) with n ∈ [10,100]\n"

menu2 = "-----------Any Network-----------"


cls()
while choice != 3:
    choice = get_choice(menu, 3)
    match choice:
       
        case 1:
            choice1 = get_choice(menu1, 9, True)
            match choice1:
                case 1:
                    s = Square(20)
                    s.free_move()
                    s.show_matrix()
                    s.plot_dynamic()

                case 2:
                    dynamics = []
                    for i in range(100):
                        s = Square(20)
                        s.free_move()
                        dynamics.append(s.energy)
                    average = get_dynamics_average(np.array(dynamics))
                    plot_average(average)

                case 3:
                    pass

                case 4:
                    s = Square(20)
                    s.restricting_move() # SPECIFY 8 NEIGHBORS
                    s.show_matrix()
                    s.plot_dynamic()
                    
                case 5:
                    dynamics = []
                    for i in range(100):
                        s = Square(20)
                        s.restricting_move()  # SPECIFY 8 NEIGHBORS
                        dynamics.append(s.energy)
                    average = get_dynamics_average(np.array(dynamics))
                    plot_average(average)
                
                case 6:
                    pass

                case 7:
                    s = Square(20)
                    s.restricting_move() # SPECIFY 24 NEIGHBORS
                    s.show_matrix()
                    s.plot_dynamic()
                    
                case 8:
                    dynamics = []
                    for i in range(100):
                        s = Square(20)
                        s.restricting_move() # SPECIFY 24 NEIGHBORS
                        dynamics.append(s.energy)
                    average = get_dynamics_average(np.array(dynamics))
                    plot_average(average)
                
                case 9:
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