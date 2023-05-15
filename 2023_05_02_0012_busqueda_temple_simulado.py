import random
import math
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

def simulated_annealing(distance_matrix, initial_temperature=1000, cooling_rate=0.995, min_temperature=1e-3, max_iterations=1000):
    n = len(distance_matrix)
    current_solution = list(range(n))
    random.shuffle(current_solution)
    current_cost = tsp_objective_function(current_solution, distance_matrix)

    best_solution = current_solution[:]
    best_cost = current_cost

    temperature = initial_temperature

    for _ in range(max_iterations):
        while temperature > min_temperature:
            i, j = random.sample(range(n), 2)
            candidate_solution = current_solution[:]
            candidate_solution[i], candidate_solution[j] = candidate_solution[j], candidate_solution[i]

            candidate_cost = tsp_objective_function(candidate_solution, distance_matrix)

            cost_diff = candidate_cost - current_cost
            if cost_diff < 0 or random.random() < math.exp(-cost_diff / temperature):
                current_solution = candidate_solution
                current_cost = candidate_cost

                if current_cost < best_cost:
                    best_solution = current_solution[:]
                    best_cost = current_cost

            temperature *= cooling_rate

    return best_solution, best_cost

def draw_initial_graph(points, distance_matrix):
    G = nx.Graph()
    G.add_nodes_from(range(len(points)))

    for i in range(len(points)):
        for j in range(i+1, len(points)):
            G.add_edge(i, j, weight=distance_matrix[i][j])

    pos = {i: points[i] for i in range(len(points))}
    labels = {i: str(i) for i in range(len(points))}
    edge_labels = {(u, v): G[u][v]['weight'] for u, v in G.edges()}

    nx.draw(G, pos, node_color='lightblue', node_size=2000, with_labels=True, labels=labels, font_size=10, font_weight='bold')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10, bbox=dict(facecolor='white', edgecolor='none', pad=0.1))

    plt.axis('equal')
    plt.title("Grafo inicial TSP")
    plt.show(block=False)
    plt.pause(2)
    plt.clf()


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

    plt.axis('equal')
    plt.title(f"Solución TSP - Costo: {cost}")
    plt.show(block=False)
    plt.pause(2)
    plt.clf()


# Ejemplo de uso:
n = 10
points, distance_matrix = generate_tsp_problem_with_points(n)

# Dibujar grafo inicial
draw_initial_graph(points, distance_matrix)

# Resolver TSP con Temple Simulado
solution, cost = simulated_annealing(distance_matrix)

print(f"Solución: {solution}")
print(f"Costo: {cost}")

# Dibujar solución y costo
draw_tsp_solution_with_cost(points, solution, cost)