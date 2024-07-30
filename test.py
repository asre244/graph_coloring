from collections import Counter

# Define the list with possible duplicates
my_list = [1, 2, 2, 3, 4, 4, 5]

# Count unique items using Counter
counter = Counter(my_list)

sorted_items = counter.most_common()

print(sorted_items)