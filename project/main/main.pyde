# Import necessary libraries
from random import randint
from datetime import datetime, timedelta

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

# Timer
start_time = datetime.now()
timer_duration = timedelta(seconds=60)

# Stage and Round
current_stage = 1
current_round = 1

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
    if time_difference.total_seconds() >= randint(5, 10):
        last_bomb_drop = current_time
        return True
    return False

def drop_entity():
    session = randint(1, 4)
    x = (session - 1) * width // 4
    y = 0
    if current_stage == 3:  # Only drop bombs in stage 3
        if check_bomb_drop():
            bomb_x_positions.append(x)
            bomb_y_positions.append(y)
    else:
        if check_jellyfish_drop():
            jellyfish_x_positions.append(x)
            jellyfish_y_positions.append(y)

def draw_entities():
    global jellyfish_reached_bottom, drop_speed
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
    frameRate(30);
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

# Function to display the score
def display_score():
    global start_time
    textSize(48)  # Larger text size
    fill(255)
    textAlign(LEFT, TOP)
    elapsed_time = datetime.now() - start_time
    remaining_time = timer_duration - elapsed_time
    text("Time left: " + str(remaining_time.seconds), 10, 10)  # Display timer
    textAlign(RIGHT, TOP)
    text("Score: " + str(score), width - 10, 60)  # Display score
    textAlign(CENTER, TOP)
    text("Stage: " + str(current_round), width // 2, 10)  # Display round

def check_collision():
    global score
    for i in range(len(jellyfish_x_positions)):
        if bob_x + bob_image.width > jellyfish_x_positions[i] - 100 and bob_x < jellyfish_x_positions[i] + 355:
            if bob_y + bob_image.height > jellyfish_y_positions[i] and bob_y < jellyfish_y_positions[i] + 400:
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
        if bob_x + bob_image.width > bomb_x_positions[i] and bob_x < bomb_x_positions[i] + 220:
            if bob_y + bob_image.height > bomb_y_positions[i] and bob_y < bomb_y_positions[i] + 220:
                bomb_x_positions.pop(i)
                bomb_y_positions.pop(i)
                if score >= 30:
                    update_score(-20)  # Double the score points lost
                elif score >= 20:
                    update_score(-10)  # Double the score points lost
                else:
                    update_score(-3)
                return True
    return False

def draw():
    global bob_x, current_stage, current_round, drop_speed, start_time, timer_duration

    # Check if timer has reached 60 seconds
    elapsed_time = datetime.now() - start_time
    if elapsed_time >= timer_duration:
        # Reset timer
        start_time = datetime.now()
        elapsed_time = timedelta(seconds=0)
        
        # Increment stage and round
        if current_stage == 1 and score >= 10:
            current_stage = 2
            drop_speed += 5  # Increase drop speed for stage 2
        elif current_stage == 2 and score >= 20:
            current_stage = 3
            current_round += 1
            drop_speed += 5  # Increase drop speed for stage 3

    image(loadImage("background.png"), 0, 0)
    print(jellyfish_reached_bottom)
    
    drop_entity()
    draw_entities()
    image(bob_image, bob_x, bob_y)
    if check_collision():
        return
    display_score()  # Display the score
