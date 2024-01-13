import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random
import time
import scipy as sp
from IPython.display import display, clear_output

primjer_staze_i_dodani_flow = ['A', 'B', 'D', 'F', 3]

checked_paths = [0, 0, 0, 0]

paths_list = [['A', 'B', 'D', 'F', 3],
            ['A', 'C', 'E', 'F', 2],
            ['A', 'C', 'G', 'F', 3],
            ['A', 'B', 'E', 'F', 10]]



def update_flow(G, primjer_staze_i_dodani_flow):
    # Simulate updating the flow values (you can replace this logic)
    for i in range(len(primjer_staze_i_dodani_flow) - 1):
        u, v = primjer_staze_i_dodani_flow[i], primjer_staze_i_dodani_flow[i + 1]
        if G.has_edge(u, v):
            G[u][v]['flow'] += primjer_staze_i_dodani_flow[-1]

def animate_flow_update(frame, G, pos, ax, paths_lists):
    for i in range(len(paths_list)):
        if checked_paths[i] == 0:
            update_flow(G, paths_lists[i])
            checked_paths[i] = 1
            
            # Clear the previous plot
            ax.clear()

            # Draw the directed graph with updated labels
            nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700, node_color=node_colors, font_color='black', font_size=10, edge_color='gray', width=1.5, alpha=0.7, arrowsize=15)

            # Add updated edge labels with flow/capacity information at the top of the edges
            edge_labels = {(u, v): f"{G[u][v]['flow']}/{G[u][v]['capacity']}" for u, v in G.edges()}
            nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red', bbox=dict(boxstyle="round,pad=0.3", edgecolor="none", facecolor="none"), verticalalignment="bottom")

            # Display the plot interactively
            display(fig)
            clear_output(wait=True)
            
            # Pause for a short time (adjust as needed)
            time.sleep(0.2)

    # Pause for a longer time after the loop (adjust as needed)
    time.sleep(2)



# Create a graph
graph_matrix = [[0, 12, 5, 0, 0, 0, 0],
                [0, 0, 0, 3, 4, 0, 0],
                [0, 0, 0, 0, 14, 0, 1],
                [0, 0, 0, 0, 0, 4, 0],
                [0, 0, 0, 0, 0, 3, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 2, 0]]


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


# Set the source ('A') and sink ('F') nodes
source_node = 'A'
sink_node = 'F'

# Create a list of node colors
node_colors = ['red' if node == source_node else 'blue' if node == sink_node else 'skyblue' for node in G.nodes()]
    

# tip rasporedbe
pos = nx.spectral_layout(G, center=None)
#pos = nx.spring_layout(G, seed=200)
#pos = nx.shell_layout(G)
#pos = nx.random_layout(G)
#pos = nx.circular_layout(G)


# Set up the animation
fig, ax = plt.subplots()
ani = FuncAnimation(fig, animate_flow_update, fargs=(G, pos, ax, paths_list),  interval=2000)  # Update every 2 seconds

plt.show()