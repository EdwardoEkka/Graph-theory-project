import networkx as nx
import matplotlib.pyplot as plt

# Create a directed graph
G = nx.DiGraph()

# Add nodes. In a real-world scenario, these might represent routers or switches.
G.add_node("A")
G.add_node("B")
G.add_node("C")
G.add_node("D")
G.add_node("E")

# Add edges with weights. In a real-world scenario, weights might represent latency, bandwidth, or other cost metrics.
G.add_edge("A", "B", weight=1)
G.add_edge("B", "C", weight=2)
G.add_edge("C", "D", weight=1)
G.add_edge("D", "E", weight=3)
G.add_edge("A", "D", weight=4)
G.add_edge("A", "C", weight=7)
G.add_edge("B", "E", weight=5)

# Draw the graph
pos = nx.spring_layout(G)  # positions for all nodes
nx.draw_networkx_nodes(G, pos)
nx.draw_networkx_edges(G, pos)
nx.draw_networkx_labels(G, pos)
nx.draw_networkx_edge_labels(G, pos, edge_labels=nx.get_edge_attributes(G, 'weight'))

# Display the graph
plt.show()

# Find the shortest path from A to E
shortest_path = nx.dijkstra_path(G, "A", "E")
print(f"The shortest path from A to E is: {shortest_path}")

# Simulate a failure by removing an edge
G.remove_edge("C", "D")

# Try to find a new shortest path
try:
    new_shortest_path = nx.dijkstra_path(G, "A", "E")
    print(f"After a failure, the new shortest path from A to E is: {new_shortest_path}")
except nx.NetworkXNoPath:
    print("After a failure, there is no path from A to E.")

# Analyze the resilience by checking the number of connected components
print(f"The graph has {nx.number_weakly_connected_components(G)} weakly connected component(s).")

# If the graph is not strongly connected, we can check the resilience by finding alternative paths
if not nx.is_strongly_connected(G):
    print("The network is not strongly connected, indicating potential resilience issues.")