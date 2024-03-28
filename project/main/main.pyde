from random import randint
from datetime import datetime

last_jellyfish_drop = datetime.now()
last_bomb_drop = datetime.now()

jellyfish_x_positions = []
jellyfish_y_positions = []
bomb_x_positions = []
bomb_y_positions = []

jellyfish_reached_bottom = False
drop_speed = 20

bob_image = None
bob_x = 800
bob_y = 600
bob_speed = 20

score = 0

def load_bob_image():
    global bob_image
    bob_image = loadImage("bob.png")
    if bob_image:
        print("Bob's image loaded successfully.")
    else:
        print("Error loading Bob's image.")

def check_jellyfish_drop():
    global last_jellyfish_drop
    current_time = datetime.now()
    time_difference = current_time - last_jellyfish_drop
    if time_difference.total_seconds() >= randint(1, 5):
        last_jellyfish_drop = current_time
        return True
    return False

def check_bomb_drop():
    global last_bomb_drop
    current_time = datetime.now()
    time_difference = current_time - last_bomb_drop
    if time_difference.total_seconds() >= randint(1, 10):
        last_bomb_drop = current_time
        return True
    return False

def drop_entity():
    session = randint(1, 4)
    x = (session - 1) * width // 4
    y = 0
    if check_jellyfish_drop():
        jellyfish_x_positions.append(x)
        jellyfish_y_positions.append(y)
    if check_bomb_drop():
        bomb_x_positions.append(x)
        bomb_y_positions.append(y)

def draw_entities():
    global jellyfish_reached_bottom
    for i in range(len(jellyfish_x_positions)):
        jellyfish_y_positions[i] += drop_speed
        if jellyfish_y_positions[i] >= 1000:
            jellyfish_reached_bottom = True
        # Changing jellyfish image based on the score
        if score >= 30:
            image(loadImage("jf4.png"), jellyfish_x_positions[i], jellyfish_y_positions[i])
        elif score >= 20:
            image(loadImage("jf3.png"), jellyfish_x_positions[i], jellyfish_y_positions[i])
        elif score >= 10:
            image(loadImage("jf2.png"), jellyfish_x_positions[i], jellyfish_y_positions[i])
        else:
            image(loadImage("jf1.png"), jellyfish_x_positions[i], jellyfish_y_positions[i])
            
    for i in range(len(bomb_x_positions)):
        bomb_y_positions[i] += drop_speed
        image(loadImage("bomb.png"), bomb_x_positions[i], bomb_y_positions[i])

def setup():
    size(1800, 1000)
    background_image = loadImage("background.png")
    if background_image:
        print("Background image loaded successfully.")
    else:
        print("Error loading background image.")
    load_bob_image()

def keyPressed():
    global bob_x
    if key == 'a':
        bob_x -= bob_speed
    elif key == 'd':
        bob_x += bob_speed

def update_score(points):
    global score
    score += points
    if score <= 0:  # Check if score goes below 0
        score = 0
        print("Game Over!")
        noLoop()  # Stop the game

def display_score():
    textSize(48)
    fill(255)
    textAlign(RIGHT, TOP)
    text("Score: " + str(score), width - 10, 10)

def check_collision():
    global score
    for i in range(len(jellyfish_x_positions)):
        if bob_x + bob_image.width > jellyfish_x_positions[i] and bob_x < jellyfish_x_positions[i] + 100:
            if bob_y + bob_image.height > jellyfish_y_positions[i] and bob_y < jellyfish_y_positions[i] + 100:
                jellyfish_x_positions.pop(i)
                jellyfish_y_positions.pop(i)
                if score >= 30:
                    update_score(20)  # Double the score points earned
                elif score >= 20:
                    update_score(10)  # Double the score points earned
                else:
                    update_score(5)
                return True
    for i in range(len(bomb_x_positions)):
        if bob_x + bob_image.width > bomb_x_positions[i] and bob_x < bomb_x_positions[i] + 100:
            if bob_y + bob_image.height > bomb_y_positions[i] and bob_y < bomb_y_positions[i] + 100:
                bomb_x_positions.pop(i)
                bomb_y_positions.pop(i)
                if score >= 30:
                    update_score(-40)  # Double the score points lost
                elif score >= 20:
                    update_score(-20)  # Double the score points lost
                else:
                    update_score(-10)
                return True
    return False

def draw():
    global bob_x
    image(loadImage("background.png"), 0, 0)
    drop_entity()
    draw_entities()
    image(bob_image, bob_x, bob_y)
    if check_collision():
        return
    display_score()
