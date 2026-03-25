import yt_dlp

# pip install yt-dlp

def download_1080p_video(url):
    # Configuration options for yt-dlp
    ydl_opts = {
        # Grab best video up to 1080p (mp4) + best audio (m4a), or fallback to best combined up to 1080p
        'format': 'bestvideo[height<=1080][ext=mp4]+bestaudio[ext=m4a]/best[height<=1080][ext=mp4]/best',
        
        # Name the downloaded file using the video's title
        'outtmpl': '%(title)s.%(ext)s',
        
        # Force the final merged file to be an MP4
        'merge_output_format': 'mp4',
        
        # Don't show massive blocks of text, just the progress
        'quiet': False,
        'no_warnings': True,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"Starting download for: {url}")
            print("This might take a while for a 3-hour video. Please wait...")
            ydl.download([url])
            print("\nDownload completed successfully!")
            
    except Exception as e:
        print(f"\nAn error occurred: {e}")

if __name__ == "__main__":
    # Paste your 3-hour YouTube video link here
    video_url = input("Enter the YouTube URL: ").strip()
    
    if video_url:
        download_1080p_video(video_url)
    else:
        print("No URL provided. Exiting.")