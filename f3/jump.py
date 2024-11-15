import pygame

pygame.init()
# screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True


pygame.display.set_caption("Jump")
win = pygame.display.set_mode((500, 500))
x = 100
y = 425
width = 20
height = 20
isJump = False
jumpCount = 10
vel = 5

while running:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # screen.fill()
    win.fill((0, 0, 0))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_q]:
        running = False
    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
    if keys[pygame.K_RIGHT] and x < 500 - width - vel:
        x += vel

    if not (isJump):
        if keys[pygame.K_UP] and y > vel:
            y -= vel
        if keys[pygame.K_DOWN] and y < 500 - width - vel:
            y += vel
        if keys[pygame.K_SPACE]:
            # pygame.draw.rect(win, (100, 0, 0), (x, y, width, height))
            isJump = True
    else:
        neg = 1
        if jumpCount < 0:
            neg = -1
        if jumpCount >= -10:
            y -= (jumpCount**2) * 0.5 * neg
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10

    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))

    # flip() the display to put your work on screen
    # pygame.display.flip()
    pygame.display.update()

    clock.tick(60)

pygame.quit()
