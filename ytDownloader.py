from pytube import YouTube
from sys import argv

link = argv[1]
yt = YouTube(link)
directory = '/Users/aodhanwade/Movies/Pytube'

try:
    print('Downloading: ' + yt.title)
    yd = yt.streams.get_highest_resolution()
    yd.download(directory)
except:
    print('Download failed.')
else:
    print('Download completed.')
