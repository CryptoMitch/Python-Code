# Automation Project:Youtube Downloader
# Source: https://www.youtube.com/watch?v=vEQ8CXFWLZU&list=WL&index=7&t=57s

from pytube import YouTube
from sys import argv

# Access Youtube Video Link in the Command Line via the argv arguments
link = argv[1]
yt = YouTube(link) # create Youtube object from the link

print("Title: ", yt.title) # print Title of Youtube Video
print("Views: ", yt.views) # print number of views of Youtube Video

# Download Youtube Video
youtubedownload = yt.streams.get_highest_resolution()
youtubedownload.download("/Users/mitch/Downloads")
