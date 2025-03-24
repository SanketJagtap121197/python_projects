def dfs(graph, node, visited):
    # If the node has already been visited, return
    # Otherwise, print the node and add it to the visited set
    # Then, recursively call dfs on each neighbor of the node
    # This will ensure that all nodes reachable from the starting node are visited
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neighbor in graph[node]: # graph[node] returns a list of neighbors of the node
            dfs(graph, neighbor, visited)  # Recursively call dfs on the neighbor

# Example usage
graph = {1: [2], 2: [3], 3: [1]} # A directed graph represented as an adjacency list dictionary
visited = set() # A set to keep track of visited nodes
print("DFS Traversal:")
dfs(graph, 1, visited)
