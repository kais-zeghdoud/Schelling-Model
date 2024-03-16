import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from PIL import Image
import time

def calculate_execution_time(func, *args, **kwargs):
    start_time = time.time()
    func(*args, **kwargs)
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Temps d'exécution de {func.__name__}: {execution_time} secondes")

class Square:
    simulation = 0
    threshold = 0.51

    def __init__(self, size):
        self.size = size
        self.agents = size ** 2
        self.P = int(0.45 * self.agents)
        self.N = int(0.45 * self.agents)
        self.energy = []

        # création d'une matrice carrée de zéros de taille size*size
        tab = np.zeros((size, size), dtype=int)

        # répartition aléatoire des 1 dans la matrice carrée
        tab.ravel()[np.random.choice(self.agents, self.P, replace=False)] = 1

        # récupération des cases (i,j) égales à 0
        remaining_zeros = np.ravel_multi_index(np.where(tab == 0), (size, size))

        # répartition aléatoire des -1 dans les cases 0 restantes
        tab.ravel()[np.random.choice(remaining_zeros, self.N, replace=False)] = -1

        # création du dataframe
        self.df = pd.DataFrame(tab)
        self.INITIAL_DF = self.df.copy(deep=True)

        # création du dataframe étendu
        self.update_extended_df()

        # création de la matrice de statisfaction
        self.update_satisfaction_df()

    def update_extended_df(self):
        high = pd.Series([self.df.iloc[self.size - 1].tolist()[-1]] + self.df.iloc[self.size - 1].tolist() + [
            self.df.iloc[self.size - 1].tolist()[0]])
        low = pd.Series([self.df.iloc[0].tolist()[-1]] + self.df.iloc[0].tolist() + [self.df.iloc[0].tolist()[0]])
        left = self.df[len(self.df) - 1]
        right = self.df[0]
        middle = pd.DataFrame([(left[i], *self.df.iloc[i].tolist(), right[i]) for i in range(self.size)])
        self.extended_df = pd.DataFrame([high, *middle.values, low])

    def update_satisfaction_df(self):
        mat = []
        for i in range(self.size):
            row = []
            for j in range(self.size):
                row.append(self.get_agent_satisfaction(i, j))
            mat.append(row)
        self.satisfaction_df = pd.DataFrame(mat)

    def get_agent_satisfaction(self, i, j):
        agents = 0  # neighbors that are not empty cases
        agent = self.df.iloc[i, j]
        if agent == 0:
            return 0
        else:
            neighbors = 0
            for x in range(i - 1, i + 2):
                for y in range(j - 1, j + 2):
                    if (x, y) != (i, j):
                        if self.extended_df.iloc[x + 1, y + 1] != 0:
                            agents += 1
                        if self.extended_df.iloc[x + 1, y + 1] == agent:
                            neighbors += 1
            # récupération du pourcentage d'agents voisins similaires
            try:
                ratio = neighbors / agents
            except ZeroDivisionError:
                ratio = 0
            # détermination de la satisfaction de l'agent (i,j)
            if ratio >= self.threshold:
                return 1
            else:
                return -1

    def is_square_satisfied(self):
        return not (self.satisfaction_df == -1).any().any()

    def free_move(self):
        print("Free move")
        while not self.is_square_satisfied():
            for i in range(self.size):
                for j in range(self.size):
                    if self.satisfaction_df.iloc[i, j] == -1:
                        zero_idx = np.argwhere(self.df.values == 0)  # récupération des indices des cases (i,j)=0
                        x, y = zero_idx[np.random.choice(len(zero_idx))]  # selection aléatoire d'une case vide
                        self.df.iloc[x, y] = self.df.iloc[i, j]  # déplacement de l'agent insatisfait dans une case vide
                        self.df.iloc[i, j] = 0  # déplacement de la case vide à l'emplacement de l'agent insatisfait
                        # maj des DF
                        self.update_extended_df()
                        self.update_satisfaction_df()

            # new iteration done
            self.simulation += 1
            self.energy.append(self.compute_energy())

    def restricting_move(self, nbr_neighbors):
        print("Restricting move")
        # Parcourir tous les agents de la matrice si il y a des agents insatisfaits
        while not self.is_square_satisfied():
            for i in range(self.size):
                for j in range(self.size):
                    # print("1 = " + str(i) + "; j = " + str(j))
                    if self.satisfaction_df.iloc[i, j] == -1:
                        # Récupération des indices des 8 voisins les plus proches
                        if nbr_neighbors == 8:
                            neighbors_indices =[(i + x, j + y) for x in range(-1, 2) for y in range(-1, 2) if
                                                (x != 0 or y != 0)]
                        elif nbr_neighbors == 24:
                            neighbors_indices = [(i + x, j + y) for x in range(-2, 3) for y in range(-2, 3) if
                                                 (x != 0 or y != 0)]
                        else:
                            return;

                        # Mélange des indices pour choisir aléatoirement la destination potentielle  de l'agent insatisfait.
                        np.random.shuffle(neighbors_indices)

                        # Recherche d'un voisin non occupé
                        found = False
                        for x, y in neighbors_indices:
                            if 0 <= x < self.size and 0 <= y < self.size and self.df.iloc[x, y] == 0:
                                found = True
                                # Déplacer l'agent insatisfait
                                self.df.iloc[x, y] = self.df.iloc[i, j]
                                self.df.iloc[i, j] = 0
                                break

                        if not found:
                            # Aucun voisin non occupé trouvé, cet agent reste à sa place
                            self.satisfaction_df.iloc[i, j] = 1  # L'agent est maintenant satisfait

                        # Mise à jour
                        self.update_extended_df()
                        self.update_satisfaction_df()

            # Nouvelle itération
            self.simulation += 1
            self.energy.append(self.compute_energy())

    def compute_energy(self) -> int:
        energy = 0
        for i in range(self.size):
            for j in range(self.size):
                energy += self.df.iloc[i, j] * sum(self.get_neighbors_sum(i, j))
        return - energy

    def get_neighbors_sum(self, i: int, j: int):
        for x in range(i - 1, i + 2):
            for y in range(j - 1, j + 2):
                if (x, y) != (i, j):
                    yield self.extended_df.iloc[x, y]

    def show_matrix(self):
        fig, axs = plt.subplots(1, 2)
        # création d'une colormap personnalisée : Rouge, Blanc, Bleu
        custom_cmap = LinearSegmentedColormap.from_list('custom_map', [(1, 0, 0), (1, 1, 1), (0, 0, 1)], N=3)

        axs[0].imshow(self.INITIAL_DF, cmap=custom_cmap, interpolation='nearest')
        axs[0].set_title(f"2D Square Network at iteration 0")
        axs[0].set_xticks([])
        axs[0].set_yticks([])

        axs[1].imshow(self.df, cmap=custom_cmap, interpolation='nearest')
        axs[1].set_title(f"2D Square Network at iteration {self.simulation}")
        axs[1].set_xticks([])
        axs[1].set_yticks([])

        plt.show()

    def plot_dynamic(self):
        plt.plot(self.energy)
        plt.title(f"Energy Dynamic for 2D Square Network (n={self.size})")
        plt.xlabel("Iteration")
        plt.ylabel("E(i)")
        plt.show()


s = Square(20)
# s.free_move()
calculate_execution_time(s.restricting_move(8))
s.show_matrix()
print(f"{s.simulation =} {s.is_square_satisfied() =} {s.energy =}")
s.plot_dynamic()
