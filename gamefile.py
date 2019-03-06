import pygame

pygame.init()


# ========================================================================================================================

import sqlite3
import sys
from random import *
import time
import pygame
from Sub_UI_MainMenu import MainMenuUI
from Sub_UI_LogIn import LogInUI
from Sub_UI_SignUp import SignUpUI

pygame.init()
# ========================================================================================================================
# creating the database to add things into

db = sqlite3.connect("users.db")
cursor = db.cursor()

# drop the table to remake it
cursor.execute('''DROP TABLE users''')

    #create table
cursor.execute('''CREATE TABLE users (number INT, username STRING, password STRING, security STRING,name STRING, surname STRING,G1HS INT,G2HS INT,G3HS INT)''')

cursor.execute('''INSERT INTO users (number,username,password,security,name,surname,G1HS,G2HS,G3HS) VALUES (1,"rhianmack","1234","Storkey","Rhian","Mackintosh",0,0,0)''')
cursor.execute('''INSERT INTO users (number,username,password,security,name,surname,G1HS,G2HS,G3HS) VALUES (2,"yasminS","2342","Sunthankar","Yasmin","Sunthankar",0,0,0)''')
db.commit()


# ========================================================================================================================
# pygame variables for log in menu
ScreenWidth = 800
ScreenHeight = 800
font = pygame.font.Font("freesansbold.ttf", 50)
big = pygame.font.Font("freesansbold.ttf", 50)
small = pygame.font.Font("freesansbold.ttf", 30)

#Colours
StartColour = (163, 218, 246)
StartColourD = (132, 205, 242)
backGC = (217, 240, 252)
green = (0,255,0)
red = (255,0,0)
blue = (0,0,255)
black = (0,0,0)

LogIn = "Log In"
SignIn = "Sign In"

window = pygame.display.set_mode((ScreenWidth, ScreenHeight))
window.fill((255, 255, 255))
pygame.display.set_caption("Games")
pygame.display.update()


# ========================================================================================================================

def button(StartColour, x, y, width, height, text, fontC, pos1, pos2):
    pygame.draw.rect(window, (StartColour), (x, y, width, height))
    Button2 = fontC.render(text, 1, (0, 0, 0))
    window.blit(Button2, (pos1, pos2))


# ========================================================================================================================
def LogIn():
    retry = 0
    User, wPass = LogInUI(retry)
    # print(User,wPass)
    c = False
    while c == False:
        a = False
        while a == False:

            cursor.execute('''SELECT * FROM users''')
            for row in cursor:
                username = row[1]
                number = row[0]
                print(username)
                if User == username:
                    print("matching")
                    a = True
                    passcheck(User, wPass, number)
                else:
                    pass
            print("Incorrect Username, please try again (error 2)")
            retry = 1
            User, wPass = LogInUI(retry)


# checking if the password matches that chosen username
def passcheck(User, wPass, number):
    b = False
    while b == False:
        cursor.execute('''SELECT password FROM users WHERE username = ?''', (User,))
        for row in cursor:
            if wPass == str(row[0]):
                b = True
                c = True
                break
            else:
                print("Incorrect password, please try again (error 1)")
                button(backGC, 300, 700, 150, 40, "Incorrect username or password, please try again", small, 350, 610)
                retry = 1
                User, wPass = LogInUI(retry)
                b = True

    profile(number)


# =========================================================================================================================
def SignUp():
    retry = 0
    name, surname, Nuser, Npass, confirm, Nsecurity = SignUpUI(retry)
    print(name, surname, Nuser, Npass, confirm, Nsecurity)
    # SignUpUI()
    # checking they entered the correct password
    d = False
    while d == False:
        # Npass = input("Enter your new password: ")
        # confirm = input("Please confirm your password: ")
        if Npass == confirm:
            d = True
        else:
            retry = 1
            name, surname, Nuser, Npass, confirm, Nsecurity = SignUpUI(retry)
            d = False


    # generating the number so it adds onto the end of the numbers already, wouldnt be efficent with lots of data
    cursor.execute('''SELECT number FROM users''')
    for row in cursor:
        number = row[0]
        print(number)
    number = number + 1

    cursor.execute(
        '''INSERT INTO users (number,username,password,security,name,surname,G1HS,G2HS,G3HS) VALUES (?,?,?,?,?,?,0,0,0)''',
        (number, Nuser, Npass, Nsecurity, name, surname))
    db.commit()
    Menu()


