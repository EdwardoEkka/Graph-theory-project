import networkx as nx
import matplotlib.pyplot as plt
import csv

# Define nodes
G = nx.Graph()

# Read edges, nodes, and weights from the CSV file
with open('test.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip the header row
    for row in reader:
        node1, node2, weight = row
        G.add_edge(node1, node2, weight=int(weight))

# Define positions for nodes
pos = nx.spring_layout(G)

# Draw nodes
nx.draw_networkx_nodes(G, pos, node_size=500)

# Draw edges
nx.draw_networkx_edges(G, pos)

# Draw edge labels
edge_labels = nx.get_edge_attributes(G, 'weight')  # Retrieve edge labels from the graph
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

# Draw node labels
nx.draw_networkx_labels(G, pos)

# Show the plot
plt.title("Network Visualization")
plt.axis("off")
plt.show()
