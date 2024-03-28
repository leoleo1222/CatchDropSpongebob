# main.pyde

# Set up the size of the canvas
def setup():
    size(1800, 1000)  # Set the size of the canvas to match your background image
    
    # Load the background image
    background_image = loadImage("background.png")
    
    # Check if the image is loaded successfully
    if background_image:
        print("Background image loaded successfully.")
    else:
        print("Error loading background image.")

# Draw function to set the background image
def draw():
    # Draw the background image
    image(loadImage("background.png"), 0, 0)

# Call the game.pyde file
exec(open("game.pyde").read())
