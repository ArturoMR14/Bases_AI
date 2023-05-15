import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def objective_function(x):
    """
    Definición de la función objetivo
    """
    return x[0]**2 + x[1]**2

def local_search(initial_solution, n_iterations, step_size):
    """
    Implementación del método de búsqueda local
    """
    # Inicialización de la solución
    current_solution = initial_solution
    
    # Almacenamiento de los valores de la solución y la función objetivo en cada iteración
    solutions = [current_solution]
    objectives = [objective_function(current_solution)]
    
    for i in range(n_iterations):
        # Evaluación de la función objetivo en la solución actual
        current_objective = objective_function(current_solution)
        
        # Generación del vecindario utilizando el método de descenso del gradiente
        gradient = np.array([np.cos(current_solution[0]) - step_size, -np.sin(current_solution[1]) + 2 * current_solution[1] - step_size])
        neighbor = current_solution - step_size * gradient
        
        # Evaluación de la función objetivo en el vecindario generado
        neighbor_objective = objective_function(neighbor)
        
        # Actualización de la solución si se encuentra una mejor solución en el vecindario
        if neighbor_objective < current_objective:
            current_solution = neighbor
        
        # Almacenamiento de los valores de la solución y la función objetivo en cada iteración
        solutions.append(current_solution)
        objectives.append(current_objective)
    
    # Redondeo de la solución y la función objetivo a dos decimales
    current_solution = np.round(current_solution, decimals=2)
    current_objective = np.round(objective_function(current_solution), decimals=2)
    
    return current_solution, current_objective, solutions, objectives

# Ejemplo de uso del método de búsqueda local
initial_solution = np.array([300, 300])
n_iterations = 5
step_size = 0.1

best_solution, best_objective, solutions, objectives = local_search(initial_solution, n_iterations, step_size)

# Gráfico de la función objetivo y la solución encontrada
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Rango de los valores de las variables de la función objetivo
x_range = y_range = np.arange(-300, 300, 0.1)
X, Y = np.meshgrid(x_range, y_range)

# Valores de la función objetivo en cada punto del rango
Z = objective_function([X,Y])

# Gráfico de la superficie de la función objetivo
ax.plot_surface(X, Y, Z, cmap='winter', alpha=0.5)

# Gráfico de la trayectoria de la solución encontrada
solutions = np.array(solutions)
ax.plot(solutions[:,0], solutions[:,1], objectives, color='red', linewidth=2)

# Gráfico de los puntos clave en la trayectoria de la solución
for i in range(len(solutions)):
    if i == 0:
        # Punto inicial
        ax.scatter(solutions[i,0], solutions[i,1], objectives[i], s=5, color='blue')
    elif objectives[i] < objectives[i-1]:

        # Nuevo mínimo encontrado
        ax.scatter(solutions[i,0], solutions[i,1], objectives[i], s=5, color='red')
    else:
        # Solución actual
        ax.scatter(solutions[i,0], solutions[i,1], objectives[i], s=5, color='green')

# Gráfico de la mejor solución encontrada
ax.scatter(best_solution[0], best_solution[1], best_objective, s=5, color='black')

# Etiquetas de los ejes y el título del gráfico
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Función objetivo')
ax.set_title('Búsqueda local')

# Mostrar el gráfico
plt.show()