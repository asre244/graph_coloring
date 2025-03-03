"""This is example of local minima

The way the algorithm is structured us such that the def(color) cannot better the solution unless that initial solution
configuration is changed"""

from collections import Counter
import matplotlib.pyplot as plt
import numpy as np
import time
import itertools
start = time.time()

def algorithm(n_nodes, n_edges, edge_list, node_sorted, edge_data):

    # list of colors
    colour_list = [i for i in range(0, 1000)]
    count = n_nodes
    temp = []
    temp_colours = [500]
    for i in range(0, n_nodes):
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
            temp.append([n_colours, colour_tuple])
        count -= 1
        print(count)
        print(n_colours)
    min_value = min(item[0] for item in temp)
    result = [item for item in temp if item[0] == min_value][0]
    return result[0], result[1]


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
finish = time.time()
print(finish - start)


colour_tuple = [(node_list[i], colours[i]) for i in range(0, n_nodes)]


"""not working


def check(color, j):
    if color != 0:
        list = []
        list.append([sub for sub in edge_list if j in sub])
        list = list[0]
        reordered_list = []
        for t in list:
            if t[0] != j:
                reordered_list.append(t)
            else:
                reordered_list.append((t[1], t[0]))
        elements_check = [t[0] for t in reordered_list]
        neighbor_list = [t for t in colour_tuple if t[0] in elements_check]
        neighbor_list_highest_color = [item for item in neighbor_list if item[1] == color - 1]
        if neighbor_list_highest_color != []:
            for neighbor_color in [t[0] for t in neighbor_list_highest_color]:
                check(color - 1, neighbor_color)
        else:
            pass
    else:
        pass




for i in range(number_colours - 1, -1, -1):
    result = [item for item in colour_tuple if item[1] == i]
    elements = [t[0] for t in result]
    for element in elements:
        check(i, element)
    # result = [item for item in colour_tuple if item[1] == 7]
    # elements = [t[0] for t in result]
    # list = []
    # for element in elements:
    #     list.append([sub for sub in edge_list if element in sub])
    #     pass
    #
    # list = list[0]
    # elements_check = [t[0] for t in list]
    # result_1 = result = [t for t in colour_tuple if t[0] in elements_check]

"""