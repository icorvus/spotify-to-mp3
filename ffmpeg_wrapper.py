import subprocess
import os


def convert(input: str, output: str) -> None:
    """Converts file with FFMpeg

    Args:
        input (str): path to input file
        output (str): path to output file
    """
    command = f"ffmpeg -i {input} -vn {output}"
    subprocess.run(command, shell=True,
                   stdout=subprocess.DEVNULL,
                   stderr=subprocess.DEVNULL)
    # Remove the old file as it is not needed after conversion
    os.remove(input)
