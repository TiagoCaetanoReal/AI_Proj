import yt_dlp

def download_music(url):
    options = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': '%(title)s.%(ext)s',
        'noplaylist': True
    }

    with yt_dlp.YoutubeDL(options) as ydl:
        ydl.download([url])

# Example usage:
youtube_url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'  # Replace with your desired YouTube URL
download_music(youtube_url)