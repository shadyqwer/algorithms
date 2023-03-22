import math


class Graph:
    # edges = [node1, node2, weight]
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

    # Hamiltonian paths are paths that visit every node in a graph exactly once.
    # Hamiltonian paths are a special case of Hamiltonian cycles, cycles that visit every node in a graph exactly once.
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

    # Dijkstra finds the shortest paths from one node to every other node in simple graph.
    # Either directed or undirected, on weighted use breath-first search.
    # Does not work on negative edge weights.
    # Runtime depends on data structure used for distance and unvisited nodes.
    def dijkstra(self, source):
        if not self.weighted:
            print("Graph is not weighted, use BFS.")
            return False
        distance = {node: math.inf for node in range(self.num_nodes)}  # set each distance at infinity
        distance[source] = 0  # starting distance to 0
        unvisited = [i for i in range(self.num_nodes)]  # unvisited nodes

        while unvisited:
            # find node with minimum distance so far, in first step it is always source
            min_node = None
            for node in unvisited:
                if min_node is None:
                    min_node = node
                elif distance[node] < distance[min_node]:
                    min_node = node

            # loop over edges of min distance node
            for edge in range(len(self.adj_list[min_node])):
                cost = self.weight[min_node][edge]  # cost to next outgoing edge
                next_node = self.adj_list[min_node][edge]  # outgoing edge
                if cost + distance[min_node] < distance[next_node]:  # reduce cost if can
                    distance[next_node] = cost + distance[min_node]
            unvisited.remove(min_node)
        return distance

    # As Dijkstra, it is also used for finding the shortest paths from one node to every other node in simple graph.
    # Bellman-Ford works for negative edge weights but without negative cycles.
    # Finds the shortest paths in O(V * E) where V is number of nodes and E number of edges.
    # Max edges any path can have is V - 1, so if in Vth iteration if there is shorter path negative cycle exist.
    def bellman_ford(self, source):
        distance = {node: math.inf for node in range(self.num_nodes)}  # distance for all nodes
        distance[source] = 0  # source node
        for i in range(self.num_nodes):
            done = True
            for node in range(self.num_nodes):  # loop over every node
                for edge in range(len(self.adj_list[node])):  # loop over outgoing edges
                    cost = self.weight[node][edge]
                    next_node = self.adj_list[node][edge]
                    if cost + distance[node] < distance[next_node]:
                        distance[next_node] = cost + distance[node]
                        done = False
                        if i == self.num_nodes - 1:  # there is negative weight cycle
                            print("Found negative edge weight cycle.")
                            return False
            if done:  # nothing changed, the shortest paths found
                break
        return distance

    # Prim's algorithm finds minimum (weight) spanning tree in weighted undirected graph.
    # Runs in O(V^2) where V is number of nodes
    # Takes adjacency matrix as input and returns parent pointers.
    def prims_mst(self):
        mst = [False for _ in range(self.num_nodes)]  # keep track of nodes included in mst so far
        parent = [None if i else -1 for i in range(self.num_nodes)]  # parent nodes, first node will have no parent
        value = [math.inf if i else 0 for i in range(self.num_nodes)]  # keep track of min weights, starting node is 0

        for _ in range(self.num_nodes):  # for each node in graph
            # find minimum weight vertex from vertices not in mst yet, and get its index
            next_node = math.inf
            for v in range(self.num_nodes):
                if value[v] < next_node and not mst[v]:
                    next_node = value[v]
                    index = v

            mst[index] = True  # include next node in mst
            for vertex in range(self.num_nodes):  # loop over its edges
                # check if vertex not in mst, if edge exist, and if value is smaller than current smallest
                if not mst[vertex] and self.matrix[index][vertex] and self.matrix[index][vertex] < value[vertex]:
                    parent[vertex] = index  # update parent pointer
                    value[vertex] = self.matrix[index][vertex]  # and value

        # if any node doesn't have parent graph is disconnected
        if None in parent:
            return False
        return parent

    def print_prims_mst(self):
        parent = self.prims_mst()
        # check if graph is disconnected
        if not parent or None in parent:
            return False

        total_weight = 0
        for i in range(1, self.num_nodes):  # 0 vertex have no parent
            print('{} - {}: {}'.format(parent[i], i, self.matrix[i][parent[i]]))  # print edges and weights
            total_weight += self.matrix[i][parent[i]]
        print('Total weight: ', total_weight)
        return True

    def __str__(self):
        result = 'v: [(v, w), (v w),...]\n'
        for i in range(len(self.adj_list)):
            pairs = list(zip(self.adj_list[i], self.weight[i]))
            result += "{}: {}\n".format(i, pairs)
        return result

    def __repr__(self):
        return str(self)

