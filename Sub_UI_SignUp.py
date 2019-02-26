#Pygame Signup
import pygame
pygame.init()
    

def SignUpUI(retry):
    def button(StartColour,x,y,width,height,text,fontC,pos1,pos2):
        pygame.draw.rect(window,(StartColour),(x,y,width,height))
        Button2 = fontC.render(text,1,(0,0,0))
        window.blit(Button2,(pos1,pos2))

    #------------------------------------------------------------------------------
    white = (255,255,255)
    backGC = (217, 240, 252)
    StartColour = (163,218,246)
    StartColourD = (132,205,242)
    ScreenWidth = 800
    ScreenHeight = 800
    typeFirst = ""
    typeLast = ""
    typeUser = ""
    typePass = ""
    typeConfirm = ""
    typeAnswer = ""
    big = pygame.font.Font("freesansbold.ttf",50)
    small = pygame.font.Font("freesansbold.ttf",30)
    tiny = pygame.font.Font("freesansbold.ttf",20)
    window = pygame.display.set_mode((ScreenWidth,ScreenHeight))
    window.fill((backGC))
    pygame.display.update()
    #------------------------------------------------------------------------------

    button(StartColourD,120,40,310,80,"Sign Up",big,170,55)
    button(StartColour,110,30,310,80,"Sign Up",big,170,45)
    button(StartColourD,460,40,210,80,"Submit",big,465,55)
    button(StartColour,450,30,210,80,"Submit",big,465,45)

    #name button
    button(StartColour,160,180,180,40,"First Name",small,170,185)
    button(white,350,180,270,40,"",small,170,185)

    #surname button
    button(StartColour,160,275,180,40,"Last Name",small,170,280)
    button(white,350,275,270,40,"",small,170,280)

    #username button
    button(StartColour,160,375,180,40,"Username",small,170,380)
    button(white,350,375,270,40,"",small,170,380)

    #upassword button
    button(StartColour,160,475,180,40,"Password",small,170,480)
    button(white,350,475,270,40,"",small,170,480)

    #password check button
    button(StartColour,160,575,180,40,"Confirm",small,170,580)
    button(white,350,575,270,40,"",small,170,580)

    #security question button
    button(backGC,60,685,180,10,"Security Question: What is your mothers maiden name",tiny,120,685)
    button(StartColour,160,720,180,40,"Answer",small,190,725)
    button(white,350,720,270,40,"",small,170,725)

    if retry == 1:
        button(backGC,650,475,1,1,"Passwords",tiny,650,475)
        button(backGC,650,480,1,1,"do not",tiny,650,490)
        button(backGC,650,485,1,1,"match please",tiny,650,505)
        button(backGC,650,490,1,1,"retry",tiny,650,520)
    else:
        pass

    pygame.display.update()
    
    pygame.mouse.set_pos([0,0])
    
    selec = False
    while selec == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEMOTION:
                print(event.pos)

        
        
        mousex,mousey = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if mousex >= 350 and mousex <= 620 and mousey >= 180 and mousey <= 220:
            button(StartColourD,140,170,500,60,"",small,170,185)
            button(StartColour,160,180,180,40,"First Name",small,170,185)
            button(white,350,180,270,40,"",small,170,185)
            button(white,350,180,270,40,typeFirst,small,360,185)
            pygame.display.update()

            finished = False
            
            while finished == False: 
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.unicode.isalpha():
                            typeFirst += event.unicode
                        elif event.unicode.isdigit():
                            typeFirst += event.unicode
                        elif event.key == pygame.K_BACKSPACE:
                            typeFirst = typeFirst[:-1]
                        elif event.key == pygame.K_RETURN:
                            finished = True
                            pygame.mouse.set_pos([400,235])
                            
                    print(typeFirst)
                    button(white,350,180,270,40,typeFirst,small,360,185)
                    pygame.display.update()
            
        elif mousex >= 350 and mousex <= 620 and mousey >= 275 and mousey <= 315:
            button(StartColourD,140,265,500,60,"",small,170,280)
            button(StartColour,160,275,180,40,"Last Name",small,170,280)
            button(white,350,275,270,40,"",small,170,280)
            button(white,350,275,270,40,typeLast,small,360,280)
            pygame.display.update()

            finished = False
            
            while finished == False: 
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.unicode.isalpha():
                            typeLast += event.unicode
                        elif event.unicode.isdigit():
                            typeLast += event.unicode
                        elif event.key == pygame.K_BACKSPACE:
                            typeLast = typeLast[:-1]
                        elif event.key == pygame.K_RETURN:
                            finished = True
                            pygame.mouse.set_pos([400,335])
                            
                    print(typeLast)
                    button(white,350,275,270,40,typeLast,small,360,280)
                    pygame.display.update()

        elif mousex >= 350 and mousex <= 620 and mousey >= 375 and mousey <= 415:
            button(StartColourD,140,365,500,60,"",small,170,280)
            button(StartColour,160,375,180,40,"Username",small,170,380)
            button(white,350,375,270,40,"",small,170,380)
            button(white,350,375,270,40,typeUser,small,360,380)
            pygame.display.update()

            finished = False
            
            while finished == False: 
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.unicode.isalpha():
                            typeUser += event.unicode
                        elif event.unicode.isdigit():
                            typeUser+= event.unicode
                        elif event.key == pygame.K_BACKSPACE:
                            typeUser = typeUser[:-1]
                        elif event.key == pygame.K_RETURN:
                            finished = True
                            pygame.mouse.set_pos([400,435])
                            
                    print(typeUser)
                    button(white,350,375,270,40,typeUser,small,360,380)
                    pygame.display.update()

        elif mousex >= 350 and mousex <= 620 and mousey >= 475 and mousey <= 515:
            button(StartColourD,140,465,500,60,"",small,170,280)
            button(StartColour,160,475,180,40,"Password",small,170,480)
            button(white,350,475,270,40,"",small,170,480)
            button(white,350,475,270,40,typePass,small,360,480)
            pygame.display.update()

            finished = False
            
            while finished == False: 
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.unicode.isalpha():
                            typePass += event.unicode
                        elif event.unicode.isdigit():
                            typePass += event.unicode
                        elif event.key == pygame.K_BACKSPACE:
                            typePass = typePass[:-1]
                        elif event.key == pygame.K_RETURN:
                            finished = True
                            pygame.mouse.set_pos([400,535])
                            
                    print(typePass)
                    button(white,350,475,270,40,typePass,small,360,480)
                    pygame.display.update()

        elif mousex >= 350 and mousex <= 620 and mousey >= 575 and mousey <= 615:
            button(StartColourD,140,565,500,60,"",small,170,280)
            button(StartColour,160,575,180,40,"Confirm",small,170,580)
            button(white,350,575,270,40,"",small,170,580)
            button(white,350,575,270,40,typePass,small,360,585)
            pygame.display.update()

            finished = False
            
            while finished == False: 
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.unicode.isalpha():
                            typeConfirm += event.unicode
                        elif event.unicode.isdigit():
                            typeConfirm += event.unicode
                        elif event.key == pygame.K_BACKSPACE:
                            typeConfirm = typeConfirm[:-1]
                        elif event.key == pygame.K_RETURN:
                            finished = True
                            pygame.mouse.set_pos([400,635])
                            
                    print(typeConfirm)
                    button(white,350,575,270,40,typeConfirm,small,360,580)
                    pygame.display.update()

        elif mousex >= 350 and mousex <= 620 and mousey >= 720 and mousey <= 760:
            button(StartColourD,140,710,500,60,"",small,170,280)
            button(StartColour,160,720,180,40,"Answer",small,190,725)
            button(white,350,720,270,40,"",small,170,725)
            button(white,350,720,270,40,typeAnswer,small,360,725)
            pygame.display.update()

            finished = False
            
            while finished == False: 
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.unicode.isalpha():
                            typeAnswer += event.unicode
                        elif event.unicode.isdigit():
                            typeAnswer += event.unicode
                        elif event.key == pygame.K_BACKSPACE:
                            typeAnswer = typeAnswer[:-1]
                        elif event.key == pygame.K_RETURN:
                            finished = True
                            pygame.mouse.set_pos([400,635])
                            
                    print(typeAnswer)
                    button(white,350,720,270,40,typeAnswer,small,360,725)
                    pygame.display.update()

        elif mousex >= 450 and mousex <= 660 and mousey >= 30 and mousey <= 110:
            button(StartColourD,450,30,210,80,"Submit",big,465,45)

            if click[0] == 1:
                print("Clicked Submit")
                selec = True
                return typeFirst, typeLast, typeUser, typePass, typeConfirm, typeAnswer
            

        else:
            button(backGC,130,150,520,650,"",small,0,0)
            
            #title button
            button(StartColourD,120,40,310,80,"Sign Up",big,170,55)
            button(StartColour,110,30,310,80,"Sign Up",big,170,45)
            button(StartColourD,460,40,210,80,"Submit",big,465,55)
            button(StartColour,450,30,210,80,"Submit",big,465,45)

            #name button
            button(StartColour,160,180,180,40,"First Name",small,170,185)
            button(white,350,180,270,40,typeFirst,small,360,185)

            #surname button
            button(StartColour,160,275,180,40,"Last Name",small,170,280)
            button(white,350,275,270,40,typeLast,small,360,280)

            #username button
            button(StartColour,160,375,180,40,"Username",small,170,380)
            button(white,350,375,270,40,typeUser,small,360,380)

            #upassword button
            button(StartColour,160,475,180,40,"Password",small,170,480)
            button(white,350,475,270,40,typePass,small,360,480)

            #password check button
            button(StartColour,160,575,180,40,"Confirm",small,170,580)
            button(white,350,575,270,40,typeConfirm,small,360,580)

            #security question button
            button(backGC,60,685,180,10,"Security Question: What is your mothers maiden name",tiny,120,685)
            button(StartColour,160,720,180,40,"Answer",small,190,725)
            button(white,350,720,270,40,typeAnswer,small,360,725)

            pygame.display.update()
            


        

        
    
    
    
