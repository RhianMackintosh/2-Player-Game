import pygame

pygame.init()

green = (0,255,0)
PlatformColour = (141, 224, 155)
red = (255,0,0)
blue = (0,0,255)
sky = (189, 234, 252)
black = (0,0,0)
white = (255,255,255)
Player1Colour = (224, 141, 190)
Player2Colour = (109, 111, 206)

screen_width = 900
screen_height = 800

class Player(pygame.sprite.Sprite):
    def __init__(self,colour):
        super().__init__()

        player_width = 50
        player_height = 50
        self.image = pygame.Surface([player_width,player_height])
        self.image.fill(colour)

        self.rect = self.image.get_rect()
        self.change_x = 0
        self.change_y = 0


        self.level = None

    def Update(self):
        self.Calculate_Gravity()

        if self.rect.x + self.change_x <= 0:
            self.rect.x = self.rect.x
        elif self.rect.x + self.change_x >= screen_width -50:
            self.rect.x = self.rect.x
        else:
            self.rect.x += self.change_x




        block_collision_list = pygame.sprite.spritecollide(self,self.level.platform_list,False)
        for block in block_collision_list:
            if self.change_y > 0:
                self.rect.bottom = block.rect.left
            else:
                self.rect.top = block.rect.right

        self.rect.y += self.change_y

        block_collision_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_collision_list:
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom

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

        self.image.fill(PlatformColour)

        self.rect = self.image.get_rect()


class Level(object):                                                        #what does this do?
    def __init__(self,player):
        self.platform_list = pygame.sprite.Group()
        self.player = player

    def Update(self):
        self.platform_list.update()

    def draw(self, display):
        display.fill(sky)
        self.platform_list.draw(display)


class Level_01(Level):
    def __init__(self,player):
        Level.__init__(self,player)
        level = [[900, 20, 0, 780],
                 [210, 70, 200, 400],
                 [210, 70, 600, 300],
                 [100, 10, 300, 700]
                 ]

        for platform in level:
            block = Platform(platform[0],platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)





def GameLoop():
    clock = pygame.time.Clock()
    gameDisplay = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Game')
    player1 = Player(Player1Colour)
    player2 = Player(Player2Colour)
    Level_list = []
    Level_list.append(Level_01(player1))
    Level_list.append(Level_01(player2))


    Current_level_no = 0
    Current_level = Level_list[Current_level_no]

    Sprite_list = pygame.sprite.Group()
    player1.level = Current_level
    player2.level = Current_level

    player1.rect.x = 340
    player1.rect.y = 100
    player2.rect.x = 200
    player2.rect.y = 150
        #screen_height - player1.rect.height
    Sprite_list.add(player1)
    Sprite_list.add(player2)

    done = False

    #------MAIN LOOP-----------------------------------------------------------
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player1.GoLeft()
                if event.key == pygame.K_RIGHT:
                    player1.GoRight()
                if event.key == pygame.K_UP:
                    player1.Jump()

                if event.key == pygame.K_a:
                    player2.GoLeft()
                if event.key == pygame.K_d:
                    player2.GoRight()
                if event.key == pygame.K_w:
                    player2.Jump()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and player1.change_x < 0:
                    player1.Stop()
                if event.key == pygame.K_RIGHT and player1.change_x > 0:
                    player1.Stop()

                if event.key == pygame.K_a and player2.change_x < 0:
                    player2.Stop()
                if event.key == pygame.K_d and player2.change_x > 0:
                    player2.Stop()

        Sprite_list.update()

        Current_level.Update()

        player1.Update()
        player2.Update()
        if player1.rect.right > screen_width:
            player1.rect.right = screen_width

        Current_level.draw(gameDisplay)
        Sprite_list.draw(gameDisplay)

        clock.tick(45)

        pygame.display.update()

    pygame.quit()
    quit()

if __name__ == '__main__':
    GameLoop()