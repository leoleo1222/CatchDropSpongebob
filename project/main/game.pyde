# Import necessary libraries
from random import randint
from datetime import datetime

# Variables to store last dropped times for jellyfish and bomb
last_jellyfish_drop = datetime.now()
last_bomb_drop = datetime.now()

# Lists to store x and y coordinates of dropped items
jellyfish_x_positions = []
jellyfish_y_positions = []
bomb_x_positions = []
bomb_y_positions = []

# Flag to indicate if a jellyfish has reached 1000 in the y-axis
jellyfish_reached_bottom = False

# Speed of dropping
drop_speed = 20  # Adjust this value to change the speed of dropping

# Bob's properties
bob_image = None
bob_x = 800  # Initial x-coordinate for Bob
bob_y = 800  # Initial y-coordinate for Bob
bob_speed = 20  # Speed of Bob's movement

# Function to load Bob's image
def load_bob_image():
    global bob_image
    bob_image = loadImage("bob.png")
    if bob_image:
        print("Bob's image loaded successfully.")
    else:
        print("Error loading Bob's image.")

# Function to check if it's time to drop a jellyfish
def check_jellyfish_drop():
    global last_jellyfish_drop
    current_time = datetime.now()
    time_difference = current_time - last_jellyfish_drop
    if time_difference.total_seconds() >= randint(1, 5):
        last_jellyfish_drop = current_time
        return True
    return False

# Function to check if it's time to drop a bomb
def check_bomb_drop():
    global last_bomb_drop
    current_time = datetime.now()
    time_difference = current_time - last_bomb_drop
    if time_difference.total_seconds() >= randint(1, 10):
        last_bomb_drop = current_time
        return True
    return False

# Function to drop jellyfish or bomb in a random session
def drop_entity():
    session = randint(1, 4)  # Randomly select one of the four sessions
    x = (session - 1) * width // 4  # Calculate x-coordinate based on session
    y = 0  # Start from the top
    if check_jellyfish_drop():
        jellyfish_x_positions.append(x)
        jellyfish_y_positions.append(y)
    if check_bomb_drop():
        bomb_x_positions.append(x)
        bomb_y_positions.append(y)

# Function to draw jellyfish and bombs
def draw_entities():
    global jellyfish_reached_bottom
    for i in range(len(jellyfish_x_positions)):
        jellyfish_y_positions[i] += drop_speed  # Update y-coordinate for dropping effect
        if jellyfish_y_positions[i] >= 1000:
            jellyfish_reached_bottom = True
        image(loadImage("jf1.png".format(randint(1, 4))), jellyfish_x_positions[i], jellyfish_y_positions[i])
    for i in range(len(bomb_x_positions)):
        bomb_y_positions[i] += drop_speed  # Update y-coordinate for dropping effect
        image(loadImage("bomb.png"), bomb_x_positions[i], bomb_y_positions[i])

# Setup function to initialize the canvas
def setup():
    size(1800, 1000)
    background_image = loadImage("background.png")
    if background_image:
        print("Background image loaded successfully.")
    else:
        print("Error loading background image.")
    load_bob_image()  # Load Bob's image

# Function to handle key presses
def keyPressed():
    global bob_x
    if key == 'a':
        bob_x -= bob_speed  # Move Bob left
    elif key == 'd':
        bob_x += bob_speed  # Move Bob right

# Draw function to draw the entities
def draw():
    global bob_x
    image(loadImage("background.png"), 0, 0)
    image(loadImage("bob.png"), 0, 0)  # Draw Bob at his current position
    drop_entity()
    draw_entities()
    
