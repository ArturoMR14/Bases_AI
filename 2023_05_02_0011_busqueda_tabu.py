import random
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

def generate_tsp_problem_with_points(n, seed=42):
    random.seed(seed)
    points = [(random.uniform(0, 100), random.uniform(0, 100)) for _ in range(n)]

    distance_matrix = np.zeros((n, n))

    for i in range(n):
        for j in range(i+1, n):
            distance = round(np.sqrt((points[i][0] - points[j][0])**2 + (points[i][1] - points[j][1])**2))
            distance_matrix[i][j] = distance
            distance_matrix[j][i] = distance

    return points, distance_matrix

def tsp_objective_function(solution, distance_matrix):
    distance = 0
    for i in range(len(solution)-1):
        distance += distance_matrix[solution[i]][solution[i+1]]
    distance += distance_matrix[solution[-1]][solution[0]]
    return distance

def tabu_search(distance_matrix, iterations=1000, tabu_tenure=10):
    n = len(distance_matrix)
    current_solution = list(range(n))
    random.shuffle(current_solution)
    current_cost = tsp_objective_function(current_solution, distance_matrix)
    best_solution = current_solution[:]
    best_cost = current_cost

    tabu_list = set()

    for _ in range(iterations):
        candidates = []

        for i in range(n):
            for j in range(i + 1, n):
                if (i, j) not in tabu_list:
                    candidate = current_solution[:]
                    candidate[i], candidate[j] = candidate[j], candidate[i]
                    cost = tsp_objective_function(candidate, distance_matrix)
                    candidates.append((candidate, cost))

        candidates.sort(key=lambda x: x[1])
        next_solution, next_cost = candidates[0]

        tabu_list.add((current_solution.index(next_solution[0]), current_solution.index(next_solution[1])))
        if len(tabu_list) > tabu_tenure:
            tabu_list.pop()

        current_solution = next_solution
        current_cost = next_cost

        if current_cost < best_cost:
            best_solution = current_solution[:]
            best_cost = current_cost

    return best_solution, best_cost

def draw_tsp_solution_with_cost(points, solution, cost):
    G = nx.DiGraph()
    G.add_nodes_from(range(len(points)))

    for i in range(len(solution)-1):
        G.add_edge(solution[i], solution[i+1], weight=round(np.linalg.norm(np.array(points[solution[i]]) - np.array(points[solution[i+1]])), 2))
    G.add_edge(solution[-1], solution[0], weight=round(np.linalg.norm(np.array(points[solution[-1]]) - np.array(points[solution[0]])), 2))

    pos = {i: points[i] for i in range(len(points))}
    labels = {i: str(i) for i in range(len(points))}
    edge_labels = {(u, v): G[u][v]['weight'] for u, v in G.edges()}

    nx.draw(G, pos, node_color='lightblue', node_size=2000, with_labels=True, labels=labels, font_size=10, font_weight='bold', arrows=True, arrowsize=20)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10, bbox=dict(facecolor='white', edgecolor='none', pad=0.1))

    plt.text(0.5, 1.05, f"Costo: {cost}", horizontalalignment='center', verticalalignment='center', transform=plt.gca().transAxes, fontsize=12)

    plt.axis('equal')
    plt.show(block=False)
    plt.pause(2)
    plt.clf()
    
def draw_initial_graph(points):
    G = nx.Graph()
    G.add_nodes_from(range(len(points)))

    for i in range(len(points)):
        for j in range(i+1, len(points)):
            G.add_edge(i, j, weight=round(np.linalg.norm(np.array(points[i]) - np.array(points[j])), 2))

    pos = {i: points[i] for i in range(len(points))}
    labels = {i: str(i) for i in range(len(points))}
    edge_labels = {(u, v): G[u][v]['weight'] for u, v in G.edges()}

    nx.draw(G, pos, node_color='lightblue', node_size=2000, with_labels=True, labels=labels, font_size=10, font_weight='bold')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10, bbox=dict(facecolor='white', edgecolor='none', pad=0.1))

    plt.axis('equal')
    plt.title("Grafo inicial")
    plt.show(block=False)
    plt.pause(2)
    plt.clf()

# Ejemplo de uso:
n = 10
points, distance_matrix = generate_tsp_problem_with_points(n)
solution, optimal_cost = tabu_search(distance_matrix)

draw_initial_graph(points)


print(f"Solución óptima: {solution}")
print(f"Costo óptimo: {optimal_cost}")


# Generar una solución aleatoria y calcular su costo
random_solution = list(range(n))
random.shuffle(random_solution)
random_cost = tsp_objective_function(random_solution, distance_matrix)

print(f"Solución aleatoria: {random_solution}")
print(f"Costo aleatorio: {random_cost}")


draw_tsp_solution_with_cost(points, solution, optimal_cost)        #solucion optima 
draw_tsp_solution_with_cost(points, random_solution, random_cost)   #solucion random 