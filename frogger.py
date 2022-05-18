from random import Random, randint
import pygame


pygame.init()

WIDTH = 600
HEIGHT = 300
VELOCITY = 2

if __name__ == "__main__":
    display_surface = pygame.display.set_mode((WIDTH, HEIGHT))
    frog_image = pygame.image.load("frog2.png")
    frog_rect = frog_image.get_rect()
    frog_rect.centerx = WIDTH//2
    frog_rect.centery = HEIGHT//2
    car_image = pygame.image.load("car2.png")
    car_rect = car_image.get_rect()
    car_rect.centerx = WIDTH//2
    car_rect.centery = HEIGHT//2
    clock = pygame.time.Clock()


    running = True
    while running:
        for event in pygame.event.get():
         if event.type == pygame.QUIT:
            running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and frog_rect.left > 0:
            frog_rect.x -= VELOCITY
        if keys[pygame.K_RIGHT] and frog_rect.right < WIDTH:
            frog_rect.x += VELOCITY
        if keys[pygame.K_UP] and frog_rect.top > 0:
            frog_rect.y -= VELOCITY
        if keys[pygame.K_DOWN] and frog_rect.bottom < HEIGHT:
            frog_rect.y += VELOCITY

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and car_rect.left > 0:
            car_rect.x -= VELOCITY
        if keys[pygame.K_d] and car_rect.right < WIDTH:
            car_rect.x += VELOCITY
        if keys[pygame.K_w] and car_rect.top > 0:
            car_rect.y -= VELOCITY
        if keys[pygame.K_s] and car_rect.bottom < HEIGHT:
            car_rect.y += VELOCITY

        if frog_rect.colliderect(car_rect):
            car_rect.x = randint(0, WIDTH - 10)
            car_rect.y = randint(0, HEIGHT - 15)

        if car_rect.colliderect(frog_rect):
            frog_rect.x = randint(0, WIDTH, - 10)
            frog_rect.y = randint(0, HEIGHT, - 15)

        display_surface.fill((0,0,0))
        display_surface.blit(frog_image, frog_rect)
        display_surface.blit(car_image, car_rect)

        pygame.display.update()
        clock.tick(60)
        


    pygame.quit()
    
