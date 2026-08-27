# Pytube
A project to download the audio from YouTube videos as MP3 files, from the command line.

## Setup Instructions
- Clone the repository.
- Ensure you have ```Python3``` installed on your machine.
- Install ```ffmpeg```, which performs the MP3 conversion, run ```brew install ffmpeg```.
- Install the dependencies, run ```pip3 install -r requirements.txt```.
- Update the ```directory``` value in ```ytDownloader.py``` to the absolute path for where you want to download the audio.

## Example Usage
There are two ways to run the downloader.

### A list of links
Add your links to the ```links``` list at the top of ```ytDownloader.py```:
```python
links = [
    'https://www.youtube.com/watch?v=IYnsfV5N2n8',
    'https://www.youtube.com/watch?v=jNQXAC9IVRw',
]
```
Then run it with no arguments:
```
python3 ytDownloader.py
```
The links download one at a time, in the order they appear in the list.

### Links on the command line
Any links passed as arguments are used instead of the ```links``` list, and download in the
order you type them. Always quote them, so the shell does not treat the ```?``` and ```&```
characters as its own:
```
python3 ytDownloader.py 'YOUTUBE_LINK'
python3 ytDownloader.py 'FIRST_LINK' 'SECOND_LINK' 'THIRD_LINK'
```

## Playlists
A playlist link downloads every video in it as an individual MP3. Playlists are given their own
folder, and the tracks are numbered so they keep the playlist order:
```
~/Music/Pytube/
├── asdfmovie.mp3
└── Events/
    ├── 01 - Blender Conference 2025 Recap.mp3
    ├── 02 - Blender at Annecy 2024 Recap.mp3
    └── 03 - Blender @ SIGGRAPH LA 2023.mp3
```
Single videos are unaffected, and stay in the main folder without a number.

A video inside a playlist that is private, deleted or region blocked is skipped, and the rest of
the playlist still downloads. The playlist link is listed under ```Failed:``` in the summary if
any of its videos were skipped, and the ```ERROR:``` lines above it name the ones that failed.

## Failed Downloads
A link that fails does not stop the rest of the batch. The error is printed, the remaining
links still download, and a summary is written at the end:
```
Completed 2 of 3.
Failed: https://www.youtube.com/watch?v=ZZZZZZZZZZZ
```
The script exits with a status of ```1``` if any link failed, and ```0``` if they all worked.

## A Note On pytube
This project originally used ```pytube```, which downloaded videos rather than audio. That
library was last released in May 2023 and no longer works — YouTube changed its internal API,
so every request now fails with ```HTTP Error 400: Bad Request``` before the download starts.
It has been replaced with ```yt-dlp```, which is actively maintained.
