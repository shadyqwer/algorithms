from graphs import Graph
from list_sorting import ListSorting

# edges1 = [[0, 1, 5], [0, 2, 10], [1, 4, 4], [1, 5, 1], [2, 3, 2], [2, 6, 3]]
# graph1 = Graph(7, edges1)
# print(graph1.print_adj_list())
# print(graph1.print_adj_matrix())

new_list = ListSorting([6,2,31,22,10])
print(new_list)

print(new_list.insertion_sort(ascending=True))
print(new_list.insertion_sort(ascending=False))

print(new_list.selection_sort(ascending=True))
print(new_list.selection_sort(ascending=False))

print(new_list.bubble_sort(ascending=True))
print(new_list.bubble_sort(ascending=False))

print(new_list.merge_sort(ascending=True))
print(new_list.merge_sort(ascending=False))
print('-quick-')
print(new_list.quick_sort(ascending=True))
print(new_list.quick_sort(ascending=False))

print('-heap-')
print(new_list.heap_sort(ascending=True))
print(new_list.heap_sort(ascending=False))
