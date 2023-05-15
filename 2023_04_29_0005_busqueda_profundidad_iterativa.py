from collections import deque
from pyvis.network import Network
import networkx as nx
import matplotlib.pyplot as plt
 
class Graph:
    # Constructor
    def __init__(self, edges, n):
 
        # Una lista de listas para representar una lista de adyacencia
        self.adjList = [[] for _ in range(n)]
 
        # agrega bordes al grafo no dirigido
        for (src, dest) in edges:
            self.adjList[src].append(dest)
            self.adjList[dest].append(src)
 
# Función para realizar DFS en el grafo de manera iterativa
def DFS_iterative(graph, start):
    # Crea una lista de booleanos para realizar un seguimiento de los nodos visitados
    visited = [False] * len(graph.adjList)
    # Crea una pila para la búsqueda DFS
    stack = []
    # Agrega el nodo inicial a la pila y marca como visitado
    stack.append(start)
    visited[start] = True
    # Crea un diccionario para almacenar el color de cada nodo
    colors = {}
    colors[start] = 'red'
    # Inicializa el contador de iteraciones
    iteration = 0
    # Itera mientras la pila no esté vacía
    while stack:
        # Incrementa el contador de iteraciones
        iteration += 1
        # Obtiene el siguiente nodo de la pila
        current_node = stack.pop()
        # Imprime el nodo actual y la iteración en la que se encuentra
        print(f"Iteration {iteration}, Visiting Node {current_node}")
        colors[current_node] = 'red'
        # Recorre los nodos adyacentes no visitados
        for neighbor in graph.adjList[current_node]:
            if not visited[neighbor]:
                # Agrega el nodo adyacente a la pila y marca como visitado
                stack.append(neighbor)
                visited[neighbor] = True
                # Asigna un color diferente al nodo visitado
                colors[neighbor] = 'green'
                
        # Dibuja el grafo con los nodos visitados de otro color
        pos = nx.spring_layout(G, seed=42)
        nx.draw(G,pos, with_labels=True, font_weight='bold', node_color=[colors.get(node, 'blue') for node in G.nodes()])
        plt.show(block=False)
        plt.pause(3)
        plt.clf()
 
# Crea el grafo con NetworkX
G = nx.Graph()
edges = ([
  (0, 1), (0, 2), (0, 3), (1, 4), (1, 5), (4, 8),
        (4, 9), (3, 6), (3, 7), (6, 10), (6, 11)])
    
G.add_nodes_from([1,2,3,4,5,6,7,8,9,10,11]) 
G.add_edges_from([(0, 1), (0, 2), (0, 3), (1, 4), (1, 5), (4, 8), (4, 9), (3, 6), (3, 7), (6, 10), (6, 11)])
# número total de nodos en el grafo

n=12

# Crea un grafo a partir de los bordes dados
graph = Graph(edges, n)
 
# Realiza una búsqueda en profundidad (DFS) iterativa en el grafo a partir del nodo 0
DFS_iterative(graph, start=0)

# Dibuja el grafo
pos = nx.spring_layout(G, seed=42)
nx.draw(G,pos, with_labels=True, font_weight='bold' )
plt.show()
plt.close