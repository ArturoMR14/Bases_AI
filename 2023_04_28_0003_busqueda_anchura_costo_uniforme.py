from queue import PriorityQueue
import networkx as nx
import matplotlib.pyplot as plt

def uniform_cost_search(graph, start, goal):

    frontier = PriorityQueue()  # cola de prioridad
    frontier.put((0, start))  # añade el nodo de inicio con un costo acumulado de 0
    explored = set()  # conjunto de nodos ya visitados
    
    while not frontier.empty():  # mientras la cola de prioridad no esté vacía
        cost, current_node = frontier.get()  # extrae el nodo con el menor costo acumulado
        if current_node == goal:  # si es el nodo de destino, se retorna el costo acumulado
            return cost
        
        explored.add(current_node)  # marca el nodo como visitado
        
        
        for neighbor, neighbor_cost in graph[current_node].items():  # expande los vecinos
            if neighbor not in explored:  # si el vecino no ha sido visitado
                frontier.put((cost + neighbor_cost, neighbor))  # añade el vecino a la cola de prioridad con su costo acumulado
        print(explored)        
    return None  # si el algoritmo ha recorrido todo el grafo sin encontrar el nodo de destino, retorna None

    
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
cost = uniform_cost_search(graph, start, goal)
print("costo optimo para recorrer del nodo " + start + " yendo al nodo " + goal + " = " + str(cost))  
# imprime el costo del camino más corto

# dibuja el grafo
node_colors = {start: 'green', goal: 'red'}

# dibuja el grafo con los nodos de inicio y destino resaltados
pos = nx.spring_layout(G)
nx.draw(G, pos, node_size=400, font_size=12, with_labels=True, node_color=[node_colors.get(node, 'blue') for node in G.nodes()])
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=12)

plt.show()
