import networkx as nx
import matplotlib.pyplot as plt

# Create a graph object
G = nx.Graph()

# Define nodes
nodes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
G.add_nodes_from(nodes)

# Define edges with weights
edges = [
    ('A', 'B', 5),
    ('A', 'C', 8),
    ('A', 'D', 6),
    ('B', 'E', 4),
    ('B', 'F', 7),
    ('C', 'G', 9),
    ('C', 'H', 3),
    ('D', 'I', 5),
    ('D', 'J', 10),
    ('E', 'F', 2),
    ('E', 'G', 6),
    ('F', 'H', 8),
    ('G', 'I', 4),
    ('H', 'J', 7)
]

# Add edges to the graph
for edge in edges:
    G.add_edge(edge[0], edge[1], weight=edge[2])

# Function to find shortest path and cost
def find_shortest_path_cost(source, destination):
    shortest_path = nx.shortest_path(G, source=source, target=destination, weight='weight')
    shortest_path_length = nx.shortest_path_length(G, source=source, target=destination, weight='weight')
    return shortest_path, shortest_path_length

# User input for source and destination nodes
source = input("Enter the source node: ")
destination = input("Enter the destination node: ")

# Find shortest path and cost
shortest_path, shortest_path_length = find_shortest_path_cost(source, destination)
print(f"\nShortest Path from {source} to {destination}: {' -> '.join(shortest_path)}")
print(f"Shortest Path Length: {shortest_path_length}")

# Create a new graph containing only the shortest path
H = G.subgraph(shortest_path)

# Define positions for nodes
pos = nx.spring_layout(H)

# Draw nodes
nx.draw_networkx_nodes(H, pos, node_size=500)

# Draw edges
nx.draw_networkx_edges(H, pos)

# Draw edge labels
edge_labels = {(edge[0], edge[1]): edge[2] for edge in edges if (edge[0], edge[1]) in H.edges()}
nx.draw_networkx_edge_labels(H, pos, edge_labels=edge_labels)

# Draw node labels
nx.draw_networkx_labels(H, pos)

# Show the plot
plt.title(f"Shortest Path from {source} to {destination}")
plt.axis("off")
plt.show()
