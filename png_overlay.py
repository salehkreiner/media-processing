from PIL import Image

def overlay_images(background_path, overlay_paths, overlay_positions, overlay_sizes):
    # Open the background image
    background = Image.open(background_path).convert("RGBA")
    
    # Loop through each overlay image path
    for overlay_path, position, size in zip(overlay_paths, overlay_positions, overlay_sizes):
        # Open the overlay image
        overlay = Image.open(overlay_path).convert("RGBA")
        
        # Resize the overlay image if necessary
        if size:
            overlay = overlay.resize(size)
        
        # Paste the overlay onto the background at the specified position
        background.paste(overlay, position, overlay)
    
    # Display the final image
    background.show()

if __name__ == "__main__":
    # Path to the background image
    background_path = "background.png"
    
    # Paths to the overlay images
    overlay_paths = ["overlay1.png", "overlay2.png", "overlay3.png"]
    
    # Positions where the overlay images will be placed
    overlay_positions = [(100, 100), (200, 200), (300, 300)]
    
    # Sizes to which the overlay images will be resized (None for no resizing)
    overlay_sizes = [(None, None), (50, 50), (150, 150)]
    
    # Overlay the images onto the background
    overlay_images(background_path, overlay_paths, overlay_positions, overlay_sizes)
