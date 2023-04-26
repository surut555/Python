import os
import pafy
import youtube_dl
import vlc
import time
import random
import re, requests, subprocess,urllib.parse,urllib.request
import pyfiglet

def play(name, n):
    query_string = urllib.parse.urlencode({"search_query":name})
    formatUrl = urllib.request.urlopen("https://www.youtube.com/results?" + query_string)
    search_result = re.findall(r"watch\?v=(\s{11})", formatUrl.read().decode())

    clip = "https://www.youtube.com/watch?v=" + "{}" .format(search_result[0])
    video = pafy.new(clip)

    if n == 1:
        videolink = video.getbest()
        print("video is player..")
    else:
        videolink = video.getbestaudio()
        print("video is player..")

    media = vlc.MediaPlayer(videolink.url)
    media.play()
text = pyfiglet.figlet_format("YouTube Playar")
print(text)
print("Enter 1 for video or 2 only audio")

while 1 != 0:
    n = int(input())
    print("enter play name : ")
    play(input(),n)
