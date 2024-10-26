import pygame, constants, player


def main():
    print(constants.START_MSG)
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")

    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    running = True
    gamer = player.Player(x=constants.SCREEN_WIDTH /2, y=constants.SCREEN_WIDTH/2)

    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        dt = clock.tick(60) / 1000  # limits FPS to 60

        # fill the screen with a color to wipe away anything from last frame
        screen.fill(constants.BG_COLOR)

        # RENDER YOUR GAME HERE
        gamer.update(dt)
        gamer.draw(screen=screen)

        # flip() the display to put your work on screen
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()

    