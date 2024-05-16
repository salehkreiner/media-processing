from moviepy.editor import VideoFileClip, AudioFileClip
import moviepy.editor as mp

def change_video_speed_with_audio(video_path, audio_path, output_path, speed_factor):
    # Load the video clip
    video_clip = VideoFileClip(video_path)

    # Load the audio clip
    audio_clip = AudioFileClip(audio_path)

    # Modify the speed of the video clip
    modified_video_clip = video_clip.fx(mp.vfx.speedx, speed_factor)

    # Modify the speed of the audio clip with pitch correction
    modified_audio_clip = audio_clip.fx(mp.audio.speedx, speed_factor)

    # Set the duration of the modified audio clip to match the duration of the video clip
    modified_audio_clip = modified_audio_clip.subclip(0, modified_video_clip.duration)

    # Combine the modified video clip with the modified audio clip
    video_with_audio = modified_video_clip.set_audio(modified_audio_clip)

    # Write the resulting video with audio to a new file
    video_with_audio.write_videofile(output_path, codec="libx264", audio_codec="aac", temp_audiofile="temp-audio.m4a", remove_temp=True)

if __name__ == "__main__":
    # Path to the input video file
    video_path = "input_video.mp4"

    # Path to the audio file
    audio_path = "input_audio.mp3"
    
    # Output path for the resulting video with audio
    output_path = "output_video_with_audio.mp4"

    # Speed factor (e.g., 1.5 for 50% faster, 0.5 for 50% slower)
    speed_factor = float(input("Enter the speed factor (1.0 for no change): "))

    # Change the speed of the video and audio while maintaining the original pitch
    change_video_speed_with_audio(video_path, audio_path, output_path, speed_factor)

    print("Process completed.")
