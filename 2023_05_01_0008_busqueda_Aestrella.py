import heapq
import math
import networkx as nx
import matplotlib.pyplot as plt

# Definir el grafo
graph = {
    'A': {'B': 5, 'C': 4, 'E': 3},
    'B': {'A': 5, 'C': 2, 'D': 4, 'F': 6},
    'C': {'A': 4, 'B': 2, 'D': 1, 'E': 7},
    'D': {'B': 4, 'C': 1, 'E': 2, 'F': 3, 'G': 5},
    'E': {'A': 3, 'C': 7, 'D': 2, 'H': 4},
    'F': {'B': 6, 'D': 3, 'G': 2, 'I': 6},
    'G': {'D': 5, 'F': 2, 'H': 3, 'J': 4},
    'H': {'E': 4, 'G': 3, 'I': 2, 'K': 5},
    'I': {'F': 6, 'H': 2, 'J': 3, 'L': 4},
    'J': {'G': 4, 'I': 3, 'K': 2, 'M': 5},
    'K': {'H': 5, 'J': 2, 'L': 3, 'N': 4},
    'L': {'I': 4, 'K': 3, 'M': 1, 'O': 5},
    'M': {'J': 5, 'L': 1, 'N': 2, 'P': 4},
    'N': {'K': 4, 'M': 2, 'O': 3, 'P': 1},
    'O': {'L': 5, 'N': 3, 'P': 2},
    'P': {'M': 4, 'N': 1, 'O': 2},
}

def get_neighbors(node):
    return graph[node].items()

def euclidean_distance(node1, node2):
    # No se usa en este caso
    return 0

def a_star(start, goal, neighbors_fn, heuristic_fn):
    frontier = [(0, start)]
    came_from = {}
    cost_so_far = {start: 0}
    iteration = 0

    while frontier:
        iteration += 1
        print(f"Iteration {iteration}: Exploring {frontier}")
        _, current = heapq.heappop(frontier)

        if current == goal:
            path = [current]
            while current in came_from:
                current = came_from[current]
                path.append(current)
            path.reverse()
            return path

        for neighbor, cost in neighbors_fn(current):
            new_cost = cost_so_far[current] + cost
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                priority = new_cost + heuristic_fn(neighbor, goal)
                heapq.heappush(frontier, (priority, neighbor))
                came_from[neighbor] = current

    return None

# Ejecutar la búsqueda A* y mostrar la ruta encontrada
start_node = 'A'
end_node = 'L'
path = a_star(start_node, end_node, get_neighbors, euclidean_distance)
# Calcular el costo total de la ruta encontrada
total_cost = 0
for i in range(len(path)-1):
    total_cost += graph[path[i]][path[i+1]]
print(f"Total cost: {total_cost}")

# Crear un objeto de grafo de NetworkX y añadir nodos y conexiones
graph_nx = nx.Graph()
for node in graph:
    graph_nx.add_node(node)
    for neighbor, cost in graph[node].items():
        graph_nx.add_edge(node, neighbor, weight=cost)

# Colorear los nodos según su estado
node_colors = []
for node in graph_nx.nodes:
    if node == start_node:
        node_colors.append('green')
    elif node == end_node:
        node_colors.append('red')
    elif node in path:
        node_colors.append('yellow')
    else:
        node_colors.append('gray')

# Dibujar el grafo con los nodos coloreados
pos = nx.spring_layout(graph_nx)
nx.draw(graph_nx, pos=pos, node_color=node_colors, with_labels=True, font_weight='bold')
edge_labels = nx.get_edge_attributes(graph_nx, 'weight')

# Mostrar las etiquetas de los bordes
nx.draw_networkx_edge_labels(graph_nx, pos=pos, edge_labels=edge_labels)

# Mostrar el grafo y la ruta más corta
plt.show()
