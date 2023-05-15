import pygame

class MapColoringCSP:
    def __init__(self, variables, domains, neighbors, constraints):
        self.variables = variables
        self.domains = {var: list(domain) for var, domain in domains.items()}
        self.neighbors = neighbors
        self.constraints = constraints

    def is_consistent(self, var, value):
        for neighbor in self.neighbors[var]:
            if len(self.domains[neighbor]) == 1 and self.domains[neighbor][0] == value:
                return False
        return True

    def assign(self, var, value):
        self.domains[var] = [value]

    def unassign(self, var):
        self.domains[var] = self.original_domains[var]

    def infer(self, var, value):
        inferences = []
        for neighbor in self.neighbors[var]:
            if value in self.domains[neighbor]:
                if len(self.domains[neighbor]) == 1:
                    return None
                self.domains[neighbor].remove(value)
                inferences.append((neighbor, value))
        return inferences

def ac3(csp, queue):
    while queue:
        xi, xj = queue.pop(0)
        if revise(csp, xi, xj):
            if len(csp.domains[xi]) == 0:
                return False
            for xk in csp.neighbors[xi]:
                if xk != xj:
                    queue.append((xk, xi))
    return True

def revise(csp, xi, xj):
    revised = False
    for x in csp.domains[xi][:]:
        if not any([csp.constraints(xi, x, xj, y) for y in csp.domains[xj]]):
            csp.domains[xi].remove(x)
            revised = True
    return revised

def select_unassigned_variable(csp):
    for var in csp.variables:
        if len(csp.domains[var]) > 1:
            return var
    return None

def backtrack(csp):
    if all(len(csp.domains[var]) == 1 for var in csp.variables):
        return csp.domains

    var = select_unassigned_variable(csp)
    for value in csp.domains[var]:
        if csp.is_consistent(var, value):
            csp.assign(var, value)
            inferences = csp.infer(var, value)
            if inferences is not None:
                visualize_process(csp, var)
                result = backtrack(csp)
                if result:
                    return result
            csp.unassign(var)

    return None

# Inicializar pygame
pygame.init()

# Configuración de la ventana
width, height = 400, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Map Coloring Visualization")

# Colores
colors = {
    "red": (255, 0, 0),
    "green": (0, 255, 0),
    "blue": (0, 0, 255),
    
}

# Dibujar el grafo
def draw_graph(solution):
    screen.fill((255, 255, 255))

    for var in csp.variables:        
        x, y = coordinates[var]
        pygame.draw.circle(screen, colors[solution[var][0]], (x, y), 30)

        text = pygame.font.Font(None, 40).render(var, True, (0, 0, 0))
        screen.blit(text, (x - 12, y - 12))

    for var1, neighbors in csp.neighbors.items():
        for var2 in neighbors:
            pygame.draw.line(screen, (0, 0, 0), coordinates[var1], coordinates[var2], 3)

    pygame.display.update()

# Visualizar el proceso del algoritmo
def visualize_process(csp, var):
    draw_graph(csp.domains)
    pygame.time.delay(300)

# Variables, dominios y restricciones del problema
coordinates = {
    "R1": (100, 100),
    "R2": (200, 50),
    "R3": (300, 100),
    "R4": (100, 200),
    "R5": (200, 200),
    "R6": (300, 200),
    "R7": (100, 300),
    "R8": (300, 300),
}

# Variables, dominios y restricciones del problema
variables = ["R1", "R2", "R3", "R4", "R5", "R6", "R7", "R8"]
domains = {var: ["red", "green", "blue"] for var in variables}
neighbors = {
    "R1": ["R2", "R4", "R5"],
    "R2": ["R1", "R3", "R5"],
    "R3": ["R2", "R5", "R6"],
    "R4": ["R1", "R5", "R7"],
    "R5": ["R1", "R2", "R3", "R4", "R6", "R7", ],
    "R6": ["R3", "R5", "R8"],
    "R7": ["R4", "R5", "R8"],
    "R8": ["R6", "R7", ],
}

def constraints(var1, color1, var2, color2):
    return color1 != color2

# Crear el CSP
csp = MapColoringCSP(variables, domains, neighbors, constraints)

# Resolver y visualizar el problema
queue = [(x1, x2) for x1 in variables for x2 in neighbors[x1]]
ac3(csp, queue)
solution = backtrack(csp)

# Mantener la ventana abierta hasta que se cierre
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()

       
