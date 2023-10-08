import tkinter as tk
import os
import urllib.request
from moviepy.editor import *
from sclib import SoundcloudAPI, Track


api = SoundcloudAPI()


def download_and_create_video():
    url = entry_url.get()
    if url == "":
        status_label.config(text="Please enter a SoundCloud URL")
        return
    track = api.resolve(url)
    if not isinstance(track, Track):
        status_label.config(text="Invalid SoundCloud URL")
        return

    if not os.path.exists('music'):
        os.makedirs('music')
    if not os.path.exists(f'music/{track.genre}'):
        os.makedirs(f'music/{track.genre}')
    if not os.path.exists("images"):
        os.makedirs("images")
    if not os.path.exists("videos"):
        os.makedirs("videos")

    trackname = f'music/{track.genre}/{track.artist} - {track.title}.mp3'

    if not os.path.exists(trackname):
        with open(trackname, 'wb+') as file:
            track.write_mp3_to(file)

    artwork_url = track.artwork_url
    if artwork_url is not None:
        imagename = f'images/{track.artist} - {track.title}.jpg'
        if not os.path.exists(imagename):
            urllib.request.urlretrieve(artwork_url, imagename)

    duration = track.duration / 1000

    image_clip = ImageClip(imagename, duration=duration)
    audio_clip = AudioFileClip(trackname)
    video_clip = image_clip.set_audio(audio_clip)
    output_video_path = f'videos/{track.artist} - {track.title}.mp4'

    if not os.path.exists(output_video_path):
        video_clip.write_videofile(output_video_path, fps=24, codec='libx264',)
        status_label.config(text="Video created successfully")
    else:
        status_label.config(text="Video already exists")

    # upload to youtube
    try:
        os.system(
            f'python upload_video.py --file="{output_video_path}" --title="{track.title}" --description="{track.description}" --keywords="{track.genre}" --category="22" --privacyStatus="public"')
    except:
        print("failed upload.")
    else:
        print("upload successful.")
        status_label.config(text="Video uploaded successfully")


app = tk.Tk()
app.title("SoundCloud to Video Downloader")
app.geometry("500x200")
label = tk.Label(app, text="Enter SoundCloud URL:")
label.pack(pady=10)

entry_url = tk.Entry(app, width=40)
entry_url.pack()

download_button = tk.Button(
    app, text="upload to Youtube", command=download_and_create_video)
download_button.pack(pady=10)

status_label = tk.Label(app, text="")
status_label.pack()


app.mainloop()
