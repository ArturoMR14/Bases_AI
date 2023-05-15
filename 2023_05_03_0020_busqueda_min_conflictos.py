import random

# Ejemplo de CSP: tres variables con valores enteros entre 1 y 5
csp = {
    'A': [1, 2, 3],
    'B': [2, 3, 4],
    'C': [3, 4, 5],
}

# Restricciones: las variables no pueden tener el mismo valor
def not_equal(var1, var2):
    return var1 != var2

csp_constraints = {
    ('A', 'B'): not_equal,
    ('A', 'C'): not_equal,
    ('B', 'C'): not_equal,
}

# Función para comprobar si una asignación satisface todas las restricciones del CSP
def satisfied(assignment):
    for (var1, var2), constraint in csp_constraints.items():
        if var1 in assignment and var2 in assignment and not constraint(assignment[var1], assignment[var2]):
            return False
    return True

# Función para resolver el CSP utilizando la búsqueda local de mínimos conflictos
def min_conflicts(csp, max_steps=1000):
    # Inicializar una asignación aleatoria de valores a las variables del CSP
    assignment = {var: random.choice(csp[var]) for var in csp}

    # Iterar hasta que se encuentre una solución o se alcance el límite de iteraciones
    for i in range(max_steps):
        # Si la asignación actual satisface todas las restricciones, se ha encontrado una solución
        if satisfied(assignment):
            return assignment
    
        # Seleccionar una variable en conflicto al azar
        var = random.choice([v for v in csp if not satisfied({v: val for v, val in assignment.items() if v != var})])

        # Seleccionar un valor que minimice los conflictos con las variables adyacentes
        min_conflicts = min(csp[var], key=lambda val: sum(not satisfied({var: val, **assignment}) for var in csp if var != v))

        # Asignar el valor que minimiza los conflictos a la variable
        assignment[var] = min_conflicts

    # Si se alcanza el límite de iteraciones sin encontrar una solución, se devuelve None
    return None

# Ejecutar el algoritmo de búsqueda local de mínimos conflictos en el CSP de ejemplo
solution = min_conflicts(csp)

if solution:
    print("Solución encontrada:")
    print(solution)
else:
    print("No se ha encontrado solución en el número de iteraciones máximas permitidas.")
