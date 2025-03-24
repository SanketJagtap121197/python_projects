class DirectedGraphMatrix:
    def __init__(self, size):
        self.size = size
        self.graph = [[0] * size for _ in range(size)]

    def add_edge(self, from_vertex, to_vertex):
        self.graph[from_vertex][to_vertex] = 1  # Directed edge

    def display(self):
        for row in self.graph:
            print(row)

# Example usage
g = DirectedGraphMatrix(3)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 0)

g.display()
