from PIL import Image, ImageEnhance, ImageFilter, ImageOps
import os

def brighten_image(image_path, output_path, factor):
    image = Image.open(image_path)
    enhancer = ImageEnhance.Brightness(image)
    brightened_image = enhancer.enhance(factor)
    brightened_image.save(output_path)

def apply_monotone_effect(image_path, output_path, color):
    image = Image.open(image_path).convert('L')
    monotone_image = ImageOps.colorize(image, black=color, white=color)
    monotone_image.save(output_path)

def apply_blur_effect(image_path, output_path, radius):
    image = Image.open(image_path)
    blurred_image = image.filter(ImageFilter.GaussianBlur(radius))
    blurred_image.save(output_path)

if __name__ == "__main__":
    # Path to the input PNG image file
    input_image_path = "input_image.png"

    # Create a directory to store output images if it doesn't exist
    output_dir = "output_images"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Apply brighten effect
    brighten_image(input_image_path, os.path.join(output_dir, "brightened_image.png"), factor=1.5)

    # Apply monotone effect
    apply_monotone_effect(input_image_path, os.path.join(output_dir, "monotone_image.png"), color="#FF0000")

    # Apply blur effect
    apply_blur_effect(input_image_path, os.path.join(output_dir, "blurred_image.png"), radius=5)

    print("Effects applied successfully.")
