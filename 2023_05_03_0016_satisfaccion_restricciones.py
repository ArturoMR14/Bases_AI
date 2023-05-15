import pygame

# Dimensiones de la ventana
WIDTH = 540
HEIGHT = 600

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
GREEN = (0, 128, 0)

# Inicializar Pygame
pygame.init()

# Crear la ventana
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Resolución de Sudoku con metodo de vuelta atras")

# Fuente para los números
FONT = pygame.font.SysFont(None, 40)

class Sudoku:
    def __init__(self, puzzle):
        self.grid = puzzle

    def solve(self):
        if not self.find_empty():
            return True

        row, col = self.find_empty()

        for num in range(1, 10):
            if self.valid(num, row, col):
                self.grid[row][col] = num
                self.draw_grid(row, col, GREEN)

                pygame.display.update()
                pygame.time.delay(50)

                if self.solve():
                    return True

                self.grid[row][col] = 0
                self.draw_grid(row, col, GRAY)

                pygame.display.update()
                pygame.time.delay(50)

        return False

    def find_empty(self):
        for row in range(9):
            for col in range(9):
                if self.grid[row][col] == 0:
                    return row, col
        return None

    def valid(self, num, row, col):
        for i in range(9):
            if self.grid[row][i] == num or self.grid[i][col] == num:
                return False

        box_row = (row // 3) * 3
        box_col = (col // 3) * 3

        for i in range(box_row, box_row + 3):
            for j in range(box_col, box_col + 3):
                if self.grid[i][j] == num:
                    return False

        return True

    def print_grid(self):
        for i in range(9):
            for j in range(9):
                print(self.grid[i][j], end=" ")
            print()

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

# Se define el problema de Sudoku
sudoku = Sudoku(puzzle)

# Se dibuja el Sudoku vacío
sudoku.draw_grid(-1, -1, BLACK)

# Se resuelve el Sudoku
if sudoku.solve():
    print("La solución es:")
    sudoku.print_grid()
    pygame.quit()
else:
    print("No hay solución para el Sudoku.")