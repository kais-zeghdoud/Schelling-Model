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


def get_dynamics_average(arr:list)->list:
    return [np.nanmean([subarr[i] for subarr in arr if len(subarr) > i]) for i in range(max(map(len, arr)))]


def get_plot(tab:list, title:str, x:str, y:str, xticks=False):
    if xticks:
        plt.plot(xticks, tab, marker='o', linestyle='-')
        plt.xticks(xticks)
    else:
        plt.plot(tab, marker='o', linestyle='-')
    plt.title(title)
    plt.xlabel(x)
    plt.ylabel(y)
    plt.show()