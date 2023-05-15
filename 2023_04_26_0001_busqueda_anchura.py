import networkx as nx
import matplotlib.pyplot as plt
from collections import deque
 
# hacemos una clase para representar un objeto grafo
class Graph:
    # Constructor
    def __init__(self, edges, n):
 
        # Una lista de listas para representar una lista de adyacencia
        self.Lista_adyacencias = [ [] for _ in range(n)] #crea una lista vacía para cada uno de los nodos en el rango de 0 a n-1.
 
        # Agrega bordes al grafo no dirigido
        for (nodo_a, nodo_b) in edges:
            self.Lista_adyacencias[nodo_a].append(nodo_b)
            self.Lista_adyacencias[nodo_b].append(nodo_a)
            # En la lista de bordes, el método agrega al "nodo_b" a la lista de adyacencia del "nodo_a " 
            # y agrega el "nodo_a" a la lista de adyacencia del nodo_b. 
            # De esta manera, se crean conexiones bidireccionales entre los nodos en el grafo no dirigido
 
 
    # Realiza al metodo busqueda por anchura 
def anchura(grafo, nodo_inicio):
    
    # Crea una cola para almacenar los nodos que se deben visitar
    queue = deque([nodo_inicio])

    # Para realizar un seguimiento de si se visitó un nodo o no
    visitado = [False] * len(grafo.Lista_adyacencias)
    visitado[nodo_inicio] = True

    # Crea un grafo vacío para visualizar el proceso
    G = nx.Graph()
    
    # Agrega los nodos y bordes al grafo
    for i in range(len(grafo.Lista_adyacencias)):
        G.add_node(i)
        for j in grafo.Lista_adyacencias[i]:
            G.add_edge(i, j)
            
    # Colorea el nodo de inicio de rojo
    color_nodos = ['red' if i == nodo_inicio else 'blue' for i in range(len(grafo.Lista_adyacencias))]

    # Dibuja el grafo original
    pos = nx.spring_layout(G, seed=42)
    nx.draw(G, pos, node_color=color_nodos, with_labels=True, font_color='black',font_weight='bold')
    plt.show(block=False)
    plt.pause(1)
    plt.clf()

    # Mientras haya nodos en la cola, sigue explorando
    while queue:
        # Saca un nodo de la cola
        nodo = queue.popleft()
        print(f"iteracion: {nodo}")
        print(f"Visitando el nodo {nodo}")
        # Recorre los nodos adyacentes
        for nodo_adyacente in grafo.Lista_adyacencias[nodo]:
            # Si un nodo no ha sido visitado, marca como visitado y agregalo a la cola
            if not visitado[nodo_adyacente]:
                visitado[nodo_adyacente] = True
                queue.append(nodo_adyacente)

                # Colorea el nodo visitado de verde
                color_nodos[nodo_adyacente] = 'green'

                # Dibuja el grafo actualizado
                pos = nx.spring_layout(G, seed=42)
                nx.draw(G, pos, node_color=color_nodos, with_labels=True, font_color='white', font_weight='bold') 
                plt.show(block=False)
                plt.pause(2)
                plt.clf()

 
if __name__ == '__main__':
    # Lista de bordes de graph según el diagrama anterior
    edges = [(0, 1), (0, 2), (0, 3), (1, 4), (1, 5), (4, 8),(4, 9), (3, 6), (3, 7), (6, 10), (6, 11)]

    # número total de nodos en el graph
    n = 12

    # construye un graph a partir de los bordes dados
    graph = Graph(edges, n)

    # Realiza BFS a partir del vértice 0
    anchura(graph, 0)