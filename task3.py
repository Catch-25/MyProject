from two_smallest import find_two_smallest
from integers import list1, list2, list3

all_lists = [list1, list2, list3]
results = []

for current_list in all_lists:
    smallest_pair = find_two_smallest(current_list)
    results.append(f"List: {current_list}, Smallest two: {smallest_pair}\n")

with open("results.txt", "w") as f:
    f.writelines(results)

print("Results saved to results.txt")