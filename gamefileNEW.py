import pygame

pygame.init()

green = (0,255,0)
red = (255,0,0)
blue = (0,0,255)
black = (0,0,0)
white = (255,255,255)

screen_width = 900
screen_height = 800

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        player_width = 50
        player_height = 50
        self.image = pygame.Surface([player_width,player_height])
        self.image.fill(red)

        self.rect = self.image.get_rect()
        self.change_x = 0
        self.change_y = 0


        self.level = None

    def Update(self):
        self.Calculate_Gravity()

        self.rect.x += self.change_x

        block_collision_list = pygame.sprite.spritecollide(self,self.level.platform_list,False)
        for block in block_collision_list:
            if self.change_y > 0:
                self.rect.bottom = platform.rect.top
            else:
                self.rect.top = platform.rect.bottom

            self.change_y = 0

    def Calculate_Gravity(self):
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += 0.35

        if self.rect.y >= screen_height - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = screen_height - self.rect.height

    def Jump(self):
        self.rect.y += 2
        platform_collision_hit = pygame.sprite.spritecollide(self,self.level.platform_list,False)
        self.rect.y -= 2
        if len(platform_collision_hit) > 0 or self.rect.bottom >= screen_height:
            self.change_y = -10


    def GoLeft(self):
        self.change_x = -6

    def GoRight(self):
        self.change_x = 6

    def Stop(self):
        self.change_x = 0


class Platform(pygame.sprite.Sprite):
    def __init__(self,platform_width,platform_height):
        super().__init__()

        self.image = pygame.Surface([platform_width,platform_height])

        self.image.fill(green)

        self.rect = self.image.get_rect()







def GameLoop():
    clock = pygame.time.Clock()
    gameDisplay = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Game')
    pygame.display.update()


