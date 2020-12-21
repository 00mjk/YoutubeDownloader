import pytube
import re 

# Testing this
# https://www.youtube.com/watch?v=UjTv8ivh7mY

def download_video(video):
    video.filter(audio_codec="mp4a.40.2", type="video").first().download(filename="Video")

def youtube_url_validation(url):
    
    youtube_regex = (r'(https?://)?(www\.)?'
                    '(youtube|youtu|youtube-nocookie)\.(com|be)/'
                    '(watch\?.*?(?=v=)v=|embed/|v/|.+\?v=)?([^&=%\?]{11})')
    
    youtube_regex_match = re.match(youtube_regex, url)
    
    if youtube_regex_match:
        return youtube_regex_match
    else:
        return "Invalid url!"

while True:
    url = input("Insert your url: \n> ")
    
    try:
        youtube_url_validation(url)
    except ValueError as e:
        print("e")
    else:
        pass

    video = pytube.YouTube(url).streams 

    choose = input(f"Download *{url}* ?\n> ").lower()

    if choose == "yes" or choose == "y":
        print("Downloading...")
        download_video(video)
        print("Download Complete!")
        break
    elif choose == "no" or choose == "n":
        print("Download Canceled!")
        break
    else:
        print("Invalid Operation!")
        break