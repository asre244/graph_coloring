"""Wrong"""

from collections import Counter
import matplotlib.pyplot as plt
import numpy as np
import time
import itertools
start = time.time()

def algorithm(n_nodes, n_edges, edge_list, node_sorted, edge_data):

    # list of colors
    colour_list = [i for i in range(0, 5)]
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


# n_nodes = 4
# edge_list = [[0,1],[0,2],[0,3],[2,3],[1,2]]


n_nodes = 10
edge_list = [[5,1],[5,2],[5,3],[5,4],[0,6],[0,7],[0,8],[1,6],[2,7],[3,8],[4,9]]
node_list = [i for i in range(0, n_nodes)]
# count_edges = sorted(Counter(edge_data).items())
edge_data = [item for sublist in edge_list for item in sublist]
n_edges = len(edge_list)
node_counter = Counter(edge_data)
node_sorted_tuple = node_counter.most_common()
node_sorted = [item[0] for item in node_sorted_tuple]


# Create adjacency list
adj_list = {i: set() for i in range(n_nodes)}
for edge in edge_list:
    adj_list[edge[0]].add(edge[1])
    adj_list[edge[1]].add(edge[0])

# Helper function to get first-order and second-order connections
def get_ordered_connections(start_node, adj_list):
    first_order = list(adj_list[start_node])
    second_order = set()

    for node in first_order:
        second_order.update(adj_list[node])

    # Remove start_node from second_order connections
    if start_node in second_order:
        second_order.remove(start_node)

    # Remove first_order nodes from second_order connections
    second_order -= set(first_order)

    return first_order, list(second_order)


# Get the first-order and second-order connections for the most connected node
most_connected_node = node_sorted[0]
first_order, second_order = get_ordered_connections(most_connected_node, adj_list)

# Combine the nodes while ensuring no duplicates
node_sorted_2 = [most_connected_node] + first_order + second_order

# Add any remaining nodes that weren't covered in first or second-order connections
remaining_nodes = set(range(n_nodes)) - set(node_sorted_2)
node_sorted_2.extend(remaining_nodes)

# Print the final sorted list of nodes
print("Original node_sorted:", node_sorted)
print("New node_sorted_2:", node_sorted_2)

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


# colour_tuple = [(node_list[i], colours[i]) for i in range(0, n_nodes)]
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