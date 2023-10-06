import tkinter as tk
import random
import webbrowser
import os
from pytube import YouTube
from threading import Thread
from tkinter import filedialog

# Create the GUI window
window = tk.Tk()
window.title("YouTube Video Player")
window.geometry("400x300")

# Function to sanitize a filename
def sanitize_filename(filename):
    sanitized_filename = "".join([c for c in filename if c.isalnum() or c.isspace()])
    sanitized_filename = sanitized_filename.replace(" ", "_")
    return sanitized_filename

# Function to download a YouTube video
def download_video(youtube_url, output_directory):
    try:
        yt = YouTube(youtube_url)
        video_title = yt.title
        sanitized_title = sanitize_filename(video_title)
        stream = yt.streams.get_highest_resolution()
        video_filename = f"{sanitized_title}.mp4"
        video_path = os.path.join(output_directory, video_filename)
        stream.download(output_path=output_directory, filename=video_filename)
        return video_path
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None

# Function to play video
def play_video(video_path):
    webbrowser.open(video_path)

# Function to open YouTube video in a web browser
def open_youtube_video():
    search_query = entry.get()
    url = f"https://www.youtube.com/results?search_query={search_query}"
    webbrowser.open(url)

# Function to download and play video from a YouTube link
def download_and_play_video():
    youtube_url = url_entry.get()

    def download_and_play():
        download_directory = filedialog.askdirectory(title="Chọn thư mục lưu trữ")
        if download_directory:
            video_path = download_video(youtube_url, download_directory)
            if video_path:
                play_video(video_path)

    video_thread = Thread(target=download_and_play)
    video_thread.start()

# Function to play random video from the playlist
def play_random_video():
    if playlist:
        random_video = random.choice(playlist)
        play_video(random_video)
        current_video_label.config(text="Video hiện tại: " + os.path.basename(random_video))
    else:
        current_video_label.config(text="Không có video trong danh sách")

# Function to add video to the playlist
def add_video_to_playlist():
    file_paths = filedialog.askopenfilenames(title="Chọn video")
    if file_paths:
        playlist.extend(file_paths)

# Create a frame for the YouTube section
youtube_frame = tk.Frame(window)
youtube_frame.pack()

# Entry for YouTube search
entry = tk.Entry(youtube_frame, width=40)
entry.grid(column=0, row=0)

# Button to search YouTube
search_button = tk.Button(youtube_frame, text="Tìm kiếm YouTube", command=open_youtube_video)
search_button.grid(column=1, row=0)

# Entry for YouTube URL
url_entry = tk.Entry(youtube_frame, width=40)
url_entry.grid(column=0, row=1)

# Button to download and play YouTube video
download_button = tk.Button(youtube_frame, text="Tải Video", command=download_and_play_video)
download_button.grid(column=1, row=1)

# Create a frame for the video player
video_frame = tk.Frame(window)
video_frame.pack()

# Button to play random video
play_button = tk.Button(video_frame, text="Xem Video Ngẫu Nhiên", command=play_random_video)
play_button.pack()

# Label to display current video
current_video_label = tk.Label(video_frame, text="Video hiện tại: ")
current_video_label.pack()

# Button to exit the application
exit_button = tk.Button(window, text="Thoát", command=window.quit)
exit_button.pack()

# Button to add video to the playlist
add_video_button = tk.Button(video_frame, text="Chọn Video", command=add_video_to_playlist)
add_video_button.pack()

# Create a playlist to store downloaded videos
playlist = []

# Run the application
window.mainloop()
