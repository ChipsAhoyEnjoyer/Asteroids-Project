import pygame, circleshape,constants


class Shot(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.position = pygame.math.Vector2(x, y)
    
    def draw(self, screen):
        pygame.draw.circle(
            surface=screen, 
            color=constants.SHOT_COLOR, 
            center=[self.position.x, self.position.y], 
            radius=self.radius, 
            width=constants.SHOT_WIDTH,
            )
   
    def update(self, dt):
        self.position += self.velocity * dt
