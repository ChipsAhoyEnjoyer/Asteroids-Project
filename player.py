import circleshape, pygame, constants, shot


class Player(circleshape.CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, constants.PLAYER_RADIUS)
        self.rotation = 0
        self.cd_timer = 0
    
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(
            surface=screen, 
            color=constants.PLAYER_COLOR, 
            points=self.triangle(), 
            width=constants.PLAYER_WIDTH
            )
        
    def shoot(self):
        if self.cd_timer <= 0:
            self.cd_timer = constants.PLAYER_SHOOT_COOLDOWN
            bullet = shot.Shot(self.position.x, self.position.y, constants.SHOT_RADIUS)
            bullet.velocity = pygame.math.Vector2(0, 1).rotate(self.rotation) * constants.PLAYER_SHOT_SPEED
    
    def rotate(self, dt):
        self.rotation += constants.PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * constants.PLAYER_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()
        
        if self.cd_timer > 0:
            self.cd_timer -= dt

        if keys[pygame.K_a]:
            self.rotate(dt=dt * -1)
        if keys[pygame.K_d]:
            self.rotate(dt=dt)
        if keys[pygame.K_w]:
            self.move(dt=dt)
        if keys[pygame.K_s]:
            self.move(dt=dt * -1)
        if keys[pygame.K_SPACE]:
            self.shoot()
