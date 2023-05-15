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
 
# Función auxiliar para realizar DFS en un nodo
def DFSUtil(graph, v, visited):
    # Marcar el nodo actual como visitado y mostrarlo
    visited[v] = True
    print(v, end=' ')
 
    # Recurrir para todos los nodos adyacentes no visitados
    for i in graph.adjList[v]:
        if not visited[i]:
            DFSUtil(graph, i, visited)
 
# Función para realizar DFS en el grafo
def DFS(graph):
    # Crea una lista de booleanos para realizar un seguimiento de los nodos visitados
    visited = [False] * len(graph.adjList)
 
    # Realiza una llamada a la función de utilidad recursiva para todos los nodos no visitados
    for i in range(len(graph.adjList)):
        if not visited[i]:
            DFSUtil(graph, i, visited)
G = nx.Graph() #create a graph
if __name__ == '__main__':
    # Lista de bordes de grafo
    edges = [
  (0, 1), (0, 2), (0, 3), (1, 4), (1, 5), (4, 8),
        (4, 9), (3, 6), (3, 7), (6, 10), (6, 11)
    ]
    G.add_nodes_from([1,2,3,4,5,6,7,8,9,10,11]) 
    G.add_edges_from([
  (0, 1), (0, 2), (0, 3), (1, 4), (1, 5), (4, 8),
        (4, 9), (3, 6), (3, 7), (6, 10), (6, 11)])
    # número total de nodos en el grafo
    n = 12
 
    # construye un grafo a partir de los bordes dados
    graph = Graph(edges, n)
 
    # realiza una búsqueda en profundidad (DFS) en el grafo
    DFS(graph)
    pos = nx.spring_layout(G, seed=42)
    nx.draw(G, pos, node_color="blue", with_labels=True, font_color='black', font_weight='bold')

    plt.show()