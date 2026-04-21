import yt_dlp

# pip install yt-dlp

RESOLUTION_OPTIONS = {
    "1": {"label": "4K     @ 60fps", "height": 2160, "fps": 60},
    "2": {"label": "4K     @ 30fps", "height": 2160, "fps": 30},
    "3": {"label": "1080p  @ 60fps", "height": 1080, "fps": 60},
    "4": {"label": "1080p  @ 30fps", "height": 1080, "fps": 30},
    "5": {"label": "720p   @ 60fps", "height": 720,  "fps": 60},
    "6": {"label": "720p   @ 30fps", "height": 720,  "fps": 30},
    "7": {"label": "480p   @ 30fps", "height": 480,  "fps": 30},
    "8": {"label": "360p   @ 30fps", "height": 360,  "fps": 30},
}

def pick_resolution():
    print("\n┌─────────────────────────────────────┐")
    print("│        Select Resolution & FPS       │")
    print("├────┬────────────────────────────────-┤")
    for key, opt in RESOLUTION_OPTIONS.items():
        print(f"│ {key}  │  {opt['label']:<30}│")
    print("└────┴─────────────────────────────────┘")

    while True:
        choice = input("\nEnter choice [1-8]: ").strip()
        if choice in RESOLUTION_OPTIONS:
            selected = RESOLUTION_OPTIONS[choice]
            print(f"\n✔ Selected: {selected['label'].strip()}")
            return selected["height"], selected["fps"]
        print("  Invalid choice. Please enter a number from 1 to 8.")

def build_format_string(height, fps):
    # Prefer video matching both height AND fps, fall back gracefully
    return (
        f"bestvideo[height<={height}][fps<={fps}][ext=mp4]"
        f"+bestaudio[ext=m4a]"
        f"/bestvideo[height<={height}][fps<={fps}]"
        f"+bestaudio"
        f"/bestvideo[height<={height}][ext=mp4]"
        f"+bestaudio[ext=m4a]"
        f"/best[height<={height}][ext=mp4]"
        f"/best"
    )

def download_video(url, height, fps):
    ydl_opts = {
        "format": build_format_string(height, fps),
        "outtmpl": "%(title)s.%(ext)s",
        "merge_output_format": "mp4",
        "quiet": False,
        "no_warnings": True,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"\nStarting download → {url}\n")
            ydl.download([url])
            print("\n✔ Download completed successfully!")

    except Exception as e:
        print(f"\n✘ An error occurred: {e}")

if __name__ == "__main__":
    video_url = input("Enter the YouTube URL: ").strip()

    if not video_url:
        print("No URL provided. Exiting.")
    else:
        height, fps = pick_resolution()
        download_video(video_url, height, fps)
