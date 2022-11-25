import requests
import re
import json

def convert_link(input_link):
    media_type = re.split(r"/", input_link)[3]
    file_name = re.split(r"/", input_link)[5]

    session = requests.Session()
    response = session.get(f"https://www.radiojavan.com/{media_type}/{media_type[:-1]}_host/?id={file_name}")
    base_url = str(json.loads(response.text)["host"])

    if media_type == "podcasts":
        return f"{base_url}/media/podcast/mp3-256/{file_name}.mp3"
    elif media_type == "mp3s":
        return f"{base_url}/media/mp3/{file_name}.mp3"
    elif media_type == "videos":
        return f"{base_url}/media/music_video/hq/{file_name}.mp4"
    else:
        return None
