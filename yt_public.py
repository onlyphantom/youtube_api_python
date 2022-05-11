import os
import csv
from datetime import datetime as dt
from dotenv import load_dotenv
from googleapiclient.discovery import build

from utils.comments import process_comments, make_csv

load_dotenv()
API_KEY = os.getenv("API_KEY")

youtube = build("youtube", "v3", developerKey=API_KEY)

def search_result(query):
    """
    Refer to the documentation: https://googleapis.github.io/google-api-python-client/docs/dyn/youtube_v3.search.html
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

def comment_threads(channelID, to_csv=False):
    
    comments_list = []
    
    request = youtube.commentThreads().list(
        part='id,replies,snippet',
        videoId=channelID,
    )
    response = request.execute()
    comments_list.extend(process_comments(response['items']))

    # if there is nextPageToken, then keep calling the API
    while response.get('nextPageToken', None):
        request = youtube.commentThreads().list(
            part='id,replies,snippet',
            videoId=channelID,
            pageToken=response['nextPageToken']
        )
        response = request.execute()
        comments_list.extend(process_comments(response['items']))
    
    print(f"Finished fetching comments for {channelID}. {len(comments_list)} comments found.")
    
    if to_csv:
        make_csv(comments_list, channelID)
    
    return comments_list

if __name__ == '__main__':
    pyscriptVidId = 'Qo8dXyKXyME'
    channelId = 'UCzIxc8Vg53_ewaRIk3shBug'

    # response = search_result("pyscript")
    # response = channel_stats(channelId) 
    response = comment_threads(pyscriptVidId, to_csv=True)

    # print(response)
