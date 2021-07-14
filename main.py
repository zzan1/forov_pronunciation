import requests 
import re
import base64
import playsound
import os

target_word = "input"

forvo_search = r"https://forvo.com/search/" + target_word + "/"

header = {
    "referer": "https://forvo.com/",
    "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Mobile Safari/537.36 Edg/91.0.864.67"
}

responce = requests.get(forvo_search, headers = header)

audio = re.finditer(r"onclick=\"Play[(](.*?)[)]", responce.text)
if audio: 
    for item in audio:
        audio_base = r"https://audio00.forvo.com/mp3/" 
        audio_suffix = base64.b64decode(item.group(1).split(",")[1]).decode("utf-8")
        r_audio = requests.get(audio_base + audio_suffix, headers = header)
        if r_audio:
            with open(r"C:\Users\24486\Music\cache/cache.mp3", "wb") as f:
                f.write(r_audio.content)
            playsound.playsound(r"C:\Users\24486\Music\cache/cache.mp3")
            os.remove(r"C:\Users\24486\Music\cache/cache.mp3")
            break
            



