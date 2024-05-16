from PIL import Image

def create_animation(background_path, foreground_path, output_path, animation_speed):
    # Open the background and foreground images
    background = Image.open(background_path)
    foreground = Image.open(foreground_path)

    # Get the dimensions of the background image
    bg_width, bg_height = background.size

    # Calculate the initial position of the foreground image
    fg_x = 0
    fg_y = (bg_height - foreground.height) // 2

    # Create an empty list to store frames of the animation
    frames = []

    # Create the animation frames
    while True:
        # Create a new frame by pasting the background image
        frame = background.copy()

        # Paste the foreground image onto the frame at the current position
        frame.paste(foreground, (fg_x, fg_y), foreground)

        # Append the frame to the list of frames
        frames.append(frame)

        # Move the foreground image to the right
        fg_x += animation_speed

        # If the foreground image moves off the right edge of the background, reverse its direction
        if fg_x >= bg_width:
            fg_x = bg_width - 1
            animation_speed = -animation_speed

        # If the foreground image moves off the left edge of the background, reverse its direction
        elif fg_x < 0:
            fg_x = 0
            animation_speed = -animation_speed

    # Save the frames as an animated GIF
    frames[0].save(output_path, save_all=True, append_images=frames[1:], loop=0, duration=50)

if __name__ == "__main__":
    # Path to the background JPEG image
    background_path = "background.jpg"

    # Path to the foreground PNG image with transparency
    foreground_path = "foreground.png"

    # Output path for the animated GIF
    output_path = "animation.gif"

    # Animation speed (pixels per frame)
    animation_speed = 5

    # Create the animation
    create_animation(background_path, foreground_path, output_path, animation_speed)

    print("Animation created successfully.")
