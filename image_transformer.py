from PIL import Image, ImageEnhance, ImageFilter, ImageOps, ImageTransform
import os

class ImageTransformer:
    def __init__(self, image_path):
        self.image = Image.open(image_path)
        self.output_dir = "transformed_images"
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def rotate_image(self, angle):
        rotated_image = self.image.rotate(angle)
        rotated_image.save(os.path.join(self.output_dir, "rotated_image.png"))

    def warp_image(self, matrix):
        warped_image = self.image.transform(self.image.size, ImageTransform.AFFINE, matrix)
        warped_image.save(os.path.join(self.output_dir, "warped_image.png"))

if __name__ == "__main__":
    # Path to the input image file
    input_image_path = "input_image.png"

    # Create an instance of ImageTransformer
    transformer = ImageTransformer(input_image_path)

    # Rotate the image by 45 degrees
    transformer.rotate_image(45)

    # Warp the image using an affine transformation matrix
    affine_matrix = (1, 0.5, 0, 0, 1, 0)
    transformer.warp_image(affine_matrix)

    print("Transformations applied successfully.")
