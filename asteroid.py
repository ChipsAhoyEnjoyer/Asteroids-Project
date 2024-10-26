import pygame, constants, circleshape


class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.position = pygame.Vector2(x, y)

    def draw(self, screen):
        pygame.draw.circle(
            surface=screen, 
            color=constants.ASTEROID_COLOR, 
            center=[self.position.x, self.position.y], 
            radius=self.radius, 
            width=constants.ASTEROID_WIDTH,
            )
   
    def update(self, dt):
        self.position += self.velocity * dt