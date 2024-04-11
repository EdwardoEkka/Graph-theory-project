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

# Find minimum spanning tree
mst = nx.minimum_spanning_tree(G)

# Draw the original graph
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=700, node_color='skyblue', font_size=12, font_weight='bold')
edge_labels = {(edge[0], edge[1]): edge[2] for edge in edges}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.title('Original Network')

# Draw the minimum spanning tree
plt.subplot(1, 2, 2)
pos_mst = nx.spring_layout(mst)
nx.draw(mst, pos_mst, with_labels=True, node_size=700, node_color='lightgreen', font_size=12, font_weight='bold')
nx.draw_networkx_edge_labels(mst, pos_mst, edge_labels=edge_labels)
plt.title('Minimum Spanning Tree Network')

# Show the plot
plt.tight_layout()
plt.show()
