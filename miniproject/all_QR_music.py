import tkinter as tk  # Thư viện để tạo giao diện đồ họa
import random
import webbrowser
import pygame  # Thư viện để phát âm thanh
import os
import qrcode  # Thư viện để tạo mã QR
from tkinter import ttk
from pytube import YouTube  # Thư viện để tải video từ YouTube
from moviepy.editor import VideoFileClip  # Thư viện để xử lý video
from threading import Thread  # Thư viện để xử lý đa luồng
from tkinter import filedialog

from PIL import Image, ImageTk  # Thư viện để làm việc với hình ảnh

# Khởi tạo pygame để phát âm thanh
pygame.init()

# Tạo cửa sổ GUI (giao diện đồ họa)
window = tk.Tk()
window.title("Trình Tải Nhạc từ YouTube")
window.geometry("400x300")

# Hàm để làm sạch tên tệp (xóa ký tự đặc biệt không hợp lệ)
def sanitize_filename(filename):
    sanitized_filename = "".join([c for c in filename if c.isalnum() or c.isspace()])
    sanitized_filename = sanitized_filename.replace(" ", "_")
    return sanitized_filename

# Hàm để tải về và chuyển đổi video từ YouTube thành âm thanh
def download_and_convert_video(youtube_url, output_directory):
    try:
        yt = YouTube(youtube_url, on_progress_callback=None, on_complete_callback=None)
        video_title = yt.title
        sanitized_title = sanitize_filename(video_title)
        stream = yt.streams.get_highest_resolution()
        temp_video_directory = "temp_video"
        if not os.path.exists(temp_video_directory):
            os.makedirs(temp_video_directory)
        video_filename = f"{sanitized_title}.mp4"
        video_path = os.path.join(temp_video_directory, video_filename)
        stream.download(output_path=temp_video_directory, filename=video_filename)
        video = VideoFileClip(video_path)
        audio = video.audio
        output_audio_path = os.path.join(output_directory, f"{sanitized_title}.wav")
        audio.write_audiofile(output_audio_path)
        video.close()
        audio.close()
        os.remove(video_path)
        os.rmdir(temp_video_directory)
        
        # Thêm bài hát đã tải vào danh sách phát
        playlist.append(output_audio_path)
        
        return output_audio_path
    except Exception as e:
        print(f"Đã xảy ra lỗi: {str(e)}")
        return None

# Hàm để phát âm thanh
def play_audio(audio_path):
    global current_audio_path
    current_audio_path = audio_path

    def play_thread():
        pygame.mixer.music.load(audio_path)
        pygame.mixer.music.play()
        # Lấy thời lượng của bài hát và cài đặt nó cho thanh trượt tiến trình
        audio = pygame.mixer.Sound(audio_path)
        duration = audio.get_length()
        progress_scale.config(to=duration)
        while pygame.mixer.music.get_busy():
            window.update()
            continue

    audio_thread = Thread(target=play_thread)
    audio_thread.start()

# Hàm để mở video YouTube trong trình duyệt web
def open_youtube_video():
    search_query = entry.get()
    url = f"https://www.youtube.com/results?search_query={search_query}"
    webbrowser.open(url)

# Hàm để tải về và phát âm thanh từ YouTube
def download_and_play_audio():
    youtube_url = url_entry.get()

    def download_and_play():
        download_directory = filedialog.askdirectory(title="Chọn thư mục lưu trữ")
        if download_directory:
            audio_path = download_and_convert_video(youtube_url, download_directory)
            if audio_path:
                play_audio(audio_path)
                update_progress()  # Bắt đầu cập nhật thanh trượt tiến trình khi bắt đầu phát

    audio_thread = Thread(target=download_and_play)
    audio_thread.start()

# Hàm để phát âm nhạc ngẫu nhiên từ danh sách phát
def play_random_music():
    global current_song_index

    if playlist:
        current_song_index = random.randint(0, len(playlist) - 1)
        audio_path = playlist[current_song_index]
        play_audio(audio_path)
        current_music_label.config(text="Bài hát: " + os.path.basename(audio_path))
        progress_scale.set(0)  # Đặt thanh trượt về vị trí ban đầu
        on_progress_scale_release(None)  # Đặt thời gian bắt đầu bài hát
    else:
        current_music_label.config(text="Không có bài hát trong danh sách")


# Hàm để cập nhật thanh trượt tiến trình phát âm thanh
def update_progress():
    current_time = pygame.mixer.music.get_pos() / 1000
    progress_scale.set(current_time)
    if pygame.mixer.music.get_busy():
        window.after(1000, update_progress)

