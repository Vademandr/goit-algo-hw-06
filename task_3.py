import heapq
import networkx as nx
import matplotlib.pyplot as plt


G = nx.Graph()
stations = ["Залізничний вокзал", "Торговий центр", "Парк", "Центр міста", "Спальний район", "Пляж"]
G.add_nodes_from(stations)


edges = [
    ("Залізничний вокзал", "Торговий центр", 1),
    ("Торговий центр", "Парк", 2),
    ("Парк", "Центр міста", 1),
    ("Центр міста", "Спальний район", 3),
    ("Спальний район", "Пляж", 2),
    ("Пляж", "Залізничний вокзал", 4),
    ("Залізничний вокзал", "Центр міста", 5),
]

G.add_weighted_edges_from(edges)


def dijkstra(graph, start):
    distances = {node: float("infinity") for node in graph.nodes}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, attributes in graph[current_node].items():
            weight = attributes["weight"]
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


all_distances = {node: dijkstra(G, node) for node in G.nodes}


print("Найкоротші відстані між усіма парами вершин:")
for source in all_distances:
    for target in all_distances[source]:
        print(f"Від {source} до {target}: відстань {all_distances[source][target]}")


pos = nx.circular_layout(G)
nx.draw(
    G,
    pos,
    with_labels=True,
    node_color="lightgreen",
    node_size=2000,
    edge_color="blue",
    font_size=15,
    font_color="darkgreen",
)


edge_labels = {(u, v): f'{d["weight"]}' for u, v, d in G.edges(data=True)}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

plt.title("Схема транспортної мережі міста з вагами ребер")
plt.show()