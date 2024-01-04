import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random


# Create a graph
graph_matrix = [[0, 12, 5, 0, 0, 0],
                [0, 0, 0, 3, 0, 0],
                [0, 0, 0, 0, 14, 0],
                [0, 0, 0, 0, 0, 4],
                [0, 0, 0, 0, 0, 3],
                [0, 0, 0, 0, 0, 0]]


G = nx.Graph()

for i in range(len(graph_matrix)):
    for j in range(len(graph_matrix[i])):
        print(graph_matrix[i][j])
