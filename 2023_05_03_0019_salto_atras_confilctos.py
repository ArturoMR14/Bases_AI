import pygame
import time

def conflict(current, row):
    for i in range(row):
        if current[i] == current[row] or \
           current[i] - current[row] == row - i or \
           current[row] - current[i] == row - i:
            return True
    return False

def backtrack(n, row, current, result, screen):
    if row == n:
        result.append(current[:])
        draw_board(screen, n, current, (0, 255, 0))
        time.sleep(0.5)  # Esperar medio segundo antes de continuar
    else:
        for i in range(n):
            current[row] = i
            if not conflict(current, row):
                draw_board(screen, n, current, (255, 0, 0))
                time.sleep(0.5)  # Esperar una décima de segundo antes de continuar
                backtrack(n, row + 1, current, result, screen)
def n_queens(n):
    current, result = [0] * n, []
    pygame.init()
    screen = pygame.display.set_mode((n*50, n*50))
    draw_board(screen, n, current, (200, 200, 200))
    backtrack(n, 0, current, result, screen)
    pygame.quit()
    return result

def draw_board(screen, n, current, color):
    screen.fill((255, 255, 255))
    for i in range(n):
        for j in range(n):
            cell_color = (200, 200, 200) if (i+j) % 2 == 0 else (100, 100, 100)
            pygame.draw.rect(screen, cell_color, (j*50, i*50, 50, 50))
            if current[i] == j:
                pygame.draw.circle(screen, color, (j*50+25, i*50+25), 20)
    pygame.display.flip()

if __name__ == '__main__':
    n=4
    solutions = n_queens(n)
    print(f"Se encontraron {len(solutions)} soluciones.")
