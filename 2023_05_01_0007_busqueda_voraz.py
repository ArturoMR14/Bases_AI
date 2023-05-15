from queue import PriorityQueue
import networkx as nx
import matplotlib.pyplot as plt

def manhattan_distance(a, b):
    return abs(ord(a) - ord(b))

def greedy_best_first_search(graph, start, goal):
    frontier = PriorityQueue()
    frontier.put((0, start, 0, []))
    explored = set()

    iteration = 0

    while not frontier.empty():
        _, current_node, current_cost, path = frontier.get()

        if current_node in explored:
            continue

        path = path + [current_node]
        explored.add(current_node)

        print(f"Iteration {iteration}: Visiting node {current_node}")
        iteration += 1

        if current_node == goal:
            return explored, path, current_cost

        for neighbor, edge_cost in graph[current_node].items():
            if neighbor not in explored:
                distance = manhattan_distance(neighbor, goal)
                total_cost = current_cost + edge_cost
                frontier.put((distance, neighbor, total_cost, path))

graph = {
    'A': {'B': 4, 'C': 8},
    'B': {'A': 4, 'D': 8, 'E': 11},
    'C': {'A': 8, 'F': 7, 'G': 4},
    'D': {'B': 8, 'H': 9, 'I': 14},
    'E': {'B': 11, 'J': 10},
    'F': {'C': 7, 'K': 4},
    'G': {'C': 4, 'L': 1},
    'H': {'D': 9, 'L': 1},
    'I': {'D': 14, },
    'J': {'E': 10},
    'K': {'F': 4},
    'L': {'G': 1},
}

G = nx.Graph()

for node in graph.keys():
    G.add_node(node)

for node, neighbors in graph.items():
    for neighbor, weight in neighbors.items():
        G.add_edge(node, neighbor, weight=weight)

start = 'A'
goal = 'L'
visited, path, cost = greedy_best_first_search(graph, start, goal)
print(f"Nodos visitados para ir desde el nodo {start} al nodo {goal}: {visited}")
print(f"Camino desde el nodo {start} al nodo {goal}: {path}")
print(f"Costo total para ir desde el nodo {start} al nodo {goal}: {cost}")

node_colors = {node: 'yellow' if node in path else 'blue' for node in G.nodes()}
node_colors[start] = 'green'
node_colors[goal] = 'red'

pos = nx.spring_layout(G)
nx.draw(G, pos, node_size=400, font_size=12, with_labels=True, node_color=[node_colors[node] for node in G.nodes()])
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=12)

plt.show()
