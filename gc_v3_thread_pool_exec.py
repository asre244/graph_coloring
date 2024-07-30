from collections import Counter
import numpy as np
from concurrent.futures import ThreadPoolExecutor, as_completed
import pandas as pd

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

def algorithm(n_nodes, n_edges, edge_list, node_sorted, iter, edge_data):

    # list of colors
    colour_list = [i for i in range(0, 1000)]
    temp = []
    temp_colours = [500]
    colour_choice = [colour_list for i in node_sorted]
    colour_tuple = [np.nan for i in node_sorted]
    node_list_2 = node_sorted[iter:] + node_sorted[:iter]
    for n in node_list_2:
        temp_unique_colours = len(set([x for x in colour_tuple if not np.isnan(x)]))
        if temp_unique_colours >= min(temp_colours):
            break
        else:
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
    if np.nan in colour_tuple:
        pass
    else:
        temp_colours.append(n_colours)
        temp.append([n_colours, colour_tuple, node_list_2])

    temp_values = [item[0] for item in temp]
    min_value = min(temp_values)
    result = [item for item in temp if item[0] == min_value][0]
    return result[0], result[1]


def solve_it(input_data):
    data_list = input_data.split()
    data_list = list(map(int, data_list))
    n_nodes = data_list[0]
    n_edges = data_list[1]
    edge_data = data_list[2:]
    edge_list = [edge_data[i:i + 2] for i in range(0, int(len(edge_data)), 2)]
    node_list = [i for i in range(0, n_nodes)]

    node_counter = Counter(edge_data)
    node_sorted_tuple = node_counter.most_common()
    node_sorted = [item[0] for item in node_sorted_tuple]

    # [counter[i][1] for i in node_list]

    # plot
    # plotting(edge_list)
    final = []
    with ThreadPoolExecutor(max_workers=8) as executor:
        results = [executor.submit(algorithm, n_nodes, n_edges, edge_list, node_sorted, i, edge_data) for i in node_sorted]
        for f in as_completed(results):
            final.append(f.result())
    min_value = min(item[0] for item in final)
    result = [item for item in final if item[0] == min_value][0]
    output_data = str(min_value) + ' ' + str(0) + '\n'
    output_data += ' '.join(map(str, result))
    print(','.join(map(str, result)))
    print(output_data)
    return output_data

    # number_colours, colours = algorithm(n_nodes, n_edges, edge_list, node_sorted, edge_data)
    #
    # output_data = str(number_colours) + ' ' + str(0) + '\n'
    # output_data += ' '.join(map(str, colours))
    # print(','.join(map(str, colours)))
    # print(output_data)
    # return output_data


if __name__ == '__main__':
    file_location = r'S:\Jobs\EPWA\EPNR\Script\TEST\Discrete Optimization\assignment_3\Graph coloring\coloring\data\gc_70_7'
    with open(file_location, 'r') as input_data_file:
        input_data = input_data_file.read()
    solve_it(input_data)

