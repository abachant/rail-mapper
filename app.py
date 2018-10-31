import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('CommuterRailStationLineOrdering.csv')

graph = {}

for i in range(len(df)):
    if df.iloc[i].stop_id not in graph:
        graph[df.iloc[i].stop_id] = []

    if i != len(df)-1:
        if df.iloc[i+1].route_long_name == df.iloc[i].route_long_name and df.iloc[i+1].stop_id not in graph[df.iloc[i].stop_id] and df.iloc[i+1].stop_id != df.iloc[i].stop_id:
            graph[df.iloc[i].stop_id].append(df.iloc[i+1].stop_id)
        else:
            pass
    if i !=0:
        if df.iloc[i-1].route_long_name == df.iloc[i].route_long_name and df.iloc[i-1].stop_id not in graph[df.iloc[i].stop_id] and df.iloc[i-1].stop_id != df.iloc[i].stop_id:
            graph[df.iloc[i].stop_id].append(df.iloc[i-1].stop_id)
        else:
            pass

print(graph)

G = nx.Graph()
# graph = {"South Station": ["Central Station", "Dorchester"],
#     "Dorchester": ["South Station", "Quincy"],
#     "Quincy": ["Dorchester", "Braintree", "Weymouth"],
#     "Braintree": ["Quincy", "South Weymouth", "Randolph"],
#     "Weymouth": ["Quincy", "Hingham"],
#     "Hingham": ["Weymouth", "Cohasset"],
#     "Cohasset": ["Hingham", "North Scituate"],
#     "North Scituate": ["Cohasset", "Scituate"],
#     "Scituate": ["North Scituate", "Greenbush"],
#     "Greenbush": ["Scituate", "Marshfield Hills"],
#     "Marshfield Hills": ["Greenbush", "Marshfield"],
#     "Marshfield": ["Marshfield Hills", "Duxbury"],
#     "South Weymouth": ["Braintree", "North Abington", "Rockland"],
#     "Randolph": ["Braintree", "Stoughton", "Avon"],
#     "North Station": ["Central Station", "Cambridge", "Somerville", "Malden", "Everett"],
#     "East Station": ["Central Station", "Chelsea", "Lynn"],
#     "Cambridge": ["Belmont", "North Station"],
#     "Belmont": ["Cambridge", "Waltham"],
#     "Waltham": ["Belmont", "Watertown"]
# }

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
