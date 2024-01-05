import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random
import time

primjer_staze_i_dodani_flow = ['A', 'B', 'D', 'F', 3]


def update_flow(G, primjer_staze_i_dodani_flow):
    # Simulate updating the flow values (you can replace this logic)
    for i in range(len(primjer_staze_i_dodani_flow) - 1):
        u, v = primjer_staze_i_dodani_flow[i], primjer_staze_i_dodani_flow[i + 1]
        if G.has_edge(u, v):
            G[u][v]['flow'] += primjer_staze_i_dodani_flow[-1]

def animate_flow_update(frame, G, pos, ax, primjer_staze_i_dodani_flow):
    # Update the flow values every 2 seconds
    if frame % 2 == 0:
        update_flow(G, primjer_staze_i_dodani_flow)

    # Clear the previous plot
    ax.clear()

    # Draw the directed graph with updated labels
    nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', font_color='black', font_size=10, edge_color='gray', width=1.5, alpha=0.7, arrowsize=15, connectionstyle='arc3,rad=0.1')

    # Add updated edge labels with flow/capacity information at the top of the edges
    edge_labels = {(u, v): f"{G[u][v]['flow']}/{G[u][v]['capacity']}" for u, v in G.edges()}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red', bbox=dict(boxstyle="round,pad=0.3", edgecolor="none", facecolor="none"), verticalalignment="bottom")

    # Show the plot
    plt.show()


# Create a graph
graph_matrix = [[0, 12, 5, 0, 0, 0],
                [0, 0, 0, 3, 0, 0],
                [0, 0, 0, 0, 14, 0],
                [0, 0, 0, 0, 0, 4],
                [0, 0, 0, 0, 0, 3],
                [0, 0, 0, 0, 0, 0]]


G = nx.DiGraph()

for i in range(len(graph_matrix)):
    slovo_vrh = chr(65 + i)
    G.add_node(slovo_vrh)

# end for

#pocetni graf sa tokom 0 u svim bridovima
for i in range(len(graph_matrix)):
    for j in range(len(graph_matrix[i])):
        if (graph_matrix[i][j] != 0):
            G.add_edge(chr(65+i), chr(65+j), flow = 0, capacity = graph_matrix[i][j])
    

pos = nx.spring_layout(G)

# Set up the animation
fig, ax = plt.subplots()
ani = FuncAnimation(fig, animate_flow_update, fargs=(G, pos, ax, primjer_staze_i_dodani_flow), interval=2000)  # Update every 2 seconds

plt.show()