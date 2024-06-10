# start the main loop
while True:
# listen for events
    for event in pygame.event.get():
     if event.type == pygame.QUIT: sys.exit()
# update the game objects as appropriate
red_rect = red_rect.move(speed)
if red_rect.left < 0 or red_rect.right > width:
speed[0] = -speed[0]
if red_rect.top < 0 or red_rect.bottom > height:
speed[1] = -speed[1]
# update the screen
screen.fill(black)
screen.blit(red_surf, red_rect)
pygame.display.flip()
clock.tick(60)
