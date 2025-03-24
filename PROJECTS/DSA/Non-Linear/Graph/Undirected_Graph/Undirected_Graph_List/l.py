def add_edge(adj, i, j):
    adj[i].append(j)
    adj[j].append(i)  
    # Undirected graph
    # So, add an edge from j to i as well
    # Since, this is an undirected graph
    # If it was a directed graph, we would not add this line
    # And, the graph would be represented as a directed graph

def display_adj_list(adj):
    for i in range(len(adj)):
        print(f"{i}: ", end="")
        for j in adj[i]:
            print(j, end=" ")
        print()

# Create a graph with 4 vertices and no edges
V = 4
adj = [[] for _ in range(V)]

# Now add edges one by one
add_edge(adj, 0, 1)
add_edge(adj, 0, 2)
add_edge(adj, 1, 2)
add_edge(adj, 2, 3)

print("Adjacency List Representation:")
display_adj_list(adj)
