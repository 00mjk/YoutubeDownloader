import pytube

url = "https://www.youtube.com/watch?v=UM6YDJ2aalU&t=91s"

video = pytube.Youtube(url)

for stream in video.streams:
    print(stream)