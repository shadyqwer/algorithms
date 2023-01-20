import math


class Graph:
    def __init__(self, num_nodes, edges, directed=False):
        # check if directed and weighted
        self.num_nodes = num_nodes
        self.directed = directed
        self.weighted = len(edges) > 0 and len(edges[0]) == 3

        # create adjacency list
        self.adj_list = [[] for _ in range(num_nodes)]
        self.weight = [[] for _ in range(num_nodes)]
        for edge in edges:
            self.adj_list[edge[0]].append(edge[1])
            if self.weighted:
                self.weight[edge[0]].append(edge[2])
            if not self.directed:
                self.adj_list[edge[1]].append(edge[0])
                if self.weighted:
                    self.weight[edge[1]].append(edge[2])

        # create adjacency matrix
        self.matrix = [[False for _ in range(num_nodes)] for _ in range(num_nodes)]
        for edge in edges:
            if self.weighted:
                self.matrix[edge[0]][edge[1]] = edge[2]
                if not directed:
                    self.matrix[edge[1]][edge[0]] = edge[2]
            else:
                self.matrix[edge[0]][edge[1]] = True
                if not directed:
                    self.matrix[edge[1]][edge[0]] = True

    def print_adj_matrix(self):
        print_matrix = ""
        for matrix in self.matrix:
            print_matrix += "{}\n".format(matrix)
        return print_matrix

    def print_adj_list(self):
        print_list = ""
        for i in range(len(self.adj_list)):
            if self.weighted:
                pairs = list(zip(self.adj_list[i], self.weight[i]))
            else:
                pairs = list(self.adj_list[i])
            print_list += "{}: {}\n".format(i, pairs)
        return print_list

    def __ham_helper(self, path, position, all_paths):
        if position == self.num_nodes:
            if self.matrix[path[-1]][path[0]]:
                all_paths.append(path.copy())
                all_paths[-1].append(path[0])
            return

        for next_vertex in range(self.num_nodes):
            if self.matrix[next_vertex][path[position - 1]] and next_vertex not in path:
                path.append(next_vertex)
                self.__ham_helper(path, position + 1, all_paths)
                path.pop()

    def hamiltonian_cycles(self, start_point=0):
        path = [start_point]
        all_paths = []
        self.__ham_helper(path, position=1, all_paths=all_paths)
        return all_paths

    def __str__(self):
        result = 'v: [(v, w), (v w),...]\n'
        for i in range(len(self.adj_list)):
            pairs = list(zip(self.adj_list[i], self.weight[i]))
            result += "{}: {}\n".format(i, pairs)
        return result

    def __repr__(self):
        return str(self)

