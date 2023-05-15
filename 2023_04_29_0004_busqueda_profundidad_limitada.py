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
 
# Función para realizar búsqueda en profundidad limitada en el grafo
def DFS_Limited(graph, start, depth):
    visited = [False] * len(graph.adjList)
    stack = deque([(start, 0)])
 
    while stack:
        (vertex, level) = stack.pop()
 
        if not visited[vertex]:
            visited[vertex] = True
            print(vertex, end=' ')
            if level < depth:
                for neighbor in graph.adjList[vertex]:
                    stack.append((neighbor, level+1))
 
    return visited

G = nx.Graph() #create a graph
if __name__ == '__main__':
    # Lista de bordes de grafo
    edges = [
  (0, 1), (0, 2), (0, 3), (1, 4), (1, 5), (4, 8),
        (4, 9), (3, 6), (3, 7), (6, 10), (6, 11)
    ]
    G.add_nodes_from([0,1,2,3,4,5,6,7,8,9,10,11]) 
    G.add_edges_from([
  (0, 1), (0, 2), (0, 3), (1, 4), (1, 5), (4, 8),
        (4, 9), (3, 6), (3, 7), (6, 10), (6, 11)])
    # número total de nodos en el grafo
    n = 12
 
    # construye un grafo a partir de los bordes dados
    graph = Graph(edges, n)
 
    # realiza una búsqueda en profundidad limitada en el grafo con profundidad máxima de 2
    profundidad= 2
    visited = DFS_Limited(graph, 0, profundidad)
    
    #color los nodos que si han sido visitados
    node_colors = ["red" if visited[i] else "blue" for i in range(0, len(graph.adjList))]
    
    #grafica el grafo con los colores de nodos actualizados
    nx.draw(G, with_labels=True, font_weight='bold', node_color=node_colors)
    plt.show()
    plt.pause(3)
    plt.close