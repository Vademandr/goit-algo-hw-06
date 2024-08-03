import networkx as nx
import matplotlib.pyplot as plt


G = nx.Graph()
stations = ["Залізничний вокзал", "Торговий центр", "Парк", "Центр міста", "Спальний район", "Пляж"]
G.add_nodes_from(stations)


edges = [
    ("Залізничний вокзал", "Торговий центр"),
    ("Торговий центр", "Парк"),
    ("Парк", "Центр міста"),
    ("Центр міста", "Спальний район"),
    ("Спальний район", "Пляж"),
    ("Пляж", "Залізничний вокзал"),
    ("Залізничний вокзал", "Центр міста"),
]


G.add_edges_from(edges)
pos = nx.circular_layout(G)


edge_labels = {
    ("Залізничний вокзал", "Торговий центр"): "1",
    ("Торговий центр", "Парк"): "2",
    ("Парк", "Центр міста"): "3",
    ("Центр міста", "Спальний район"): "4",
    ("Спальний район", "Пляж"): "5",
    ("Пляж", "Залізничний вокзал"): "6",
    ("Залізничний вокзал", "Центр міста"): "7",
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

plt.title("Схема транспортної мережі міста з нумерацією ребер")
plt.show()


num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
degree_centrality = nx.degree_centrality(G)


print(f"Кількість вершин: {num_nodes}")
print(f"Кількість ребер: {num_edges}")
print("Ступінь вершин:")
for node, degree in degree_centrality.items():
    print(f"{node}: {degree:.2f}")