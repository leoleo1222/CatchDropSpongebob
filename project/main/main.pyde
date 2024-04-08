# Importing the Processing library
from processing import *

# Variable to keep track of the current page
currentPage = 1

# Variable to keep track of the score
score = 0

# Variable to keep track of the remaining time
remainingTime = 20  # Example: 60 seconds

# Variable to store the time when the game started
startTime = 0

# Variable to store the score when the game is over
finalScore = 0

# Position variables for Bob
bobWidth = 342
bobHeight = 377
bobX = 900
bobY = 600
bobImage = None  # Placeholder for the Bob image

jellyfishes = []  # List to store jellyfishes: [image, x, y]
jellyfishImages = []
jellyfishSpeed = 10  # Speed of jellyfish falling

# Variable to store the time when a new jellyfish should be generated
nextJellyfishTime = 0
# Variable to store the random interval between jellyfish generations (in milliseconds)
randomInterval = 0

def setup():
    size(1800, 1000)
    background_image = loadImage("background.png")
    global startTime, bobImage, randomInterval
    startTime = millis()  # Get the current time when the game starts
    bobImage = loadImage("bob.png")  # Load the image for Bob
    jellyfishImages.append(loadImage("jf1.png"))
    jellyfishImages.append(loadImage("jf2.png"))
    jellyfishImages.append(loadImage("jf3.png"))
    jellyfishImages.append(loadImage("jf4.png"))
    generateJellyfishes()
    randomInterval = int(random(750, 1650))  # Generate a random interval (Fine-tuning QAQ)
    print("Finish loading the setup()")

def draw():
    global currentPage, bobX, bobY, score, finalScore, nextJellyfishTime
    image(loadImage("background.png"), 0, 0)
    if currentPage == 1:
        drawWelcomePage()
    elif currentPage >= 2:
        drawGamePage()
        drawJellyfishes()
        moveJellyfishes()
        bobX = mouseX - bobWidth / 2 
        checkCollision()  # Check for collision with jellyfishes
        if millis() > nextJellyfishTime:
            generateJellyfish()
            nextJellyfishTime = millis() + randomInterval

def drawWelcomePage():
    # Display welcome message and start button
    textAlign(CENTER)
    textSize(60)
    fill(0)
    text("Welcome to Catch-and-Drop Game", width/2, height*0.3)
    
    textSize(50)
    fill(0)
    text("Press any key to start!", width/2, height*0.7)
    
def drawGamePage():
    global score, remainingTime, currentPage
    # Implement gameplay for each stage
    # Example: Display current score and remaining time
        
    if currentPage < 5:
        textSize(40)
        fill(0)
        text("Score: " + str(score), 100, 40)
        text("Time: " + str(remainingTime), 100, 100)  # Display time at the top right corner
        text("Current Stage: " + str(currentPage - 1), width/2, 100)

        # Update the remaining time based on elapsed time
        elapsedSeconds = (millis() - startTime) // 1000
        remainingTime = max(0, 20 - elapsedSeconds)  # Countdown from 60 seconds
    
    if remainingTime == 0 and currentPage < 5:
        # If time runs out, increment the phase and reset game parameters
        currentPage += 1
        showSpeedUpText
        resetGame()
    
    if currentPage == 5:
        # Display game over message, final score, and restart button
        textAlign(CENTER)
        textSize(20)
        fill(0)
        text("Game Over", width/2, height/2 - 20)
        text("Your Score: " + str(finalScore), width/2, height/2 + 20)  # Display the stored final score
        rectMode(CENTER)
        fill(200, 100, 100)
        rect(width/2, height/2 + 100, 120, 50)
        fill(255)
        text("Restart", width/2, height/2 + 110)
    
    # for _ in range(5):
    #         fill(255, 0, 0)  # Red color for "SPEED UP" text
    #         text("!!! SPEED UP !!!", width/2, height/2 - 20)
    #         delay(500)  # Delay for 0.5 seconds
    #         fill(255)
    #         text("!!! SPEED UP !!!", width/2, height/2 - 20)
    #         delay(500)  # Delay for 0.5 seconds
    
    # Draw Bob
    image(bobImage, bobX, bobY, bobWidth, bobHeight)  # Draw Bob using the loaded image

