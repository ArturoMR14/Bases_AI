import networkx as nx
import matplotlib.pyplot as plt
import random

def hill_climbing_search(graph, start_node, max_iterations=1000):
    current_node = start_node
    visited = set()
    path = [start_node]
    iteration = 0

    while iteration < max_iterations:
        visited.add(current_node)
        neighbors = list(graph.neighbors(current_node))
        random.shuffle(neighbors)
        next_node = None
        max_weight = -float("inf")

        for neighbor in neighbors:
            if neighbor not in visited:
                weight = graph[current_node][neighbor]['weight']
                if weight > max_weight:
                    max_weight = weight
                    next_node = neighbor

        if next_node is None:
            break

        current_node = next_node
        path.append(current_node)
        iteration += 1

    return path

def draw_graph(graph, path=None):
    pos = nx.spring_layout(graph)
    non_path_nodes = set(graph.nodes) - set(path)
    nx.draw(graph, pos, node_size=400, font_size=12, with_labels=True, node_color='blue')
    edge_labels = nx.get_edge_attributes(graph, 'weight')
    
    nx.draw_networkx_nodes(graph, pos, nodelist=non_path_nodes, node_color='lightblue', node_size=400)
    nx.draw_networkx_nodes(graph, pos, nodelist=[path[0]], node_color='green', node_size=400)
    nx.draw_networkx_nodes(graph, pos, nodelist=[path[-1]], node_color='red', node_size=400)
    nx.draw_networkx_nodes(graph, pos, nodelist=path[1:-1], node_color='yellow', node_size=400)

    nx.draw_networkx_labels(graph, pos=pos , labels={node: node for node in graph.nodes}, font_size=10, font_weight='bold')
    nx.draw_networkx_edge_labels(graph, pos=pos , edge_labels=edge_labels, font_size=10)
    nx.draw_networkx_edges(graph, pos=pos , edgelist=graph.edges, edge_color='black', width=1)

    if path:
        edges = [(path[i], path[i+1]) for i in range(len(path) - 1)]
        nx.draw_networkx_edges(graph, pos=pos , edgelist=edges, edge_color='red', width=2)

    plt.axis('off')
    plt.show()

# Ejemplo de uso:
weighted_edges = [
    ('A', 'B', 5), ('A', 'C', 6), ('B', 'D', 2), ('B', 'E', 3),
    ('C', 'F', 9), ('C', 'G', 1), ('D', 'H', 7), ('E', 'I', 8),
    ('F', 'J', 10), ('G', 'K', 4)
]

graph = nx.Graph()
graph.add_weighted_edges_from(weighted_edges)
start_node = 'B'

path = hill_climbing_search(graph, start_node)
print(f"El camino de la búsqueda de ascenso de colinas desde el nodo {start_node} es :   {path}")

draw_graph(graph, path)
