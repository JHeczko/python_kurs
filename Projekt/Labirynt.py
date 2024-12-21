import random
import networkx as nx
import numpy as np
from matplotlib import pyplot as plt
from Projekt.Partition import Partition


class Labirynt:
    def __init__(self, wiersze, kolumny):
        self.graph_base = nx.Graph()
        self.graph_base.add_nodes_from(list(x for x in range(wiersze*kolumny)))
        self.labirynt = nx.Graph
        self.wiersze = wiersze
        self.kolumny = kolumny

        for i in range(self.kolumny):
            for j in range(self.wiersze):
                if kolumny*(j+1)+i < kolumny*wiersze:
                    self.graph_base.add_edge((kolumny*j)+i, kolumny*(j+1)+i)
                if i != kolumny-1:
                    self.graph_base.add_edge((kolumny*j)+i, (kolumny*j+i)+1)

    def plot(self,opt):
        if opt==0:
            nx.draw(self.labirynt, with_labels=True, font_weight='bold')
        if opt==1:
            nx.draw(self.graph_base, with_labels=True, font_weight='bold')
        plt.show()

    def generate_maze_matrix(self):
        rows = self.wiersze
        cols = self.kolumny

        # Tworzenie macierzy z domyślnymi ścianami
        maze_matrix = np.ones((2 * rows + 1, 2 * cols + 1), dtype=int)

        # Ustaw przejścia w macierzy na podstawie grafu
        for row in range(rows):
            for col in range(cols):
                cell_index = row * cols + col
                maze_matrix[2 * row + 1][2 * col + 1] = 0  # Komórka

                if self.labirynt.has_edge(cell_index, cell_index + cols):  # Przejście w dół
                    maze_matrix[2 * row + 2][2 * col + 1] = 0

                if self.labirynt.has_edge(cell_index, cell_index + 1):  # Przejście w prawo
                    maze_matrix[2 * row + 1][2 * col + 2] = 0

        # Dodaj wejście i wyjście
        maze_matrix[0][1] = 0
        maze_matrix[rows*2][cols*2-1] = 0

        return maze_matrix

    def add_entrance_and_exit(self, maze_matrix):
        rows, cols = maze_matrix.shape

        # Możliwe pozycje dla wejścia i wyjścia (z krawędzi)
        edges = []

        # Górna i dolna krawędź
        for col in range(1, cols, 2):
            edges.append((0, col))  # Górna krawędź
            edges.append((rows - 1, col))  # Dolna krawędź

        # Lewa i prawa krawędź
        for row in range(1, rows, 2):
            edges.append((row, 0))  # Lewa krawędź
            edges.append((row, cols - 1))  # Prawa krawędź

        # Losowo wybierz wejście i wyjście
        entrance = random.choice(edges)
        edges.remove(entrance)
        exit_ = random.choice(edges)

        # Ustaw wejście i wyjście jako przejścia (`0`)
        maze_matrix[entrance] = 0
        maze_matrix[exit_] = 0

        print(f"Wejście: {entrance}, Wyjście: {exit_}")
        return maze_matrix

    def generate_random_labirynt(self):
        self.labirynt = self._kruskal_algorithm(self.graph_base)

    def _kruskal_algorithm(self, graph: nx.Graph):
        g = nx.Graph()
        g.add_nodes_from([x for x in range(graph.number_of_nodes())])

        kolejka = []
        for edge in graph.edges():
            kolejka.append(edge)
        max_int = len(kolejka)

        partition = Partition(graph.number_of_nodes())

        while (len(kolejka) != 0) and (partition.size() > 1):
            random_number = random.randint(0, max_int-1)
            edge = kolejka[random_number]
            max_int -= 1

            v0 = edge[0]
            v1 = edge[1]

            s = partition.find_set(v0)
            t = partition.find_set(v1)
            if not s==t:
                partition.join(s,t)
                g.add_edge(v0,v1)
            kolejka.pop(random_number)
        return g

