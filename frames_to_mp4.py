import os
import cv2

def images_to_video(image_folder, video_name, fps=12):
    # Get the list of image files in the folder
    image_files = [os.path.join(image_folder, f) for f in os.listdir(image_folder) if f.endswith(('.png', '.jpg', '.jpeg', '.gif'))]

    # Sort the image files by name
    image_files.sort()

    # Get the first image to obtain its dimensions
    img = cv2.imread(image_files[0])
    height, width, _ = img.shape

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(video_name, fourcc, fps, (width, height))

    # Loop through each image file and write it to the video
    for image_file in image_files:
        img = cv2.imread(image_file)
        out.write(img)

    # Release the VideoWriter object
    out.release()

if __name__ == "__main__":
    # Folder containing the input images
    image_folder = "input_images"
    
    # Name of the output video file
    video_name = "output_video.mp4"
    
    # Frames per second for the output video
    fps = 12
    
    # Convert images to video
    images_to_video(image_folder, video_name, fps)
