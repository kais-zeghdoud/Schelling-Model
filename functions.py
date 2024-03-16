import os, time, matplotlib.pyplot as plt, numpy as np
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


def calculate_execution_time(func, *args, **kwargs):
    start_time = time.time()
    func(*args, **kwargs)
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Temps d'exécution de {func.__name__}: {execution_time} secondes")

# e = [-471, -564, -666, -776, -990, -1086, -1201, -1405, -1571, -1707, -1967, -2248, -2516, -2917, -3024, -3264, -3172, -3985, -3997, -4310, -4417, -4664, -5241, -11695, -12698]