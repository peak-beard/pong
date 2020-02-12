# https://www.101computing.net/pong-tutorial-using-pygame-adding-a-bouncing-ball/

# defining some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# screen width and height
SCREEN_WIDTH = 1000          # recommended 700
SCREEN_HEIGHT = 800         # recommended 500

# position paddle A
paddle_a_x = 20
paddle_a_y = SCREEN_HEIGHT // 2

# position paddle B
paddle_b_x = SCREEN_WIDTH - 30
paddle_b_y = SCREEN_HEIGHT // 2

# line position
line_start_pos = [SCREEN_WIDTH // 2, 0]
line_end_pos = [SCREEN_WIDTH // 2, SCREEN_HEIGHT]
line_width = 5              # recommended 5
