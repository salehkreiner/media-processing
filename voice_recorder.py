import sounddevice as sd
import wavio
import time

def record_audio(duration, filename):
    if duration < 5 or duration > 60:
        raise ValueError("Duration must be between 5 and 60 seconds")

    # Sampling rate
    fs = 44100  # Sample rate in Hz
    print(f"Recording for {duration} seconds...")

    # Record audio
    myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=2, dtype='int16')
    sd.wait()  # Wait until recording is finished
    print("Recording finished")

    # Save as WAV file
    wavio.write(filename, myrecording, fs, sampwidth=2)
    print(f"Audio saved as {filename}")

if __name__ == "__main__":
    duration = float(input("Enter the duration of the recording (5-60 seconds): "))
    filename = input("Enter the filename to save the recording (e.g., 'output.wav'): ")
    record_audio(duration, filename)
