
from queue import PriorityQueue

class Graph:
    def __init__(self, num_of_vertices):
        self.v = num_of_vertices
        self.edges = [[-1 for i in range(num_of_vertices)] for j in range(num_of_vertices)]
        self.visited = []

    def add_edge(self, u, v, weight):
        self.edges[u][v] = weight
        self.edges[v][u] = weight


def get_puz(demo=True):
    puz = []
    if demo:
        file = open("input17_demo.txt")
    else:
        file = open("input17.txt")
    for line in file:
        puz.append(list(line.replace('\n', '')))

    return puz

puz = get_puz()

g = Graph(13*13)

# Fill the graph with values from the matrix
for i in range(13):
    for j in range(13):
        if puz[i][j] != '0':
            g.add_edge(i, j, int(puz[i][j]))


g

def dijkstra(graph, start_vertex):
    D = {v:float('inf') for v in range(graph.v)}
    D[start_vertex] = 0

    pq = PriorityQueue()
    pq.put((0, start_vertex))

    while not pq.empty():
        (dist, current_vertex) = pq.get()
        graph.visited.append(current_vertex)

        for neighbor in range(graph.v):
            if graph.edges[current_vertex][neighbor] != -1:
                distance = graph.edges[current_vertex][neighbor]
                if neighbor not in graph.visited:
                    old_cost = D[neighbor]
                    new_cost = D[current_vertex] + distance
                    if new_cost < old_cost:
                        pq.put((new_cost, neighbor))
                        D[neighbor] = new_cost
    return D

dijkstra(g, 0)