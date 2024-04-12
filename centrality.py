import networkx as nx
import matplotlib.pyplot as plt

# Define node and edge data
nodes_data = [
    (1, {"label": "Server A", "type": "Server"}),
    (2, {"label": "Router A", "type": "Router"}),
    (3, {"label": "Server B", "type": "Server"}),
    (4, {"label": "User Device", "type": "Device"}),
    (5, {"label": "Server C", "type": "Server"}),
    (6, {"label": "Router B", "type": "Router"}),
    (7, {"label": "Database Server", "type": "Server"}),
    (8, {"label": "Firewall", "type": "Firewall"}),
    (9, {"label": "Switch", "type": "Switch"})
]

edges_data = [
    (1, 2, {"edge_type": "Data Flow", "risk_level": "High"}),
    (2, 3, {"edge_type": "Data Flow", "risk_level": "Medium"}),
    (3, 4, {"edge_type": "Access", "risk_level": "Low"}),
    (1, 5, {"edge_type": "Data Flow", "risk_level": "Medium"}),
    (5, 6, {"edge_type": "Data Flow", "risk_level": "Low"}),
    (5, 7, {"edge_type": "Data Flow", "risk_level": "High"}),
    (6, 9, {"edge_type": "Data Flow", "risk_level": "High"}),
    (7, 4, {"edge_type": "Access", "risk_level": "Medium"}),
    (9, 4, {"edge_type": "Data Flow", "risk_level": "Low"}),
    (6, 8, {"edge_type": "Data Flow", "risk_level": "High"})
]

# Create a graph
G = nx.Graph()

# Add nodes to the graph
G.add_nodes_from(nodes_data)

# Add edges to the graph
G.add_edges_from(edges_data)

# Calculate centrality measures
degree_centrality = nx.degree_centrality(G)
closeness_centrality = nx.closeness_centrality(G)
betweenness_centrality = nx.betweenness_centrality(G)

# Print centrality measures
print("Degree Centrality:")
for node_id, centrality in degree_centrality.items():
    print(f"Node {node_id}: {centrality}")

print("\nCloseness Centrality:")
for node_id, centrality in closeness_centrality.items():
    print(f"Node {node_id}: {centrality}")

print("\nBetweenness Centrality:")
for node_id, centrality in betweenness_centrality.items():
    print(f"Node {node_id}: {centrality}")

# Visualize the graph
pos = nx.spring_layout(G)  # Positions for all nodes

# Draw nodes
nx.draw_networkx_nodes(G, pos, node_color='skyblue', node_size=700)

# Draw edges
nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.5)

# Draw labels
labels = {node[0]: node[1]['label'] for node in G.nodes(data=True)}
nx.draw_networkx_labels(G, pos, labels=labels, font_size=10, font_family='sans-serif')

# Draw edge labels
edge_labels = {(edge[0], edge[1]): edge[2]['edge_type'] for edge in G.edges(data=True)}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

plt.title("Network Graph")
plt.axis('off')
plt.show()
