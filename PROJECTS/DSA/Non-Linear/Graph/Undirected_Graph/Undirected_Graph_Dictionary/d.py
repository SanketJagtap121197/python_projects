class Graph:
    def __init__(self):
        self.adj_list = {}  # Dictionary to store adjacency list

    def add_vertex(self, vertex):
        """Adds a vertex to the graph."""
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []

    def add_edge(self, vertex1, vertex2):
        """Adds an undirected edge between two vertices."""
        if vertex1 in self.adj_list and vertex2 in self.adj_list:
            self.adj_list[vertex1].append(vertex2)
            self.adj_list[vertex2].append(vertex1)  # Undirected edge

    def display(self):
        """Displays the adjacency list."""
        for vertex, neighbors in self.adj_list.items():
            print(f"{vertex} -> {neighbors}")

# Example usage:
graph = Graph()
graph.add_vertex("A")
graph.add_vertex("B")
graph.add_vertex("C")

graph.add_edge("A", "B")
graph.add_edge("A", "C")
graph.add_edge("B", "C")

graph.display()
