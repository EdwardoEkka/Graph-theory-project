import networkx as nx
import matplotlib.pyplot as plt
import csv

# Create a graph object
G = nx.Graph()

# Read edges, nodes, and weights from the CSV file
with open('test.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip the header row
    for row in reader:
        node1, node2, weight = row
        G.add_edge(node1, node2, weight=float(weight))

# Find minimum spanning tree
mst = nx.minimum_spanning_tree(G)

# Draw the original graph
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=700, node_color='skyblue', font_size=12, font_weight='bold')
edge_labels = nx.get_edge_attributes(G, 'weight')
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
