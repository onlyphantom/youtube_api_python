import os
import csv
from datetime import datetime as dt
from urllib import response
from dotenv import load_dotenv
from googleapiclient.discovery import build

from utils.comments import process_comments, make_csv

load_dotenv()
API_KEY_1 = os.getenv("API_KEY_1")
API_KEY_2 = os.getenv("API_KEY_2")
API_KEY_3 = os.getenv("API_KEY_3")
API_KEY_4 = os.getenv("API_KEY_4")
API_KEY_5 = os.getenv("API_KEY_5")

youtube_1 = build("youtube", "v3", developerKey=API_KEY_1)
youtube_2 = build("youtube", "v3", developerKey=API_KEY_2)
youtube_3 = build("youtube", "v3", developerKey=API_KEY_3)
youtube_4 = build("youtube", "v3", developerKey=API_KEY_4)
youtube_5 = build("youtube", "v3", developerKey=API_KEY_5)

scraped_videos = {}

def search_result(youtube, query):
    """
    Refer to the documentation: https://googleapis.github.io/google-api-python-client/docs/dyn/youtube_v3.search.html
    """
    request = youtube.search().list(
        part="snippet",
        q=query,
        maxResults=10,
    )

    return request.execute()

def get_video_ids(youtube, channelId):
    """
    Refer to the documentation: https://googleapis.github.io/google-api-python-client/docs/dyn/youtube_v3.search.html
    """
    videoIds = []

    request = youtube.channels().list(
        part="contentDetails",
        id=channelId
    )

    response = request.execute()

    playlistId = response['items'][0]['contentDetails']['relatedPlaylists']['uploads']

    request = youtube.playlistItems().list(
        part="contentDetails",
        playlistId=playlistId,
        maxResults=50
    )

    response = request.execute()
    responseItems = response['items']

    videoIds.extend([item['contentDetails']['videoId'] for item in responseItems])

    # if there is nextPageToken, then keep calling the API
    while response.get('nextPageToken', None):
        print(f'Fetching next page of videos for {channelId}_{playlistId}')
        request = youtube.playlistItems().list(
            part="contentDetails",
            playlistId=playlistId,
            maxResults=50,
            pageToken=response['nextPageToken']
        )
        response = request.execute()
        responseItems = response['items']

        videoIds.extend([item['contentDetails']['videoId'] for item in responseItems])
    
    print(f"Finished fetching videoIds for {channelId}. {len(videoIds)} videos found.")

    return videoIds

def channel_stats(youtube, channelIDs, to_csv=False):
    """
    Refer to the documentation: https://googleapis.github.io/google-api-python-client/docs/dyn/youtube_v3.channels.html
    """
    if type(channelIDs) == str:
        channelIDs = [channelIDs]

    stats_list = []

    for channelId in channelIDs:
        request = youtube.channels().list(
            part="statistics",
            id=channelId
        )
        response = request.execute()
        response = response['items'][0]['statistics']
        response['channelId'] = channelId

        stats_list.append(response)

    if to_csv:
        header = stats_list[0].keys()
        with open(f'channelStats.csv', 'w') as f:
            writer = csv.DictWriter(f, fieldnames=header)
            writer.writeheader()
            writer.writerows(stats_list)

    return stats_list

def video_stats(youtube, videoIDs, channelID, to_csv=False):
    if type(videoIDs) == str:
        videoIDs = [videoIDs]
    
    stats_list = []

    for videoId in videoIDs:
        request = youtube.videos().list(
            part="snippet, statistics, contentDetails",
            id=videoId
        )
        response = request.execute()
        statistics = response['items'][0]['statistics']
        snippet = response['items'][0]['snippet']
        statistics['videoId'] = videoId
        statistics['title'] = snippet['title']
        statistics['description'] = snippet['description']
        statistics['publishedAt'] = snippet['publishedAt']
        statistics['duration'] = response['items'][0]['contentDetails']['duration']
        statistics['thumbnail'] = snippet['thumbnails']['high']['url']
        statistics['channelId'] = channelID

        if statistics.get('likeCount', None) == None:
            statistics['likeCount'] = 0

        print(f"Fetched stats for {videoId}")
        stats_list.append(statistics)
    
    if to_csv:
        header = stats_list[0].keys()
        with open(f'videosFolder/videoStats_{channelID}.csv', 'w', encoding='utf8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=header)
            writer.writeheader()
            writer.writerows(stats_list)
    
    print(f'Success in fetching video stats for {channelID}')

    return stats_list


def comment_threads(youtube, videoID, channelID=None, to_csv=False):
    
    comments_list = []
    
    try:
        request = youtube.commentThreads().list(
            part='id,replies,snippet',
            videoId=videoID,
        )
        response = request.execute()
    except Exception as e:
        print(f'Error fetching comments for {videoID} - error: {e}')
        if scraped_videos.get('error_ids', None):
            scraped_videos['error_ids'].append(videoID)
        else:
            scraped_videos['error_ids'] = [videoID]
        return

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
    
    print(f"Finished fetching comments for {videoID}. {len(comments_list)} comments found.")
    
    if to_csv:
        try:
            make_csv(comments_list, channelID, videoID)
        except Exception as e:
            print(f'Error writing comments to csv for {videoID} - error: {e}')
            if scraped_videos.get('error_csv_ids', None):
                scraped_videos['error_csv_ids'].append(videoID)
            else:
                scraped_videos['error_csv_ids'] = [videoID]
            return

    if scraped_videos.get(channelID, None):
        scraped_videos[channelID].append(videoID)
    else:
        scraped_videos[channelID] = [videoID]
    
    return comments_list

if __name__ == '__main__':
    pyscriptVidId = 'Qo8dXyKXyME'
    channelId = 'UCzIxc8Vg53_ewaRIk3shBug'

    channelIds = []
    # with open('youtube.csv', 'r') as csvfile:
    #     reader = csv.reader(csvfile)
    #     next(reader)
    #     for row in reader:
    #         channelIds.append(row[2])

    # channel_stats(youtube_2, channelIds, to_csv=True)

    # videoDict = {}
    # for idx in range(len(channelIds)):
    #     if idx <= len(channelIds)/5:
    #         youtube = youtube_1
    #     elif idx <= len(channelIds)/5*2:
    #         youtube = youtube_2
    #     elif idx <= len(channelIds)/5*3:
    #         youtube = youtube_3
    #     elif idx <= len(channelIds)/5*4:
    #         youtube = youtube_4
    #     else:
    #         youtube = youtube_5
    #     videoIds = get_video_ids(youtube, channelIds[idx])
    #     videoDict[channelIds[idx]] = videoIds
    
    import json
    # with open('videoDict.json', 'w') as fp:
    #     json.dump(videoDict, fp)

    with open('videoDict.json', 'r') as fp:
        videoDict = json.load(fp)

    for channelId, videoIds in videoDict.items():
        video_stats(youtube_3, videoIDs=videoIds, channelID=channelId, to_csv=True)

    # for channelId, videoIds in videoDict.items():
    #     for videoId in videoIds:
    #         comment_threads(youtube_3, videoID=videoId, channelID=channelId, to_csv=True)

    # with open('scrapedVideos.json', 'w') as fp:
    #     json.dump(scraped_videos, fp)

    # response = search_result("pyscript")
    # response = channel_stats(youtube_2, channelId) 
    # response = comment_threads(youtube_2, videoID='pnecPXlfR5U', to_csv=False)
    # print(response)

    #NOTES -> troublesome video (videoId: CqssnS_v1a4) -> no likecount, so I manually add 0 to it