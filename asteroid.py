import pygame, constants, circleshape, random


class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.position = pygame.Vector2(x, y)

    def split(self):
        self.kill()
        if self.radius > constants.ASTEROID_MIN_RADIUS:
            random_angle = random.uniform(20, 50)
            angle1 = pygame.math.Vector2.rotate(self.velocity, random_angle)
            angle2 = pygame.math.Vector2.rotate(self.velocity, -random_angle)
            new_radius = self.radius - constants.ASTEROID_MIN_RADIUS

            split1 = Asteroid(self.position.x, self.position.y, new_radius)
            split1.velocity = angle1 * constants.ASTEROID_SPLIT_SPEEDUP

            split2 = Asteroid(self.position.x, self.position.y, new_radius)
            split2.velocity = angle2 * constants.ASTEROID_SPLIT_SPEEDUP

        

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