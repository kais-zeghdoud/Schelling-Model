import os
cls = lambda: os.system('cls')


def get_choice(menu:str, limit:int, clear=False)->int:
    if clear:
        cls()
    print("\n-------------------------------\n⬜️🔴🔵 Schelling Model 🔵🔴⬜️\n-------------------------------")
    choice = 0
    while choice < 1 or choice > limit:
        choice = int(input(menu))
    return choice