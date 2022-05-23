import csv
from datetime import datetime as dt

today = dt.today().strftime('%d-%m-%Y')
PATH = 'commentsFolder/'

def process_comments(response_items, csv_output=False):
    comments = []

    for res in response_items:

        # loop through the replies
        if 'replies' in res.keys():
            for reply in res['replies']['comments']:
                comment = reply['snippet']
                comment['commentId'] = reply['id']
                comments.append(comment)
        else:
            comment = {}
            comment['snippet'] = res['snippet']['topLevelComment']['snippet']
            comment['snippet']['parentId'] = None
            comment['snippet']['commentId'] = res['snippet']['topLevelComment']['id']

            comments.append(comment['snippet'])

    if csv_output:
         make_csv(comments)
    
    print(f'Finished processing {len(comments)} comments.')
    return comments


def make_csv(comments, channelID=None, videoID=None):
    # Handle 0 comments issue
    if len(comments) == 0:
        return

    header = comments[0].keys()

    if channelID and videoID:
        filename = f'{PATH}comments_{channelID}_{videoID}_{today}.csv'
    elif channelID:
        filename = f'{PATH}comments_{channelID}_{today}.csv'
    else:
        filename = f'{PATH}comments_{today}.csv'

    with open(filename, 'w', encoding='utf8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=header)
        writer.writeheader()
        writer.writerows(comments)
