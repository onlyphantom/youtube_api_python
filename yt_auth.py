from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
import csv

from tabulate import tabulate

SCOPES = ['https://www.googleapis.com/auth/yt-analytics.readonly']

API_SERVICE_NAME = 'youtubeAnalytics'
API_VERSION = 'v2'
CLIENT_SECRETS_FILE = 'client_secret.json'

def get_service():
  flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
  credentials = flow.run_console()
  # alternatively (https://github.com/onlyphantom/youtube_api_python/pull/3/files):
  # credentials = flow.run_local_server()
  return build(API_SERVICE_NAME, API_VERSION, credentials = credentials)

def execute_api_request(client_library_function, **kwargs):
  response = client_library_function(
    **kwargs
  ).execute()
  return response

def create_table(table, headers=None):
    if headers:
        headerstring = "\t{}\t" * len(headers)
        print(headerstring.format(*headers))

    rowstring = "\t{}\t" * len(table[0])

    for row in table:
        print(rowstring.format(*row))

def create_csv(table, headers=None, filename='output.csv'):
    with open(filename, 'w') as f:
        writer = csv.writer(f)
        if headers:
            writer.writerow(headers)
        writer.writerows(table)

if __name__ == '__main__':

    youtubeAnalytics = get_service()
    result = execute_api_request(
        youtubeAnalytics.reports().query,
        ids='channel==MINE',
        startDate='2022-05-01',
        endDate='2023-04-30',
        metrics='estimatedMinutesWatched,views,likes,subscribersGained',
        dimensions='day',
        sort='day'
    )
    headers = ['date', 'estMinutesWatched', 'views', 'likes', 'subscribersGained']
    # create_table(result['rows'], headers=headers)
    create_csv(result['rows'], headers=headers)
    print(tabulate(result['rows'], headers=headers, tablefmt="pretty"))
  
