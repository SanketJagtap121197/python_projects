class DirectedGraph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, from_vertex, to_vertex):
        if from_vertex in self.graph and to_vertex in self.graph:
            self.graph[from_vertex].append(to_vertex)
        else:
            print("One or both vertices not found.")

    def display(self):
        for vertex, edges in self.graph.items():
            print(f"{vertex} -> {', '.join(map(str, edges))}")

# Example usage
g = DirectedGraph()
g.add_vertex(1)
g.add_vertex(2)
g.add_vertex(3)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 1)

g.display()
