import os
import webbrowser
from pytube import YouTube
from moviepy.editor import VideoFileClip
import pygame
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from threading import Thread

def sanitize_filename(filename):
    # Remove characters that are not suitable for filenames
    sanitized_filename = "".join([c for c in filename if c.isalnum() or c.isspace()])
    sanitized_filename = sanitized_filename.replace(" ", "_")
    return sanitized_filename

def download_and_convert_video(youtube_url, output_directory):
    try:
        # Create a YouTube object from the URL
        yt = YouTube(youtube_url)

        # Get the video title and sanitize it for filename
        video_title = yt.title
        sanitized_title = sanitize_filename(video_title)

        # Get the highest resolution stream available
        stream = yt.streams.get_highest_resolution()

        # Create a directory for temporary video storage
        temp_video_directory = "temp_video"
        if not os.path.exists(temp_video_directory):
            os.makedirs(temp_video_directory)

        # Download the video
        video_filename = f"{sanitized_title}.mp4"
        video_path = os.path.join(temp_video_directory, video_filename)
        stream.download(output_path=temp_video_directory, filename=video_filename)

        # Convert the video to audio
        video = VideoFileClip(video_path)
        audio = video.audio

        # Save the audio with the same title as the video to the specified directory
        output_audio_path = os.path.join(output_directory, f"{sanitized_title}.wav")
        audio.write_audiofile(output_audio_path)

        # Close video and audio objects
        video.close()
        audio.close()

        # Remove temporary video and directory
        os.remove(video_path)
        os.rmdir(temp_video_directory)

        return output_audio_path
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None

def play_audio(audio_path):
    pygame.mixer.init()
    pygame.mixer.music.load(audio_path)
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(1.0)

def open_youtube_video():
    search_query = entry.get()
    url = f"https://www.youtube.com/results?search_query={search_query}"
    webbrowser.open(url)

def download_and_play_audio():
    youtube_url = url_entry.get()

    def download_and_play():
        # Ask the user for the download directory
        download_directory = filedialog.askdirectory(title="Chọn thư mục lưu trữ")
        if download_directory:
            audio_path = download_and_convert_video(youtube_url, download_directory)
            if audio_path:
                play_audio(audio_path)

    # Create a thread for downloading and playing audio
    audio_thread = Thread(target=download_and_play)
    audio_thread.start()

# Create the GUI window
root = tk.Tk()
root.title("YouTube Video to Audio")

# Create the input frame
frame = ttk.Frame(root)
frame.grid(column=0, row=0, padx=10, pady=10)

search_label = ttk.Label(frame, text="Tìm kiếm video trên YouTube:")
search_label.grid(column=0, row=0)

entry = ttk.Entry(frame, width=40)
entry.grid(column=1, row=0)

search_button = ttk.Button(frame, text="Tìm kiếm", command=open_youtube_video)
search_button.grid(column=2, row=0)

url_label = ttk.Label(frame, text="URL video YouTube:")
url_label.grid(column=0, row=1)

url_entry = ttk.Entry(frame, width=40)
url_entry.grid(column=1, row=1)

download_button = ttk.Button(frame, text="Tải và Phát âm thanh", command=download_and_play_audio)
download_button.grid(column=2, row=1)

# Run the application
root.mainloop()