# Hàm được gọi khi người dùng thả thanh trượt tiến trình
def on_progress_scale_release(event):
    current_time = progress_scale.get()
    pygame.mixer.music.rewind()
    pygame.mixer.music.set_pos(current_time)

# Hàm để thêm âm nhạc vào danh sách phát
def add_music_to_playlist():
    file_paths = filedialog.askopenfilenames(title="Chọn nhiều bài hát")
    if file_paths:
        playlist.extend(file_paths)

# Hàm để tạo mã QR từ nội dung tùy chỉnh
def generate_qr_code():
    qr_content = qr_entry.get()  # Lấy nội dung tùy chỉnh cho mã QR
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data(qr_content)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="black", back_color="white")
    # Hiển thị mã QR trong cửa sổ mới
    qr_window = tk.Toplevel(window)
    qr_window.title("Mã QR")
    qr_img = ImageTk.PhotoImage(qr_img)
    qr_label = ttk.Label(qr_window, image=qr_img)
    qr_label.image = qr_img
    qr_label.pack()

# Biến toàn cục để theo dõi bài hát hiện tại trong danh sách phát
current_song_index = 0

# Hàm để phát bài hát tiếp theo trong danh sách phát
def play_next_song():
    global current_song_index
    if playlist:
        current_song_index += 1
        if current_song_index >= len(playlist):
            current_song_index = 0  # Quay lại bài đầu tiên nếu đã đến cuối danh sách
        audio_path = playlist[current_song_index]
        play_audio(audio_path)
        current_music_label.config(text="Bài hát: " + os.path.basename(audio_path))
        progress_scale.set(0)  # Đặt thanh trượt về vị trí ban đầu
        on_progress_scale_release(None)  # Đặt thời gian bắt đầu bài hát

# Biến toàn cục để theo dõi trạng thái tạm dừng
is_paused = False
current_audio_path = None
def pause_resume_music():
    global is_paused
    if pygame.mixer.music.get_busy():
        if is_paused:
            pygame.mixer.music.unpause()
            is_paused = False
            pause_button.config(text="Tạm Dừng")
        else:
            pygame.mixer.music.pause()
            is_paused = True
            pause_button.config(text="Tiếp Tục")


# Tạo một khung cho phần YouTube
youtube_frame = ttk.Frame(window)
youtube_frame.pack()

# Nhập nội dung tùy chỉnh cho mã QR
qr_entry = ttk.Entry(youtube_frame, width=40)
qr_entry.grid(column=0, row=0)

# Nút để tạo và hiển thị mã QR
generate_qr_button = ttk.Button(youtube_frame, text="Tạo QR", command=generate_qr_code)
generate_qr_button.grid(column=1, row=0)

# Nhập tìm kiếm YouTube
entry = ttk.Entry(youtube_frame, width=40)
entry.grid(column=0, row=1)

# Nút để tìm kiếm YouTube
search_button = ttk.Button(youtube_frame, text="Tìm kiếm YouTube", command=open_youtube_video)
search_button.grid(column=1, row=1)

# Nhập URL YouTube
url_entry = ttk.Entry(youtube_frame, width=40)
url_entry.grid(column=0, row=2)

# Nút để tải về và phát âm thanh từ YouTube
download_button = ttk.Button(youtube_frame, text="Tải MP3", command=download_and_play_audio)
download_button.grid(column=1, row=2)

# Tạo khung cho trình phát âm nhạc
music_frame = ttk.Frame(window)
music_frame.pack()

# Nút để phát âm nhạc ngẫu nhiên
play_button = ttk.Button(music_frame, text="Phát Nhạc Ngẫu Nhiên", command=play_random_music)
play_button.pack()

# Nhãn để hiển thị âm nhạc hiện tại
current_music_label = ttk.Label(music_frame, text="Bài hát: ")
current_music_label.pack()

# Thanh trượt tiến trình
progress_scale = ttk.Scale(music_frame, orient="horizontal", length=300)
progress_scale.bind("<ButtonRelease-1>", on_progress_scale_release)
progress_scale.pack()

# Nút để chuyển đến bài hát tiếp theo
next_song_button = ttk.Button(music_frame, text="Bài Hát Tiếp Theo", command=play_next_song)
next_song_button.pack()

# Nút để tạm dừng hoặc tiếp tục bài hát
pause_button = ttk.Button(music_frame, text="Tạm Dừng", command=pause_resume_music)
pause_button.pack()

# Nút để thêm âm nhạc vào danh sách phát
add_music_button = ttk.Button(music_frame, text="Thêm Bài Hát", command=add_music_to_playlist)
add_music_button.pack()

# Tạo danh sách phát để lưu trữ các bài hát đã tải về
playlist = []

# Chạy ứng dụng
window.mainloop()
