import networkx as nx
import matplotlib.pyplot as plt


G = nx.Graph()
stations = ["City A", "City B", "City C", "City D", "City E", "City F"]
G.add_nodes_from(stations)


edges = [
    ("City A", "City B"),
    ("City B", "City C"),
    ("City C", "City D"),
    ("City D", "City E"),
    ("City E", "City F"),
    ("City F", "City A"),
    ("City A", "City D"),
]


G.add_edges_from(edges)
pos = nx.circular_layout(G)


edge_labels = {
    ("City A", "City B"): "1",
    ("City B", "City C"): "2",
    ("City C", "City D"): "3",
    ("City D", "City E"): "4",
    ("City E", "City F"): "5",
    ("City F", "City A"): "6",
    ("City A", "City D"): "7",
}


nx.draw(
    G,
    pos,
    with_labels=True,
    node_color="yellow",
    node_size=2000,
    edge_color="blue",
    font_size=15,
    font_color="darkgreen",
)


nx.draw_networkx_edge_labels(
    G,
    pos,
    edge_labels=edge_labels,
    font_color="red",
    font_size=12,
)

plt.title("Схема транспортної мережі між містами з нумерацією ребер")
plt.show()


num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
degree_centrality = nx.degree_centrality(G)


print(f"Кількість вершин: {num_nodes}")
print(f"Кількість ребер: {num_edges}")
print("Ступінь вершин:")
for node, degree in degree_centrality.items():
    print(f"{node}: {degree:.2f}")