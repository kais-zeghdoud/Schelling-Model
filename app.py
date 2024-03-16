from schelling import Square
from functions import *
import matplotlib.pyplot as plt
import numpy as np
import threading


choice = 0
menu = "-----------MAIN MENU-----------\n\
    1: Study of a 2D Square Network\n\
    2: Study of any network\n\
    3: Quit the application\n"

menu1 = "-----------2D Square Network-----------\n\
    1: Plot single dynamic E(i) for n=20 and q=51%\n\
    2: Plot for 100 dynamics <E>(i) for 100 different dynamics (n=20 and q=51%)\n\
    3: Plot <E∞>(n) with n ∈ [10,100]\n\n\
    4: [Move within 8 of nearby neighbors] Plot single dynamic E(i) for n=20 and q=51% \n\
    5: [Move within 8 of nearby neighbors] Plot for 100 dynamics <E>(i) for 100 different dynamics (n=20 and q=51%)\n\
    6: [Move within 8 of nearby neighbors] Plot <E∞>(n) with n ∈ [10,100]\n\n\
    7: [Move within 24 of nearby neighbors] Plot single dynamic E(i) for n=20 and q=51% \n\
    8: [Move within 24 of nearby neighbors] Plot for 100 dynamics <E>(i) for 100 different dynamics (n=20 and q=51%)\n\
    9: [Move within 24 of nearby neighbors] Plot <E∞>(n) with n ∈ [10,100]\n\n\
    10: Go back to main menu\n"

menu2 = "-----------Any Network-----------\n\
    1: For n = 400 and q = 51%, plot for a single dynamic : E(i) with i iteration number, until the algorithm converges.\n\
    2: For n = 400 and q = 51%, plot for 100 different dynamics : < E > (i) with <> being the average over the 100 dynamics.\n\
    3: We define E∞ as the energy value after convergence of the algorithm, which depends a priori on the number n of vertices, which is why we can write E∞(n).\n\
    Plot for q = 51%, < E∞ > (n) with n ∈ [[10,1000]].\n\
    4: Study the network effects in a graph for Schelling's model\n"


cls()
while choice != 3:
    choice = get_choice(menu, 3)
    match choice:
       
        case 1:
            choice1 = get_choice(menu1, 10, True)
            match choice1:
                case 1:
                    s = Square(20)
                    s.free_move()
                    print(s.df)
                    s.show_matrix()
                    s.plot_dynamic()

                case 2:
                    dynamics = []
                    for i in range(101):
                        s = Square(20)
                        s.free_move()
                        dynamics.append(s.energy)
                        print(f"Dynamic {i} done: {s.energy=}")
                    average = get_dynamics_average(dynamics)
                    get_plot(average, "100 different dynamics average for 2D Square Network (n=20, q=51%)", "Iteration", "<E(i)>")

                case 3:
                    energies = []
                    for n in range(10, 101): # n ∈ [10,100]
                        s = Square(n)
                        s.free_move()
                        energies.append(s.energy[-1]) # getting the E∞ value after convergence of the algorithm
                        print(f"Square with size {n} done: {s.energy[-1]=}")
                    get_plot(energies, "E∞(n) value after algorithm convergence for Squares with n ∈ [10,100]", "Square Size n", "E∞", [n for n in range(10,101)])

                case 4:
                    s = Square(20)
                    s.restricting_move(8) # 8 nearest neighbors
                    s.show_matrix()
                    s.plot_dynamic()
                    
                case 5:
                    dynamics = []
                    for i in range(11):
                        s = Square(20)
                        s.restricting_move(8,)  # 8 nearest neighbors
                        dynamics.append(s.energy)
                        print("dynamic ", i, " done")
                    average = get_dynamics_average(np.array(dynamics))
                    get_plot(average, "10 different dynamics average for 2D Square Network (n=20, q=51%, 8 nearest neighboors)", "Iteration", "<E(i)>")
                
                case 6:
                    energies = []
                    for n in range(10, 101): # n ∈ [10,100]
                        s = Square(n)
                        s.restricting_move(8) # 8 nearest neighbors
                        energies.append(s.energy[-1]) # getting the E∞ value after convergence of the algorithm
                        print(f"Square with size {n} done: {s.energy[-1]=}")
                    get_plot(energies, "E∞(n) value after algorithm convergence for Squares with n ∈ [10,100]", "Square Size n", "E∞", [n for n in range(10,101)])

                case 7:
                    s = Square(20)
                    s.restricting_move(24) # 24 nearest neighbors
                    s.show_matrix()
                    s.plot_dynamic()
                    
                case 8:
                    dynamics = []
                    for i in range(11):
                        s = Square(20)
                        s.restricting_move(24) # 24 nearest neighbors
                        dynamics.append(s.energy)
                    average = get_dynamics_average(np.array(dynamics))
                    get_plot(average,  "10 different dynamics average for 2D Square Network (n=20, q=51%, 24 nearest neighboors)", "Iteration", "<E(i)>")
                
                case 9:
                    energies = []
                    for n in range(10, 101): # n ∈ [10,100]
                        s = Square(n)
                        s.restricting_move(24) # 24 nearest neighbors
                        energies.append(s.energy[-1]) # getting the E∞ value after convergence of the algorithm
                        print(f"Square with size {n} done: {s.energy[-1]=}")
                    get_plot(energies, "E∞(n) value after algorithm convergence for Squares with n ∈ [10,100]", "Square Size n", "E∞", [n for n in range(10,101)])

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