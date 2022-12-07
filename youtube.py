import pytube


class YouTube:
    def download_audio(self, song_name: str, path="./download") -> str:
        # Get YouTube Object of the track
        print(f"Searching for the track: {song_name}")
        track = pytube.Search(song_name).results[0]
        # Get highest bitrate audio stream for mp4
        track_stream = track.streams.get_audio_only()
        filesize_mb = round(track_stream.filesize / 1_000_000, 2)
        print(f"Downloading {track_stream.title}.\
                Filesize: {filesize_mb} MB")
        track_stream.download(output_path=path, filename=f"{song_name}.mp4")
        print('Download finished.')
