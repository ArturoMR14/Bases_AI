import pygame

# Dimensiones de la ventana
WIDTH = 540
HEIGHT = 600

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
GREEN = (0, 128, 0)
YELLOW= (255, 255, 0)

# Inicializar Pygame
pygame.init()

# Crear la ventana
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Resolución de Sudoku con metodo de búsqueda hacia adelante")

# Fuente para los números
FONT = pygame.font.SysFont(None, 40)

class Sudoku:
    def __init__(self, puzzle):
        self.grid = puzzle

    def is_valid(self, row, col, num):
        # Verifica si el número ya está en la fila o columna
        for i in range(9):
            if self.grid[row][i] == num or self.grid[i][col] == num:
                return False

        # Verifica si el número ya está en la caja
        box_row = (row // 3) * 3
        box_col = (col // 3) * 3

        for i in range(box_row, box_row + 3):
            for j in range(box_col, box_col + 3):
                if self.grid[i][j] == num:
                    return False

        return True

    def forward_checking(self, row, col):
        valid_nums = set(range(1, 10))

        # Revisar fila y columna
        for i in range(9):
            valid_nums.discard(self.grid[row][i])
            valid_nums.discard(self.grid[i][col])

        # Revisar caja
        box_row = (row // 3) * 3
        box_col = (col // 3) * 3

        for i in range(box_row, box_row + 3):
            for j in range(box_col, box_col + 3):
                valid_nums.discard(self.grid[i][j])

        return valid_nums

    def solve(self, row, col):
        if row == 9:  # Se ha llegado al final del tablero
            return True

        if self.grid[row][col] != 0:  # Saltar casilla ya completada
            next_col, next_row = (col + 1) % 9, row + (col + 1) // 9
            return self.solve(next_row, next_col)

        valid_nums = self.forward_checking(row, col)

        for num in valid_nums:
            if self.is_valid(row, col, num):
                self.grid[row][col] = num
                self.draw_grid(row, col, GREEN)

                pygame.display.update()
                pygame.time.delay(20)

                next_col, next_row = (col + 1) % 9, row + (col + 1) // 9
                if self.solve(next_row, next_col):
                    return True

                self.grid[row][col] = 0
                self.draw_grid(row, col, GRAY)

                pygame.display.update()
                pygame.time.delay(20)

        return False

    def draw_grid(self, row, col, color):
        x = col * 60
        y = row * 60

        pygame.draw.rect(window, color, (x, y, 60, 60))
        for i in range(9):
            for j in range(9):
                value = self.grid[i][j]
                if value != 0:
                    text = FONT.render(str(value), True, WHITE)
                    text_rect = text.get_rect(center=(j * 60 + 30, i * 60 + 30))
                    window.blit(text, text_rect)

        pygame.display.update()

puzzle = [
    [0, 0, 3, 0, 2, 0, 6, 0, 0],
    [9, 0, 0, 3, 0, 5, 0, 0, 1],
    [0, 0, 1, 8, 0, 6, 4, 0, 0],
    [0, 0, 8, 1, 0, 2, 9, 0, 0],
    [7, 0, 0, 0, 0, 0, 0, 0, 8],
    [0, 0, 6, 7, 0, 8, 2, 0, 0],
    [0, 0, 2, 6, 0, 9, 5, 0, 0],
    [8, 0, 0, 2, 0, 3, 0, 0, 9],
    [0, 0, 5, 0, 1, 0, 3, 0, 0]
]

sudoku = Sudoku(puzzle)
sudoku.draw_grid(-1, -1, BLACK)

running = True
solved = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not solved:
        if sudoku.solve(0, 0):
            print("La solución es:")
            for row in sudoku.grid:
                print(row)
            solved = True
        else:
            print("No hay solución para el problema de Sudoku proporcionado.")
            running = False

pygame.display.update()
pygame.quit()


