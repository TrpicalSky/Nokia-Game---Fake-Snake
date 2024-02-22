import pygame
import snake
import food
import score
import sys

# Initialize Pygame
pygame.init()


#Intialize Font Render
font = pygame.font.SysFont("Arial",20)


# Set up some constants
WIDTH, HEIGHT =  240,  320  # These are typical dimensions for a Nokia phone game
FPS =  30

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Nokia Phone Game")

#Initializing Snake Class
snake_class = snake.Snake([160,160],screen=screen)

#Intitialzing Food Class
food_class = food.Food(screen=screen)

#Intializing Score Class
score_class = score.Score(screen=screen,font=font)

# Set up the clock
clock = pygame.time.Clock()

# Game loop
running = True
current_snake:pygame.Rect = pygame.Rect(0,0,0,0)
current_food:pygame.Rect = pygame.Rect(0,0,0,0)
while running:
    # Keep loop running at the right speed
    clock.tick(FPS)
    # Process input (events)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                snake_class.draw(0,-10)
            if event.key == pygame.K_s:
                snake_class.draw(0,10)
            if event.key == pygame.K_a:
                snake_class.draw(-10,0)
            if event.key == pygame.K_d:
                snake_class.draw(10,0)
        if current_snake.colliderect(current_food):
            food_class.collide(score_class)
            print("Hit Food!")
    # Update game state
    # This is where you update all the game objects

    # Draw / render
    screen.fill((0,  0,  0))  # Fill the screen with black

    # This is where you draw everything
    
    score_class.draw()

    current_snake = snake_class.draw(0,0)

    current_food = food_class.draw()




    pygame.display.flip()

pygame.quit()
sys.exit()
