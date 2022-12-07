import youtube
import spotify
import ffmpeg_wrapper
import subprocess

WELCOME_MESSAGE = """
---------------------------------------------------

                  SPOTIFY TO MP3
        default music save path is ./download
    To download your favorite music from spotify
just put URL to a track, playlist or an album below.
               Type 'exit' to quit.

---------------------------------------------------
"""


def main():
    url = ''
    while url != 'exit':
        subprocess.run('cls||clear', shell=True)
        print(WELCOME_MESSAGE)
        url = input("URL: ")
        tracks_to_download = spotify.handle_url(url)
        for track in tracks_to_download:
            youtube.download_audio(track)
            print("Converting to mp3..")
            ffmpeg_wrapper.convert('./download/temp',
                                   f"./download/'{track}'.mp3")
            print("Converting complete")


if __name__ == "__main__":
    main()
