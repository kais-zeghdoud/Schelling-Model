import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap


class Square:

    simulation = 0
    threshold = 2
    
    def __init__(self, size):
        self.size = size
        self.agents = size**2
        self.P = int(0.45 * self.agents)
        self.N = int(0.45 * self.agents)

        # création d'une matrice carrée de zéros de taille size*size
        tab = np.zeros((size, size), dtype=int)

        # répartition aléatoire des 1 dans la matrice carrée
        tab.ravel()[np.random.choice(self.agents, self.P, replace=False)] = 1

        # récupération des cases (i,j) égales à 0
        remaining_zeros = np.ravel_multi_index(np.where(tab==0), (size, size))

        # répartition aléatoire des -1 dans les cases 0 restantes
        tab.ravel()[np.random.choice(remaining_zeros, self.N, replace=False)] = -1
        
        # création du dataframe
        self.df = pd.DataFrame(tab)

        # création de la matrice de statisfaction
        self.update_satisfaction_df()


    def update_satisfaction_df(self):
        mat = []
        for i in range(self.size):
            row = []
            for j in range(self.size):
                row.append(self.satisfacion_agent(i,j))
            mat.append(row)
        self.satisfaction_df = pd.DataFrame(mat)


    def satisfacion_agent(self, i, j):
        agent = self.df.iloc[i,j]
        if agent == 0:
            return 0
        else:
            neighbors = 0
            for x in range(i-1, i+2):
                for y in range(j-1, j+2):
                    if (x,y) != (i,j) and 0<=x<len(self.df) and 0<=y<len(self.df):
                        if self.df.iloc[x,y] == agent:
                            neighbors += 1
            if neighbors >= self.threshold:
                return 1
            else: 
                return -1
            
    def is_square_satisfied(self):
        return not (self.satisfaction_df == -1).any().any()
    
    def satisfy(self):
        while not self.is_square_satisfied():
            for i in range(self.size):
                for j in range(self.size):
                    if self.satisfaction_df.iloc[i,j] == -1:
                        zero_idx = np.argwhere(self.df.values == 0) # récupération des indices des cases (i,j)=0
                        x,y = zero_idx[np.random.choice(len(zero_idx))] # selection aléatoire d'une case vide
                        self.df.iloc[x,y] = -1 # déplacement de l'agent insatisfait dans une case vide
                        self.df.iloc[i,j] = 0 # déplacement de la case vide à l'emplacement de l'agent insatisfait
            self.simulation += 1

            # updating satisfaction dataframe
            self.update_satisfaction_df()


    def show_matrix(self):
        # création d'une colormap personnalisée : Rouge, Blanc, Bleu
        custom_cmap = LinearSegmentedColormap.from_list('custom_map', [(1, 0, 0), (1, 1, 1), (0, 0, 1)], N=3)
        plt.imshow(self.df, cmap=custom_cmap, interpolation='nearest')
        plt.title("2D Square Network")
        plt.show()



s = Square(10)
print(s.df)
print(s.satisfaction_df)
print(s.is_square_satisfied())
s.satisfy()
print(f"{s.simulation =} {s.is_square_satisfied() =}")
s.show_matrix()