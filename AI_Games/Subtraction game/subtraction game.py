import pygame, sys, math

pygame.init()
WIDTH, HEIGHT = 400, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Subtraction Game - Player vs AI")

FONT = pygame.font.SysFont("arial", 36)
SMALL_FONT = pygame.font.SysFont("arial", 24)
BG_COLOR = (44, 62, 80)
STONE_COLOR = (255, 111, 97)
STONE_ALT = (107, 91, 149)
TEXT_COLOR = (255, 255, 255)
BUTTON_COLOR = (26, 188, 156)
BUTTON_HOVER = (22, 160, 133)

stones = 25
BUTTONS = []

def minimax(stones, is_maximizing):
    if stones == 0:
        return -1 if is_maximizing else 1
    scores = []
    for move in [1, 2, 3]:
        if stones - move >= 0:
            score = minimax(stones - move, not is_maximizing)
            scores.append(score)
    return max(scores) if is_maximizing else min(scores)

def ai_move(stones):
    best_score = -math.inf
    best_move = 1
    for move in [1, 2, 3]:
        if stones - move >= 0:
            score = minimax(stones - move, False)
            if score > best_score:
                best_score = score
                best_move = move
    return best_move

def draw_stones():
    screen.fill(BG_COLOR)
    for i in range(stones):
        x = 20 + (i % 5) * 70
        y = 20 + (i // 5) * 70
        color = STONE_COLOR if i % 2 == 0 else STONE_ALT
        pygame.draw.circle(screen, color, (x + 25, y + 25), 25)
        num = FONT.render(str(stones - i), True, TEXT_COLOR)
        screen.blit(num, num.get_rect(center=(x + 25, y + 25)))

def draw_buttons():
    BUTTONS.clear()
    for i, move in enumerate([1, 2, 3]):
        rect = pygame.Rect(50 + i * 100, 400, 80, 50)
        mouse_over = rect.collidepoint(pygame.mouse.get_pos())
        pygame.draw.rect(screen, BUTTON_HOVER if mouse_over else BUTTON_COLOR, rect)
        label = SMALL_FONT.render(f"Remove {move}", True, TEXT_COLOR)
        screen.blit(label, label.get_rect(center=rect.center))
        BUTTONS.append((rect, move))

def display_message(text):
    overlay = pygame.Surface((WIDTH, HEIGHT))
    overlay.set_alpha(200)
    overlay.fill((0, 0, 0))
    screen.blit(overlay, (0, 0))
    msg = FONT.render(text, True, TEXT_COLOR)
    screen.blit(msg, msg.get_rect(center=(WIDTH // 2, HEIGHT // 2)))
    pygame.display.flip()
    pygame.time.wait(3000)

def main():
    global stones
    player_turn = True
    running = True

    while running:
        draw_stones()
        draw_buttons()
        pygame.display.flip()

        if stones == 0:
            winner = "You win! 🎉" if not player_turn else "AI wins! 🤖"
            display_message(winner)
            running = False
            continue

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN and player_turn:
                for rect, move in BUTTONS:
                    if rect.collidepoint(event.pos):
                        if move > stones:
                            display_message("Invalid move!")
                        else:
                            stones -= move
                            player_turn = False

        if not player_turn and stones > 0:
            pygame.time.wait(500)
            move = ai_move(stones)
            stones -= move
            player_turn = True

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()