# =========================================================================================================================

def Menu():
    option = MainMenuUI()

    if option == "1":
        print("Sign up followed")
        SignUp()
    elif option == "2":
        print("log in followed")
        LogIn()





# =========================================================================================================================
def Menu2(number):
    menu = input("What would you like to do:\n\
    1. Edit your profile\n\
    2. View your profile\n\
    3. Go to the games\n")
    e = False
    while e == False:
        if menu == "1":
            e = True
            print("Make edit function")
        elif menu == "2":
            e = True
            profile(number)
        elif menu == "3":
            e = True
            gamesMenu(number)
        else:
            menu = input("Please enter '1' or '2': ")




# =========================================================================================================================
def profile(number):
    cursor.execute('''SELECT * FROM users where number == ?''', (number,))
    for row in cursor:
        username = row[1]
        password = row[2]
        security = row[3]
        name = row[4]
        surname = row[5]
        G1HS = row[6]
        G2HS = row[7]
        G3HS = row[8]
        print("========================================")
        print("WELCOME BACK: " + name + " " + surname)
        print("Guess the number highscore: " + str(G1HS) + " Guesses")
        print("Rock Paper scissors wins: " + str(G2HS))
        print("Game 3: " + str(G3HS))


        GameLoop()

# =========================================================================================================================
# ACTUAL GAME CODE
# =========================================================================================================================


class Character(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, colour):

        super().__init__()

        self.image = pygame.Surface([width,height])
        self.image.fill(colour)

        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

        self.change_x = 0
        self.change_y = 0

        self.gravity = 0.1
        self.velocity = 2
        self.mass = 2
        self.speed = 2
        self.isjump = 0



    def GoLeft(self):
        self.change_x = -3
        self.change_y = 0
        self.Update()
    def GoRight(self):
        self.change_x = 3
        self.change_y = 0
        self.Update()
    #def CalculateGravity(self):
        #if change_y = 0:

    def Jump(self):
        self.isjump = 1
        self.Update()

    def Stop(self):
        self.change_y = 0
        self.change_x = 0


    def Update(self):
        if self.isjump:
            F = (self.mass * self.velocity)


            self.rect.y -= F
            self.velocity -= 1

            if self.rect.y == 650:
                self.rect.y = 650
                self.isjump = 0
                self.velocity = 8

        self.rect.x += self.change_x
        if self.rect.x <= 0:
            self.rect.x = 0
        elif self.rect.x >= 850:
            self.rect.x = 850

        self.rect.y += self.change_y
        if self.rect.y <= 0:
            self.rect.y = 0
        elif self.rect.y >= 850:
            self.rect.y = 850




class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, colour):

        super().__init__()

        self.image = pygame.Surface([width,height])
        self.image.fill(colour)

        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

        pygame.display.update()




List_Of_Sprites = pygame.sprite.Group()

platform_list = pygame.sprite.Group() # creates list of platforms that can be added to below
                                      # Platform(posx, posy, width, height)

plat = Platform(0, 700, 900, 100, green)
platform_list.add(plat)
List_Of_Sprites.add(plat)

#plat = Platform()


player1 = Character(50,650,50,50,red)
player2 = Character(150,650,50,50,blue)
List_Of_Sprites.add(player1,player2)






"""

class Dangers():
    def __init__(self):


"""



def GameLoop():
    display_height = 800
    display_width = 900
    gameDisplay = pygame.display.set_mode((display_width, display_height))
    pygame.display.set_caption('Game')
    pygame.display.update()




    run = True
    while run == True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_ESCAPE]:
            run = False
            pygame.quit()
            quit()

        if keys[pygame.K_LEFT]:
            player1.GoLeft()
        if keys[pygame.K_RIGHT]:
            player1.GoRight()

        if keys[pygame.K_a]:
            player2.GoLeft()
        if keys[pygame.K_d]:
            player2.GoRight()

        if keys[pygame.K_UP]:
            player1.Jump()

        else:
            player1.Stop()
            player2.Stop()
        gameDisplay.fill(black)
        List_Of_Sprites.update()
        List_Of_Sprites.draw(gameDisplay)
        pygame.display.update()



#Menu()

GameLoop()
#=======================================================================================================================
"""Notes



"""
