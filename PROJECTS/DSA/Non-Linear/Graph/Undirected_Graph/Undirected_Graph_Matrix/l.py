def add_edge(mat, i, j):
  
    # Add an edge between two vertices
    mat[i][j] = 1  # Edge from i to j
    mat[j][i] = 1  # Edge from j to i
    # Graph is undirected, so we add edges in both directions (i to j and j to i) 

def display_matrix(mat):
  
    # Display the adjacency matrix
    for row in mat:
        print(" ".join(map(str, row)))
        # .join() method joins all items in a tuple into a single string with a space separator
        # map() function applies str() to all items in a list
        # str() function converts a number or boolean to a string
        # The above line prints each row of the matrix as a string with elements separated by a space   

# Main function to run the program
if __name__ == "__main__":
    v = 4  # Number of vertices
    # Create an empty adjacency matrix
    # v is the number of vertices in the graph
    mat = [[0] * v for _ in range(v)]  

    # Add edges to the graph
    # The graph is undirected, so we add edges in both directions
    # For example, an edge from vertex 0 to vertex 1 is also an edge from vertex 1 to vertex 0
    # The add_edge() function adds an edge between two vertices
    add_edge(mat, 0, 1)
    add_edge(mat, 0, 2)
    add_edge(mat, 1, 2)
    add_edge(mat, 2, 3)

    # Optionally, initialize matrix directly
    """
    mat = [
        [0, 1, 0, 0],
        [1, 0, 1, 0],
        [0, 1, 0, 1],
        [0, 0, 1, 0]
    ]
    """

    # Display adjacency matrix
    print("Adjacency Matrix:")
    display_matrix(mat)
