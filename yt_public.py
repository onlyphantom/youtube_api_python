import os
from dotenv import load_dotenv
from googleapiclient.discovery import build

load_dotenv()
API_KEY = os.getenv("API_KEY")

youtube = build("youtube", "v3", developerKey=API_KEY)

def search_result(query):
    """
    Refer: https://googleapis.github.io/google-api-python-client/docs/dyn/youtube_v3.search.html
    """
    request = youtube.search().list(
        part="snippet",
        q=query,
        maxResults=10,
    )

    return request.execute()

def channel_stats(channelID):
    """
    Refer to the documentation: https://googleapis.github.io/google-api-python-client/docs/dyn/youtube_v3.channels.html
    """
    request = youtube.channels().list(
        part="statistics",
        id=channelID
    )
    return request.execute()

def comment_threads(channelID):
    request = youtube.commentThreads().list(
        part='id,replies,snippet',
        videoId=channelID,
    )
    return request.execute()

if __name__ == '__main__':
    pyscriptVidId = 'Qo8dXyKXyME'
    channelId = 'UCzIxc8Vg53_ewaRIk3shBug'

    # response = search_result("pyscript")
    response = channel_stats(channelId) 
    # response = comment_threads(pyscriptVidId)

    print(response)
