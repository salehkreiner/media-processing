from moviepy.editor import VideoFileClip
import os

def change_video_speed(video_path, output_path, speed_factor):
    # Load the video clip
    video_clip = VideoFileClip(video_path)

    # Modify the speed of the video clip
    modified_clip = video_clip.fx(vfx.speedx, speed_factor)

    # Write the modified video clip to a new file
    modified_clip.write_videofile(output_path, codec="libx264", audio_codec="aac", temp_audiofile="temp-audio.m4a", remove_temp=True)

if __name__ == "__main__":
    # Path to the input video file
    video_path = "input_video.mp4"

    # Get the duration of the input video
    video_duration = 60  # seconds

    # Prompt the user to enter the speed change percentage
    speed_change_percentage = float(input("Enter the speed change percentage (e.g., 130 for 30% faster, 50 for 50% slower): "))

    # Calculate the speed factor based on the input percentage
    speed_factor = speed_change_percentage / 100.0

    # If speed factor is 1.0 (100%), no change is needed
    if speed_factor == 1.0:
        print("No speed change needed.")
    else:
        # Calculate the new duration of the video after speed change
        new_duration = video_duration / speed_factor

        # Generate a unique name for the output file
        output_path = f"output_video_{speed_change_percentage}percent.mp4"

        # Change the speed of the video and save it to a new file
        change_video_speed(video_path, output_path, speed_factor)

    print("Process completed.")
