import yt_dlp
from moviepy.editor import *
#Función para descargar el video de YouTube
def download_video(url, output_path='video.mp4'):
    ydl_opts = {
        'format': 'best',
        'outtmpl': output_path,
    }
    with yt_dlp.Youtube(ydl_opts) as ydl:
        ydl.download([url])
