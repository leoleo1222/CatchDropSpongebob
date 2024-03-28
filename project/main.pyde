def setup(): 
    global x, y, dx, dy, w, h #other fishes
    global player, playerW, playerH #player's fish
    global bg, img
    global totalNum
    global stageNum
    global timeIsup
    global startTime
    
    size(1000,1000)
    totalNum = 4

    
    bg = loadImage("background.png")    
    player = loadImage("maincharacter.png")
    playerW = 50
    playerH = 50
    
    img = []
    w = []
    h = []
    x = []
    y = []
    dx = []
    dy = []
    for i in range(totalNum): 
        scale = random(0.2, 0.4)
        img.append(loadImage("jf"+str(i)+".png"))
        w.append(img[i].width * scale)
        h.append(img[i].height * scale)
        x.append(random(0, width/2))
        y.append(random(0, height-h[i]))
        dx.append(random(0.1, 3))
        dy.append(random(-1, 1))
        
    
    startTime = millis()
    
    


    
    stageNum = 0
    

        


    
def draw():

    
    image(bg, 0, 0, width, height)
        
    if (stageNum == 0):
        drawWelcome()
    
        

        
    elif (stageNum == 1) :
            drawGamePlay()
            for i in range(totalNum):
                image(img[i], x[i], y[i], w[i], h[i])
                x[i] = x[i] + dx[i]
                y[i] = y[i] + dy[i]
                if x[i] > width:
                    scale = random(0.2, 0.4)
                    w[i] = img[i].width * scale
                    h[i] = img[i].height * scale
                    
                    x[i] = random( -w[i],-w[i]*3)
                    
                    y[i] = random(0, height-h[i])
                    
                    dx[i] = random(0.1, 3)
                    dy[i] = random(-1,1)
                    
                if (y[i] < 0):
                    y[i] = 0
                    dy[i] = -dy[i]
                elif (y[i] + h[i] > height):
                    y[i] = height - h[i]
                    dy[i] = -dy[i]

            image(player, mouseX-playerW/2, mouseY-playerH/2, playerW, playerH)
        
            
    elif (stageNum == 2) :
            drawGamePlay2()
            
    elif (stageNum == 3) :
            drawGamePlay3()
            
    elif (stageNum == 4) :
            drawGameOver()

        
def keyPressed():
    global stageNum
    if (stageNum == 0) : #at Welcome Page
        stageNum = 1 #move to Game Play if any key is pressed
    
    elif (stageNum == 1) : #at Game Play
        stageNum = 2 #move to Game Over if any key is pressed
        
    elif (stageNum == 2) : #at Game Play
        stageNum = 3
    elif (stageNum == 3) : #at Game Play
        stageNum = 4
    elif (stageNum == 4) : #at Game Play
        stageNum = 0
    
    
def drawWelcome():
    background(255)
    image(bg,0,0,width, height)
    image(player, 200,740, 100, 100)
    fill(0,0,0)
    textSize(30)    
    text("~Welcome~", 50, 50)
    text("Press any key to Game Play", 50, 100)
    text("How to play?", 50, 150)
    text("move the mouse horizontally to catch all the jellyfish and", 50,200)
    text("avoid touching the bombs",50,250)
    
    
    

def drawGamePlay():
    image(bg,0,0,width, height)
    text("Time:" + str((millis()- startTime)/1000) + "s", 40,60)
    
    
def drawGamePlay2():
    image(bg,0,0,width, height) 
    
def drawGamePlay3():
    image(bg,0,0,width, height) 

    
    
def drawGameOver():    
    image(bg,0,0,width, height)  
    fill(250, 250, 0)
    text("Game Over!", 500, 500)
    text("Click any button to restart", 300, 700)
    
    
    
    
    



    
    
    
    
    
    