# def drawGameOverPage():
#     global finalScore
#     # Display game over message, final score, and restart button
#     textAlign(CENTER)
#     textSize(60)
#     fill(0)
#     text("Game Over", width/2, height/3 - 20)
#     text("Your Score: " + str(finalScore), width/2, height/2)  # Display the stored final score
#     rectMode(CENTER)
#     textSize(40)
#     fill(200, 100, 100)
#     rect(width/2, height/2 + 100, 120, 50)
#     fill(255)
#     text("Restart", width/2, height/2 + 110)
    
def generateJellyfishes():
    global jellyfishes
    jellyfishes = []
    for _ in range(3):  # initially juse spawn 3
        generateJellyfish()

def generateJellyfish():
    global jellyfishes, currentPage
    if currentPage <= 5:
        # Randomly choose a jellyfish image
        jellyfishImage = jellyfishImages[int(random(len(jellyfishImages)))]
        # Resize jellyfish image to width 200
        jellyfishImage.resize(200, 0)
        # Randomly choose x-coordinate within the specified range (100, 1500)
        jellyfishX = int(random(100, 1500))
        # Ensure new jellyfish is at least 100 pixels away from the previous one horizontally
        while jellyfishes and abs(jellyfishX - jellyfishes[-1]["x"]) < 100:
            jellyfishX = int(random(100, 1500))
        # Add jellyfish to the list
        jellyfishes.append({"image": jellyfishImage, "x": jellyfishX, "y": 50})


def drawJellyfishes():
    global jellyfishes
    for jellyfish in jellyfishes:
        image(jellyfish["image"], jellyfish["x"], jellyfish["y"])  # Draw jellyfish image

def moveJellyfishes():
    global jellyfishes, jellyfishSpeed
    if currentPage < 5:
        for jellyfish in jellyfishes:
            jellyfish["y"] += jellyfishSpeed  # Move jellyfish down slowly

def checkCollision():
    global score
    for jellyfish in jellyfishes:
        # Check if Bob's bounding box intersects with jellyfish's bounding box
        if (bobX < jellyfish["x"] + jellyfish["image"].width and
            bobX + bobWidth > jellyfish["x"] and
            bobY < jellyfish["y"] + jellyfish["image"].height and
            bobY + bobHeight > jellyfish["y"]):
            # Collision detected
            if jellyfish["image"] == jellyfishImages[0]:  # jf1 (pink)
                score += 4
            elif jellyfish["image"] == jellyfishImages[1]:  # jf2 (brown)
                score += 3
            elif jellyfish["image"] == jellyfishImages[2]:  # jf3 (green)
                score += 1
            elif jellyfish["image"] == jellyfishImages[3]:  # jf4 (purple)
                score += 2
            jellyfishes.remove(jellyfish)  # Remove jellyfish from the list


def resetGame():
    global score, bobX, bobY, jellyfishes, remainingTime, jellyfishSpeed, nextJellyfishTime, startTime, currentStage
    remainingTime = 20
    jellyfishSpeed = jellyfishSpeed + 15  # Increase jellyfish speed for the next stage
    nextJellyfishTime = millis() + randomInterval
    # generateJellyfishes()
    startTime = millis()
    
def showSpeedUpText():
    textSize(40)
    fill(255, 0, 0)  # Red color for "SPEED UP" text
    text("!!! SPEED UP !!!", width/2, height/2 - 20)
    delay(500)  # Delay for 0.5 seconds
    fill(255)
    text("!!! SPEED UP !!!", width/2, height/2 - 20)

def keyPressed():
    global currentPage, score, finalScore
    if currentPage == 5:
        score = 0  # Reset the score when restarting the game
    currentPage = 2  # Start the game when any key is pressed
