# Import necessary libraries
from random import randint
from datetime import datetime

# Variables to store last dropped times for jellyfish and bomb
last_jellyfish_drop = datetime.now()
last_bomb_drop = datetime.now()

# Function to check if it's time to drop a jellyfish
def check_jellyfish_drop():
    global last_jellyfish_drop
    current_time = datetime.now()
    time_difference = current_time - last_jellyfish_drop
    if time_difference.total_seconds() >= randint(1, 3):
        last_jellyfish_drop = current_time
        return True
    return False

# Function to check if it's time to drop a bomb
def check_bomb_drop():
    global last_bomb_drop
    current_time = datetime.now()
    time_difference = current_time - last_bomb_drop
    if time_difference.total_seconds() >= randint(1, 2):
        last_bomb_drop = current_time
        return True
    return False

# Function to drop jellyfish or bomb in a random session
def drop_entity():
    session = randint(1, 4)  # Randomly select one of the four sessions
    x = (session - 1) * width // 4  # Calculate x-coordinate based on session
    y = 0  # Start from the top
    if check_jellyfish_drop():
        image(loadImage("jf{}.png".format(randint(1, 4))), x, y)
    if check_bomb_drop():
        image(loadImage("bomb.png"), x, y)

# Setup function to initialize the canvas
def setup():
    size(2000, 1000)
    background_image = loadImage("background.png")
    if background_image:
        print("Background image loaded successfully.")
    else:
        print("Error loading background image.")

# Draw function to draw the entities
def draw():
    image(loadImage("background.png"), 0, 0)
    drop_entity()
