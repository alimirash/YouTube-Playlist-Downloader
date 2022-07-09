import wget
import time
from pytube import Playlist

links = []
p = Playlist('Enter YouTube Playlist Link')
for url in p.video_urls:
    links.append(url)

count = 0
for link in links:
    print(f"downloading {count} nth file ...")
    wget.download(link, 'Enter the location where you want the files to be saved !!!')
    print(f"Downloaded {count} nth file!! \n")
    count += 1
    time.sleep(2)

print("all files Downloaded!")