from sys import argv, exit

import yt_dlp

directory = '/Users/aodhanwade/Music/Pytube'

links = [
    # 'https://www.youtube.com/watch?v=IYnsfV5N2n8',
]

targets = argv[1:] or links

if not targets:
    print('Usage: python3 ytDownloader.py [YOUTUBE_LINK ...]')
    print('Or add links to the links list in ytDownloader.py.')
    exit(1)

options = {
    'format': 'bestaudio/best',
    'outtmpl': directory + '/%(playlist_title|)s/%(playlist_index&{:02d} - |)s%(title)s.%(ext)s',
    'ignoreerrors': True,
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

failed = []

for position, link in enumerate(targets, start=1):
    print('[' + str(position) + '/' + str(len(targets)) + '] ' + link, flush=True)
    try:
        with yt_dlp.YoutubeDL(options) as yd:
            if yd.download([link]) != 0:
                print('Download failed: see the errors above.', flush=True)
                failed.append(link)
    except Exception as error:
        print('Download failed: ' + str(error), flush=True)
        failed.append(link)

print('Completed ' + str(len(targets) - len(failed)) + ' of ' + str(len(targets)) + '.')

for link in failed:
    print('Failed: ' + link)

if failed:
    exit(1)
