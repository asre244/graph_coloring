from collections import Counter
import matplotlib.pyplot as plt
import numpy as np


# def plotting(edges):
#     import matplotlib.pyplot as plt
#     import networkx as nx
#
#     # Create a graph using NetworkX
#     G = nx.Graph()
#     G.add_edges_from(edges)
#
#     # Use NetworkX to automatically determine positions of nodes
#     pos = nx.spring_layout(G)
#
#     # Create the plot
#     fig, ax = plt.subplots(figsize=(12, 8))
#
#     # Plot the nodes
#     nx.draw_networkx_nodes(G, pos, ax=ax, node_color='black', node_size=100)
#
#     # Plot the edges
#     nx.draw_networkx_edges(G, pos, ax=ax)
#
#     # Plot the node labels
#     nx.draw_networkx_labels(G, pos, ax=ax, font_size=5, font_color='red')
#
#     # Set axis limits and aspect ratio
#     ax.set_aspect('equal')
#
#     # Save the plot to a file
#     plt.savefig('graph_plot.png')
#
#     # Display the saved plot using an image viewer or browser
#     from PIL import Image
#     Image.open('graph_plot.png').show()


def algorithm(n_nodes, n_edges, edge_list, node_list, edge_data):
    # number of edges from node
    count_edges = sorted(Counter(edge_data).items())

    # list of colors
    colour_list = [i for i in range(0, 50)]

    n = 0
    colour_tuple = [np.nan for i in node_list]
    colour_choice = [colour_list for i in node_list]
    for n in node_list:
        colour_tuple[n] = colour_choice[n][0]
        sublist = [sub for sub in edge_list if n in sub]
        adjacent_nodes = [item for sub in sublist for item in sub if item != n]
        # Iterate through each index in B
        for index in adjacent_nodes:
            # Check if the index is within the range of A
            if index < len(colour_choice):
                # Remove all occurrences of 0 from the sublist at the given index
                colour_choice[index] = [item for item in colour_choice[index] if item != colour_tuple[n]]

    n_colours = len(set(colour_tuple))
    output_data_temp = str(n_colours) + ' ' + str(0) + '\n'
    output_data_temp += ' '.join(map(str, colour_tuple))
    return output_data_temp


with open(
        r'C:\Users\AjithSreenivasan\OneDrive - Robinson Bowmaker Paul\Coursera\Discrete Optimization\graph_coloring_2\Graph coloring\coloring\data\gc_50_3',
        'r') as input_data_file:
    input_data = input_data_file.read()
data_list = input_data.split()
data_list = list(map(int, data_list))
n_nodes = data_list[0]
n_edges = data_list[1]
edge_data = data_list[2:]
edge_list = [edge_data[i:i + 2] for i in range(0, int(len(edge_data)), 2)]
node_list = [i for i in range(0, n_nodes)]


# [counter[i][1] for i in node_list]

# plot
# plotting(edge_list)


output_data = algorithm(n_nodes, n_edges, edge_list, node_list, edge_data)
print(output_data)


