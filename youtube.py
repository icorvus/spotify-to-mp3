import pytube


def download_audio(song_name: str, path="./download") -> None:
    """Download audio track of song which name was given as argument

    Args:
        song_name (str): Name of song to download.
        path (str, optional): Download path. Defaults to "./download".

    """
    # Get YouTube Object of the track
    print(f"Searching for the track: {song_name}")
    track = pytube.Search(song_name).results[0]

    # Get highest bitrate audio stream for mp4
    track_stream = track.streams.get_audio_only()

    filesize_mb = round(track_stream.filesize / 1_000_000, 2)
    print(f"Downloading {track_stream.title}.\
            Filesize: {filesize_mb} MB")
    track_stream.download(output_path=path, filename='temp')
    print('Download finished.')
