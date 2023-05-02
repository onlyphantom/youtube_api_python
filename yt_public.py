import os
from dotenv import load_dotenv
from googleapiclient.discovery import build
from iteration_utilities import unique_everseen

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

def comment_threads(videoID, to_csv=False):
    
    comments_list = []
    
    request = youtube.commentThreads().list(
        part='id,replies,snippet',
        videoId=videoID,
    )
    response = request.execute()
    comments_list.extend(process_comments(response['items']))

    # if there is nextPageToken, then keep calling the API
    while response.get('nextPageToken', None):
        request = youtube.commentThreads().list(
            part='id,replies,snippet',
            videoId=videoID,
            pageToken=response['nextPageToken']
        )
        response = request.execute()
        comments_list.extend(process_comments(response['items']))

    comments_list = list(unique_everseen(comments_list))

    print(f"Finished fetching comments for {videoID}. {len(comments_list)} comments found.")
    
    if to_csv:
        make_csv(comments_list, videoID)
    
    return comments_list


def get_video_ids(channelId):
    """
    Refer to the documentation: https://googleapis.github.io/google-api-python-client/docs/dyn/youtube_v3.search.html
    """
    videoIds = []
 
    request = youtube.search().list(
        part="snippet",
        channelId=channelId,
        type="video",
        maxResults=50,
        order="date"
    )

    response = request.execute()
    responseItems = response['items']

    videoIds.extend([item['id']['videoId'] for item in responseItems if item['id'].get('videoId', None) != None])

    # if there is nextPageToken, then keep calling the API
    while response.get('nextPageToken', None):
        request = youtube.search().list(
            part="snippet",
            channelId=channelId,
        )
        response = request.execute()
        responseItems = response['items']

        videoIds.extend([item['id']['videoId'] for item in responseItems if item['id'].get('videoId', None) != None])
    
    print(f"Finished fetching videoIds for {channelId}. {len(videoIds)} videos found.")

    return videoIds



if __name__ == '__main__':
    # to get a list of IDs from a channel
    # ids = get_video_ids("UCws1b7urfxMnvjhUJxHjtuQ")

    # to get results from search
    # response = search_result("pyscript")

    # get channel stats
    # response = channel_stats(channelID='UCzIxc8Vg53_ewaRIk3shBug')

    # get comments
    response = comment_threads(videoID='Qo8dXyKXyME', to_csv=True)

    print(response)
