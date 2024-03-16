import os, matplotlib.pyplot as plt
cls = lambda: os.system('cls')


def get_choice(menu:str, limit:int, clear=False)->int:
    if clear:
        cls()
    print("\n-------------------------------\n⬜🔴🔵 Schelling Model 🔵🔴⬜️\n-------------------------------")
    choice = 0
    while choice < 1 or choice > limit:
        choice = int(input(menu))
    return choice

def get_dynamics_average(dynamics:list)->list:
    pass

def plot_average(avg:list):
    plt.plot(avg)
    plt.title(f"100 different dynamics average for 2D Square Network (n=20)")
    plt.xlabel("Iteration")
    plt.ylabel("E(i)")
    plt.show()