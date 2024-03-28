# Declare global variables for character image and its position
bob_image = None
bob_x = 400  # Initial x-position of Bob
bob_y = 500  # Initial y-position of Bob

# Load the character image
def setup():
    global bob_image
    size(800, 600)  # Set the size of the canvas
    bob_image = loadImage("bob.png")  # Load Bob's image

# Draw Bob on the canvas
def draw():
    global bob_x
    global bob_y
    global bob_image
    
    background(255)  # Clear the background
    
    # Draw Bob at his current position
    image(bob_image, bob_x, bob_y)
    
# Move Bob left or right based on key presses
def keyPressed():
    global bob_x
    
    # Move Bob left
    if key == 'a' or key == 'A':
        bob_x -= 10
    
    # Move Bob right
    if key == 'd' or key == 'D':
        bob_x += 10
