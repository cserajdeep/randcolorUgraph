import matplotlib.pyplot as plt
import networkx as nx
import random

G = nx.gnp_random_graph(20,0.28)  #20 nodes with .28 (approx. 30% connections)
for u,v,d in G.edges(data=True):
    d['weight'] = random.random()
    print(d['weight'])

edges,weights = zip(*nx.get_edge_attributes(G,'weight').items())

pos = nx.spring_layout(G)
nx.draw(G, pos, node_color='r', edgelist=edges, edge_color=weights, width=6.0, edge_cmap=plt.cm.Greens, with_labels=True)
plt.savefig('edges.png')  #undirected graph saved as edges.png