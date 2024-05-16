from moviepy.editor import VideoFileClip, AudioFileClip

def overlay_audio(video_path, audio_path, output_path):
    # Load the video clip
    video_clip = VideoFileClip(video_path)

    # Load the audio clip
    audio_clip = AudioFileClip(audio_path)

    # Set the audio clip duration to match the video clip duration
    audio_clip = audio_clip.set_duration(video_clip.duration)

    # Overlay the audio onto the video
    video_with_audio = video_clip.set_audio(audio_clip)

    # Write the video with overlayed audio to a new file
    video_with_audio.write_videofile(output_path, codec="libx264", audio_codec="aac", temp_audiofile="temp-audio.m4a", remove_temp=True)

if __name__ == "__main__":
    # Path to the input video file
    video_path = "input_video.mp4"
    
    # Path to the audio file to overlay
    audio_path = "audio_file.mp3"
    
    # Output path for the final video with audio overlay
    output_path = "output_video_with_audio.mp4"
    
    # Overlay the audio onto the video
    overlay_audio(video_path, audio_path, output_path)
