import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
graph = {"South Station": ["Central Station", "Dorchester"],
    "Dorchester": ["South Station", "Quincy"],
    "Quincy": ["Dorchester", "Braintree", "Weymouth"],
    "Braintree": ["Quincy", "South Weymouth", "Randolph"],
    "Weymouth": ["Quincy", "Hingham"],
    "South Weymouth": ["Braintree", "North Abington", "Rockland"],
    "Randolph": ["Braintree", "Stoughton", "Avon"],
    "North Station": ["Central Station", "Cambridge", "Somerville", "Malden", "Everett"],
    "East Station": ["Central Station", "Chelsea", "Lynn"],
    "Cambridge": ["Belmont", "North Station"],
    "Belmont": ["Cambridge", "Waltham"],
    "Waltham": ["Belmont", "Watertown"]
}
def generate_edges(graph):
    edges = []
    for node in graph:
        for neighbour in graph[node]:
            edges.append((node, neighbour))

    return edges

edges = generate_edges(graph)

G.add_edges_from(edges)
nx.draw(G)
plt.show()
