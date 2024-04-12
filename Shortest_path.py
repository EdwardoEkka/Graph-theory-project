import networkx as nx
import matplotlib.pyplot as plt
import csv

# Create a graph object
G = nx.Graph()

# Read edges with weights from the CSV file
with open('test.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip the header row
    for row in reader:
        node1, node2, weight = row
        G.add_edge(node1, node2, weight=float(weight))

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
edge_labels = nx.get_edge_attributes(H, 'weight')
nx.draw_networkx_edge_labels(H, pos, edge_labels=edge_labels)

# Draw node labels
nx.draw_networkx_labels(H, pos)

# Show the plot
plt.title(f"Shortest Path from {source} to {destination}")
plt.axis("off")
plt.show()
