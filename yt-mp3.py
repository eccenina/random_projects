import yt_dlp
import os
# pip install yt-dlp

def download_audio(youtube_url):
    # Setup options for downloading and converting
    ydl_opts = {
        'format': 'bestaudio/best', # Download the best audio quality available
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',    # Convert to mp3
            'preferredquality': '192',  # Audio quality (192kbps is standard high quality)
        }],
        'outtmpl': '%(title)s.%(ext)s', # Name the file after the video title
        'quiet': False                  # Set to True if you don't want to see download progress
    }

    try:
        print(f"\nAttempting to download: {youtube_url}")
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([youtube_url])
        print("\n✅ Download and conversion complete! Check your folder.")
        
    except Exception as e:
        print(f"\n❌ An error occurred: {e}")

if __name__ == "__main__":
    print("--- YouTube to MP3 Downloader ---")
    url = input("Enter the YouTube URL: ").strip()
    
    if url:
        download_audio(url)
    else:
        print("No URL provided. Exiting.")