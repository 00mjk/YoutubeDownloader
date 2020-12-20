import pytube 

url = "https://www.youtube.com/watch?v=UjTv8ivh7mY"

video = pytube.YouTube(url).streams

def downloadVideo(video):
    video.filter(audio_codec="mp4a.40.2", type="video").first().download(filename="Video") 

choose = input(f"Do you want to download *{url}* ?\n>").lower()

if choose == "yes" or choose == "y":
    print("Downloading...")
    downloadVideo(video)
    print("Download Complete!")
elif choose == "no" or choose == "n":
    print("Download Canceled!")
else:
    print("Invalid Operation!")
