from queue import PriorityQueue
import networkx as nx
import matplotlib.pyplot as plt


def bidirectional_search(graph, start, goal):
    # Frontera del inicio y del fin
    forward_frontier = PriorityQueue()
    backward_frontier = PriorityQueue()
    forward_frontier.put((0, start))
    backward_frontier.put((0, goal))

    # Nodos explorados del inicio y del fin
    forward_explored = set()
    backward_explored = set()

    # Padres de cada nodo en el camino óptimo del inicio y del fin
    forward_parents = {start: None}
    backward_parents = {goal: None}

    # Nodo donde se produce la intersección entre los dos caminos
    intersection_node = None

    # Iteración de la búsqueda bidireccional
    iteration = 0

    while not forward_frontier.empty() and not backward_frontier.empty():
        iteration += 1

        # Exploración hacia adelante
        forward_cost, current_node = forward_frontier.get()
        forward_explored.add(current_node)

        # Comprueba si se ha encontrado un camino óptimo
        if current_node in backward_explored:
            intersection_node = current_node
            break

        for neighbor, neighbor_cost in graph[current_node].items():
            # Si el vecino no ha sido visitado todavía, añádelo a la frontera
            if neighbor not in forward_explored and neighbor not in forward_parents:
                forward_frontier.put((forward_cost + neighbor_cost, neighbor))
                forward_parents[neighbor] = current_node

        # Exploración hacia atrás
        backward_cost, current_node = backward_frontier.get()
        backward_explored.add(current_node)

        # Comprueba si se ha encontrado un camino óptimo
        if current_node in forward_explored:
            intersection_node = current_node
            break

        for neighbor, neighbor_cost in graph[current_node].items():
            # Si el vecino no ha sido visitado todavía, añádelo a la frontera
            if neighbor not in backward_explored and neighbor not in backward_parents:
                backward_frontier.put((backward_cost + neighbor_cost, neighbor))
                backward_parents[neighbor] = current_node
                

        # Imprime información de depuración
        print(f"Iteración {iteration}")
        print(f"Nodos visitados en dirección hacia adelante: {forward_explored}")
        print(f"Nodos visitados en dirección hacia atrás: {backward_explored}")

    # No se ha encontrado camino óptimo
    if not intersection_node:
        return None

    # Construye el camino óptimo
    path = []
    current_node = intersection_node

    while current_node is not None:
        path.append(current_node)
        current_node = forward_parents.get(current_node, None)

    path.reverse()
    current_node = backward_parents.get(intersection_node, None)

    while current_node is not None:
        path.append(current_node)
        current_node = backward_parents.get(current_node, None)

    return path


graph = {
    'A': {'B': 4, 'H': 8},
    'B': {'A': 4, 'C': 8, 'H': 11},
    'C': {'B': 8, 'D': 7, 'F': 4, 'I': 2},
    'D': {'C': 7, 'E': 9, 'F': 14},
    'E': {'D': 9, 'F': 10},
    'F': {'C': 4, 'D': 14, 'E': 10, 'G': 2},
    'G': {'F': 2, 'H': 1, 'I': 6},
    'H': {'A': 8, 'B': 11, 'G': 1, 'I': 7},
    'I': {'C': 2, 'G': 6, 'H': 7},
}

G = nx.Graph()  # crea un grafo vacío

# añade los nodos
for node in graph.keys():
    G.add_node(node)

# añade las aristas con sus pesos
for node, neighbors in graph.items():
    for neighbor, weight in neighbors.items():
        G.add_edge(node, neighbor, weight=weight)

start = 'A'
goal = 'E'
path = bidirectional_search(graph, start, goal)
print("El recorrido óptimo del nodo " + start + " al nodo " + goal + " es igual al siguiente recorrido: " + str(path))

# actualiza el diccionario de colores de nodos para resaltar el recorrido óptimo en amarillo

node_colors = {node: 'blue' for node in G.nodes()}
# Si se ha encontrado un camino óptimo, asigna el color amarillo a los nodos que están en el camino
if path is not None:
    for node in path:
        node_colors[node] = 'yellow'

node_colors[start] = 'green'
node_colors[goal] = 'red'

# dibuja el grafo con los nodos de inicio y destino resaltados
pos = nx.spring_layout(G)
nx.draw(G, pos, node_size=400, font_size=12, with_labels=True, node_color=[node_colors[node] for node in G.nodes()])
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=12)

plt.show()
