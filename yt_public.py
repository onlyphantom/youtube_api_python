import os
from dotenv import load_dotenv
from googleapiclient.discovery import build

load_dotenv()
API_KEY = os.getenv("API_KEY")

def search_result(query):
    """
    Refer: https://googleapis.github.io/google-api-python-client/docs/dyn/youtube_v3.search.html
    """
    query = build("youtube", "v3", developerKey=API_KEY).search().list(
        part="snippet",
        q=query,
        maxResults=10,
    )

    response = query.execute()

def channel_stats(channelID):
    """
    Refer to the documentation: https://googleapis.github.io/google-api-python-client/docs/dyn/youtube_v3.channels.html
    """
    query = build("youtube", "v3", developerKey=API_KEY)
    request = query.channels().list(
        part="statistics",
        id=channelID
    )
    return request.execute()

response = channel_stats("UCzIxc8Vg53_ewaRIk3shBug")
print(response)
