# Spotify to MP3
> Spotify to MP3 is command line tool that let's you download music from playlists, albums and single tracks.

## Table of Contents
* [General Info](#general-information)
* [Technologies Used](#technologies-used)
* [Features](#features)
* [Screenshots](#screenshots)
* [Setup](#setup)
* [Usage](#usage)
* [Room for Improvement](#room-for-improvement)

## General Information
- Spotify does not allow users to download music in form of .mp3 files. This simple tool will allow you to take your Spotify music and download it. (not directly from Spotify)
- Track list is taken from your Spotify links through Spotify API, then tracks are found on YouTube and downloaded from there. Last step is converting YouTube .mp4 audio files to .mp3 with help of FFMpeg

## Technologies Used
- Python 3.10.8
- Spotify Web API
- FFMpeg

## Features
- Download tracks
- Download playlists
- Download albums

## Screenshots
[![0.png](https://i.postimg.cc/V6L0FfnT/0.png)](https://postimg.cc/sBq2jRn9)
[![1.png](https://i.postimg.cc/3w3kK8SR/1.png)](https://postimg.cc/mP6LjsGf)

## Setup
You need to have FFMpeg installed and added to PATH on your machine 

### Install python module dependencies
```sh
pip install -r requirements.txt
```

## Usage
- Just put url to a playlist, album or track when asked.
- Type 'exit' to quit the program

## Room for improvements
- GUI
- Give user the option to select bitrate of final music file