"""Wrong"""

from collections import Counter
import matplotlib.pyplot as plt
import numpy as np
import itertools

def algorithm(n_nodes, n_edges, edge_list, node_sorted, edge_data):

    # list of colors
    colour_list = [i for i in range(0, 1000)]

    temp = []
    temp_colours = [500]
    for i in node_sorted:
        colour_choice = [colour_list for i in node_sorted]
        colour_tuple = [np.nan for i in node_sorted]
        node_list_2 = node_sorted[i:] + node_sorted[:i]
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

    min_value = min(item[0] for item in temp)
    result = [item for item in temp if item[0] == min_value][0]
    return result[0], result[1]


with open(
        r'C:\Users\AjithSreenivasan\OneDrive - Robinson Bowmaker Paul\Coursera\Discrete Optimization\graph_coloring_2\Graph coloring\coloring\data\gc_250_9',
        'r') as input_data_file:
    input_data = input_data_file.read()
data_list = input_data.split()
data_list = list(map(int, data_list))
n_nodes = data_list[0]
n_edges = data_list[1]
edge_data = data_list[2:]
edge_list = [edge_data[i:i + 2] for i in range(0, int(len(edge_data)), 2)]
node_list = [i for i in range(0, n_nodes)]
# count_edges = sorted(Counter(edge_data).items())
node_counter = Counter(edge_data)
node_sorted_tuple = node_counter.most_common()
node_sorted = [item[0] for item in node_sorted_tuple]

# [counter[i][1] for i in node_list]

# plot
# plotting(edge_list)


number_colours, colours = algorithm(n_nodes, n_edges, edge_list, node_sorted, edge_data)

output_data = str(number_colours) + ' ' + str(0) + '\n'
output_data += ' '.join(map(str, colours))
print(','.join(map(str, colours)))
print(output_data)


