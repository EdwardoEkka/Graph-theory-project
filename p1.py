import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

as_df = pd.read_csv('as_info.csv')

# Load edge information
edge_df = pd.read_csv('edge_info.csv')

# Create an empty directed graph
G = nx.DiGraph()

# Add nodes to the graph
for _, row in as_df.iterrows():
    G.add_node(row['AS'], name=row['AS_Name'])

# Add edges to the graph
for _, row in edge_df.iterrows():
    G.add_edge(row['Source_AS'], row['Target_AS'], link_type=row['Link_Type'])

# Perform analysis
# For example, calculate centrality measures
centrality = nx.betweenness_centrality(G)

# Visualize the graph
plt.figure(figsize=(10, 8))
nx.draw(G, with_labels=True, node_size=500, font_size=10)
plt.title('Internet Topology Graph')
plt.show()
