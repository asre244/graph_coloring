"""Wrong"""

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
        # print(count)
        # print(n_colours)
    min_value = min(item[0] for item in temp)
    result = [item for item in temp if item[0] == min_value][0]
    return result[0], result[1]


def algorithm_2(n_nodes, n_edges, edge_list, node_sorted, edge_data, number_colours, colours):

    # list of colors
    colour_list = [i for i in range(0, 1000)]
    count = n_nodes
    temp = []
    temp_colours = [number_colours]
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
        # print(count)
        # print(n_colours)
    try:
        min_value = min(item[0] for item in temp)
        result = [item for item in temp if item[0] == min_value][0]
    except:
        result = [number_colours, colours]
    return result[0], result[1]

with open(
        r'C:\Users\AjithSreenivasan\OneDrive - Robinson Bowmaker Paul\Coursera\Discrete Optimization\graph_coloring_2\Graph coloring\coloring\data\gc_100_5',
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

solution_list = []
# [counter[i][1] for i in node_list]

# plot
# plotting(edge_list)


number_colours, colours = algorithm(n_nodes, n_edges, edge_list, node_sorted, edge_data)


output_data = str(number_colours) + ' ' + str(0) + '\n'
output_data += ' '.join(map(str, colours))
# print(','.join(map(str, colours)))
print(output_data)
# finish = time.time()
# print(finish - start)

sorted_node_tuple = sorted(node_sorted_tuple, key=lambda x: x[0])
A_list = list(sorted_node_tuple)
counter = 0


while counter < 10:

    colour_tuple = [(node_list[i], colours[i]) for i in range(0, n_nodes)]
    sorted_colour_tuple = sorted(colour_tuple, key=lambda x: x[0])

    B_list = list(sorted_colour_tuple)


    # Combine the corresponding elements from A and B into a single list C
    C = list(zip(A_list, B_list))

    # Sort C based on the second values of the elements from B in descending order
    C_sorted_by_B = sorted(C, key=lambda x: x[0][1], reverse=True)

    # Sort C based on the second values of the elements from A in descending order
    C_sorted_by_A = sorted(C_sorted_by_B, key=lambda x: x[1][1], reverse=True)
    node_sorted = [elem[0][0] for elem in C_sorted_by_A]
    # Extract the first elements from the tuples in C_sorted_by_A

    number_colours, colours = algorithm(n_nodes, n_edges, edge_list, node_sorted, edge_data)
    # number_colours, colours = algorithm_2(n_nodes, n_edges, edge_list, node_sorted, edge_data, number_colours, colours)

    solution_list.append([number_colours, colours])
    n_colour_solution = min(item[0] for item in solution_list)
    result = [item for item in solution_list if item[0] == n_colour_solution][0]
    output_data = str(result[0]) + ' ' + str(0) + '\n'
    output_data += ' '.join(map(str, result[1]))
    print(output_data)
    counter += 1
    pass
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