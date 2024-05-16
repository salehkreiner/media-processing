from PIL import Image

def create_animation(background_path, foreground_path, output_path, animation_speed_x, animation_speed_y):
    # Open the background and foreground images
    background = Image.open(background_path)
    foreground = Image.open(foreground_path)

    # Get the dimensions of the background image
    bg_width, bg_height = background.size

    # Get the dimensions of the foreground image
    fg_width, fg_height = foreground.size

    # Initial position of the foreground image
    fg_x = 0
    fg_y = 0

    # Direction of movement along X-axis and Y-axis
    dx = animation_speed_x
    dy = animation_speed_y

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

        # Move the foreground image
        fg_x += dx
        fg_y += dy

        # If the foreground image hits the right edge, reverse the direction along the X-axis
        if fg_x + fg_width >= bg_width or fg_x < 0:
            dx = -dx

        # If the foreground image hits the bottom edge, reverse the direction along the Y-axis
        if fg_y + fg_height >= bg_height or fg_y < 0:
            dy = -dy

    # Save the frames as an animated GIF
    frames[0].save(output_path, save_all=True, append_images=frames[1:], loop=0, duration=50)

if __name__ == "__main__":
    # Path to the background JPEG image
    background_path = "background.jpg"

    # Path to the foreground PNG image with transparency
    foreground_path = "foreground.png"

    # Output path for the animated GIF
    output_path = "animation.gif"

    # Animation speed (pixels per frame) along X-axis and Y-axis
    animation_speed_x = 5
    animation_speed_y = 3

    # Create the animation
    create_animation(background_path, foreground_path, output_path, animation_speed_x, animation_speed_y)

    print("Animation created successfully.")
