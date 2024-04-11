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

# Define positions for nodes
pos = nx.spring_layout(G)

# Draw nodes
nx.draw_networkx_nodes(G, pos, node_size=500)

# Draw edges
nx.draw_networkx_edges(G, pos)

# Draw edge labels
edge_labels = {(edge[0], edge[1]): edge[2] for edge in edges}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

# Draw node labels
nx.draw_networkx_labels(G, pos)

# Show the plot
plt.title("Network Visualization")
plt.axis("off")
plt.show()
