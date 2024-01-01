from pytube import YouTube
import sys


def download_youtube_video(link):

    try:
        yt = YouTube(link)

        print(f"Title: {yt.title}")
        print(f"Views: {yt.views}")

        yd = yt.streams.get_highest_resolution()
        yd.download()
        print("Download completed successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        link = sys.argv[1]
        download_youtube_video(link)
    else:
        print("Please provide a YouTube link as an argument.")
