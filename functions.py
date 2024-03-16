import os, matplotlib.pyplot as plt, numpy as np
cls = lambda: os.system('cls')


def get_choice(menu:str, limit:int, clear=False)->int:
    if clear:
        cls()
    print("\n-------------------------------\n⬜🔴🔵 Schelling Model 🔵🔴⬜️\n-------------------------------")
    choice = 0
    while choice < 1 or choice > limit:
        choice = int(input(menu))
    return choice


def get_dynamics_average(arr:np.ndarray)->list:
    return [np.nanmean([subarr[i] for subarr in arr if len(subarr) > i]) for i in range(max(map(len, arr)))]


def plot_average(avg:list, n=20):
    plt.plot(avg)
    plt.title(f"100 different dynamics average for 2D Square Network ({n=})")
    plt.xlabel("Iteration")
    plt.ylabel("<E(i)>")
    plt.show()