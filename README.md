# Graphs

## Task 1

Create a graph using the NetworkX library to model a specific real-world network (e.g., a city's transportation network, a social network, or an internet topology).

> 📖 You can choose any real-world network at your discretion. If you cannot think of a realistic network, create a network that closely resembles reality.

Visualize the created graph and analyze its main characteristics (e.g., the number of nodes and edges, the degree of nodes).

## Task 2

Write a program that uses DFS and BFS algorithms to find paths in the graph developed in the first task.

Then, compare the results of both algorithms for this graph, highlighting the differences in the obtained paths. Explain why the paths differ for each algorithm.

## Task 3

Implement Dijkstra's algorithm to find the shortest path in the developed graph. Add weights to the edges in the graph and find the shortest path between all nodes in the graph.


## Завдання 1:

Проект моделює транспортну мережу міста за допомогою бібліотеки
NetworkX. Граф складається з шести районів міста, з'єднаних 7
маршрутами. 

Граф був створений з наступними вершинами та ребрами:

### Вершини

- Залізничний вокзал
- Торговий центр
- Парк
- Центр міста
- Спальний район
- Пляж

### Ребра

Залізничний вокзал - Торговий центр
Торговий центр - Парк
Парк - Центр міста
Центр міста - Спальний район
Спальний район - Пляж
Пляж - Залізничний вокзал
Залізничний вокзал - Центр міста

## Візуалізація

Граф був візуалізований за допомогою бібліотеки Matplotlib, щоб 
відобразити зв'язки між районами міста.

## Завдання 2:

### Реалізація алгоритмів

Були реалізовані два ключові алгоритми для знаходження шляхів у графі:

1. **Алгоритм пошуку в глибину (DFS)**:
   DFS працює за принципом глибокого обходу графа, де спочатку досліджуються всі вузли з найближчого виходу, а потім переходять до наступного.

2. **Алгоритм пошуку в ширину (BFS)**:
   BFS досліджує граф рівнями, починаючи з найближчих сусідів до початкової вершини та переходячи до більш віддалених.

### Результати виконання алгоритмів

```python
DFS Path: ['Залізничний вокзал', 'Центр міста', 'Спальний район', 'Пляж', 'Парк', 'Торговий центр']
BFS Path: ['Залізничний вокзал', 'Торговий центр', 'Пляж', 'Центр міста', 'Парк', 'Спальний район']
```

## Висновки

- **DFS** обирає шлях, який веде в глибину, і лише після цього повертається і
  розглядає інші можливості, що призводить до іншої послідовності відвідування
  вузлів у порівнянні з BFS.
- **BFS** обирає всі вузли на одному рівні перед переходом до наступного рівня,
  тому знаходить найкоротший шлях за кількістю ребер між початковою і кінцевою
  вершинами, якщо всі ребра мають однакову вагу.

## Завдання 3:

Було реалізовано алгоритм Дейкстри для знаходження найкоротшого шляху у графі з вагами. Граф було оновлено з вагами на ребра, які представляють відстань між районами міста.

## Висновки

- Алгоритм Дейкстри показує точні результати для всіх пар вершин у графі, враховуючи ваги ребер. Це дозволяє ефективно знаходити найкоротші шляхи між районами міста.
