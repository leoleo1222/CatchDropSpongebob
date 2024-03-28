# Import necessary libraries
from random import randint
from datetime import datetime

# Variables to store last dropped time
last_drop = datetime.now()

# Lists to store x and y coordinates of dropped items
entities_x_positions = []
entities_y_positions = []

# Speed of dropping
drop_speed = 40  # Adjust this value to change the speed of dropping

# Function to check if it's time to drop an entity
def check_entity_drop():
    global last_drop
    current_time = datetime.now()
    time_difference = current_time - last_drop
    if time_difference.total_seconds() >= randint(1, 2):
        last_drop = current_time
        return True
    return False

# Function to drop an entity (either bomb or jellyfish)
def drop_entity():
    x = randint(0, width)  # Random x-coordinate within canvas width
    y = 0  # Start from the top
    if check_entity_drop():
        entity_type = randint(0, 1)  # 0 for bomb, 1 for jellyfish
        entities_x_positions.append(x)
        entities_y_positions.append(y)
        return entity_type  # Return the type of dropped entity (0 for bomb, 1 for jellyfish)
    return None

# Function to draw entities
def draw_entities():
    for i in range(len(entities_x_positions)):
        entities_y_positions[i] += drop_speed  # Update y-coordinate for dropping effect
        # Draw bomb or jellyfish based on entity type
        if i % 2 == 0:
            image(loadImage("bomb.png"), entities_x_positions[i], entities_y_positions[i])
        else:
            image(loadImage("jellyfish.png"), entities_x_positions[i], entities_y_positions[i])

# Setup function to initialize the canvas
def setup():
    size(1800, 1000)
    background_image = loadImage("background.png")
    if background_image:
        print("Background image loaded successfully.")
    else:
        print("Error loading background image.")

# Draw function to draw entities
def draw():
    image(loadImage("background.png"), 0, 0)
    entity_type = drop_entity()
    draw_entities()
