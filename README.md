### YouTube API (Python)
This is a repository hosting the code examples demonstrated in the YouTube API tutorial on my youtube channel. 
- [YouTube Analytics API tutorial | YouTube](https://youtu.be/rcE3iL0URhU)

### Usage
There are two main Python scripts: `yt_auth.py` and `yt_public.py`. 

1. Install the dependencies `pip install -r requirements.txt`

1. Execute the scripts
    - To run `yt_auth`, you will need store your secrets as `client_secret.json` in the same directory. 
    - 2b. To run `yt_public`, simply create a `.env` file and add a line to your API key: `API_KEY=<YOUR_API_KEY>`

1. Experiment! Modify `yt_public.py` to use one the ready-made functions (`search_result`, `comment_threads` etc) with a YouTube video ID / channel ID. The function names are pretty self-explanatory. Modify `yt_auth.py` to modify what gets returned, `startDate`, `endDate` etc. 

```python
pyscriptVidId = 'Qo8dXyKXyME'
channelId = 'UCzIxc8Vg53_ewaRIk3shBug'

# try one of the following (uncomment) 
# response = search_result("pyscript")
response = channel_stats(channelId) 
# response = comment_threads(pyscriptVidId)
print(response)
```

### Example:
```bash
# when returning channel_stats
python yt_public.py

# returns:
{'kind': 'youtube#channelListResponse', 'etag': '5AtqmD44H4QfpPsqQ4Wnihwsngc', 'pageInfo': {'totalResults': 1, 'resultsPerPage': 5}, 'items': [{'kind': 'youtube#channel', 'etag': 'GB2ykHK9DVB-53aKbVA6YAUXNkE', 'id': 'UCzIxc8Vg53_ewaRIk3shBug', 'statistics': {'viewCount': '57498', 'subscriberCount': '961', 'hiddenSubscriberCount': False, 'videoCount': '59'}}]}
```

When returning `comment_threads`, it is recommended to return it with a `maxResults` parameter for videos with many comments:

```bash
python yt_public.py
{'kind': 'youtube#commentThreadListResponse', 'etag': 'Ic9b-4hLJVdF7UDLjD4AtQLB0Lw', 'nextPageToken': 'QURTSl9pM0hzMS1NSUo2c1lwNFloWWIwakpIanhtemlCdkRqYXJ6SlUtLVpVYVFwU2RyeE5RZ0dlX0cyLU0ya3JHWmlKdldRSVFXWU9HRQ==', 'pageInfo': {'totalResults': 20, 'resultsPerPage': 20}, 'items': [{'kind': 'youtube#commentThread', 'etag': 'TIrOdgUxY0GufmjsAq37cP98_wI', 'id': 'UgwyC-Lg8xTM-ZwDIMl4AaABAg', 'snippet': {'videoId': 'Qo8dXyKXyME', 'topLevelComment': {'kind': 'youtube#comment', 'etag': 'r-Y1IQx1b405LtcbYs4TnrJh3Jg', 'id': 'UgwyC-Lg8xTM-ZwDIMl4AaABAg', 'snippet': {'videoId': 'Qo8dXyKXyME', 'textDisplay': 'Ahuet guys, it was really impressive, obviously when he create repl tag and instead html-page he got realtime pyhton console!', 'textOriginal': 'Ahuet guys, it was really impressive, obviously when he create repl tag and instead html-page he got realtime pyhton console!', 'authorDisplayName': 'Белгородский Джедай', 'authorProfileImageUrl': 'https://yt3.ggpht.com/ytc/AKedOLS9oo0Gh5C7ENfUDlUz3yrFTwVNGN7SFLNauA=s48-c-k-c0x00ffffff-no-rj', 'authorChannelUrl': 'http://www.youtube.com/channel/UCDqaIEKwP63mCEa1DbdI8sg', 'authorChannelId': {'value': 'UCDqaIEKwP63mCEa1DbdI8sg'}, 'canRate': True, 'viewerRating': 'none', 'likeCount': 0, 'publishedAt': '2022-05-09T19:47:23Z', 'updatedAt': '2022-05-09T19:47:23Z'}}, 'canReply': True, 'totalReplyCount': 0, 'isPublic': True}}, {'kind': 'youtube#commentThread', 'etag': 'XuqkWlpnGIcVU4IpNssELzh6cGE', 'id': 'Ugx7GGYIl6G4UYf-PSR4AaABAg', 'snippet': {'videoId': 'Qo8dXyKXyME', 'topLevelComment': {'kind': 'youtube#comment', 'etag': 'v2NOrgq8b3kEr1kSpq6vQJ2CnhE', 'id': 'Ugx7GGYIl6G4UYf-PSR4AaABAg', 'snippet': {'videoId': 'Qo8dXyKXyME', 'textDisplay': 'Thank you very much.. Please add more more more project about pyscript.... From Indonesia🇮🇩', 'textOriginal': 'Thank you very much.. Please add more more more project about pyscript.... From Indonesia🇮🇩', 'authorDisplayName': 'Renni Ekaputri', 'authorProfileImageUrl': 'https://yt3.ggpht.com/d7JLKybsXKEnS6_TKQI8wNcGCxSOeiy92-bUPWKUsYjHU2s52wapXgSfKQiOa-3IpC14d9vA_w=s48-c-k-c0x00ffffff-no-rj', 'authorChannelUrl': 'http://www.youtube.com/channel/UCrsuj8xA6W_pUIo5yagHgYA', 'authorChannelId': {'value': 'UCrsuj8xA6W_pUIo5yagHgYA'}, 'canRate': True, 'viewerRating': 'none', 'likeCount': 0, 'publishedAt': '2022-05-09T18:45:03Z', 'updatedAt': '2022-05-09T18:45:03Z'}}, 'canReply': True, 'totalReplyCount': 1, 'isPublic': True}, 'replies': {'comments': [{'kind': 'youtube#comment', 'etag': 'wUSmUhfU3ox5KY0Sz0KsPnp6iB4', 'id': 'Ugx7GGYIl6G4UYf-PSR4AaABAg.9aolZGyDz3w9apYGzzghC4', 'snippet': {'videoId': 'Qo8dXyKXyME', 'textDisplay': 'Thank you Renni! Check out the other projects we build with pyscript too 😀<br><br>Part 1 (intro to PyScript): <a href="https://youtu.be/Qo8dXyKXyME">https://youtu.be/Qo8dXyKXyME</a><br>Part 2 (PyScript deployment): <a href="https://youtu.be/oH_rTTDjMvM">https://youtu.be/oH_rTTDjMvM</a><br>Part 3 (PyScript + Altair data dashboard): <a href="https://youtu.be/ugSBaOT0rVI">https://youtu.be/ugSBaOT0rVI</a><br>Part 4 (PyScript Guest Book app, CRUD): <a href="https://youtu.be/H6rNzQeryQo">https://youtu.be/H6rNzQeryQo</a>', 'textOriginal': 'Thank you Renni! Check out the other projects we build with pyscript too 😀\n\nPart 1 (intro to PyScript): https://youtu.be/Qo8dXyKXyME\nPart 2 (PyScript deployment): https://youtu.be/oH_rTTDjMvM\nPart 3 (PyScript + Altair data dashboard): https://youtu.be/ugSBaOT0rVI\nPart 4 (PyScript Guest Book app, CRUD): https://youtu.be/H6rNzQeryQo', 'parentId': 'Ugx7GGYIl6G4UYf-PSR4AaABAg', 'authorDisplayName': 'Samuel Chan', 'authorProfileImageUrl': 'https://yt3.ggpht.com/ytc/AKedOLRGpq_SJ3BGRNRqjdgeo8_STiwyFFheA6jdGbKr=s48-c-k-c0x00ffffff-no-rj', 'authorChannelUrl': 'http://www.youtube.com/channel/UCzIxc8Vg53_ewaRIk3shBug', 'authorChannelId': {'value': 'UCzIxc8Vg53_ewaRIk3shBug'}, 'canRate': True, 'viewerRating': 'none', 'likeCount': 0, 'publishedAt': '2022-05-10T01:59:27Z', 'updatedAt': '2022-05-10T01:59:27Z'}}]}}, {'kind': 'youtube#commentThread', 'etag': 'KmRQzOOglhz5HHoGpXcEri1TS28', 'id': 'Ugxo6DY0jEyzXfmye2R4AaABAg', 'snippet': {'videoId': 'Qo8dXyKXyME', 'topLevelComment': {'kind': 'youtube#comment', 'etag': '5cTRv8hTa0SnVvzegMjpA0zg4y8', 'id': 'Ugxo6DY0jEyzXfmye2R4AaABAg', 'snippet': {'videoId': 'Qo8dXyKXyME', 'textDisplay': 'Nice 👍<br>Does it take in .ipynb files?', 'textOriginal': 'Nice 👍\nDoes it take in .ipynb files?', 'authorDisplayName': 'phlorah', 'authorProfileImageUrl': 'https://yt3.ggpht.com/ytc/AKedOLTy0xRUqmV5i3c6MpvYdh33oTA7F8AMn4vXaBUGX-rPth6cSlW_P1bP3G1_VGmH=s48-c-k-c0x00ffffff-no-rj', 'authorChannelUrl': 'http://www.youtube.com/channel/UCq035cbe5f_l8b8KNN08NnA', 'authorChannelId': {'value': 'UCq035cbe5f_l8b8KNN08NnA'}}}}}]}
```


```bash
python yt_auth.py

# returns:
+------------+-------------------+-------+-------+-------------------+
|    date    | estMinutesWatched | views | likes | subscribersGained |
+------------+-------------------+-------+-------+-------------------+
| 2022-05-01 |        756        |  194  |   9   |        11         |
| 2022-05-02 |        886        |  248  |   4   |         8         |
| 2022-05-03 |        589        |  247  |   7   |         1         |
| 2022-05-04 |       4972        | 1346  |  50   |        22         |
| 2022-05-05 |       9866        | 2689  |  62   |        55         |
| 2022-05-06 |       10002       | 2759  |  98   |        92         |
| 2022-05-07 |       10243       | 3200  |  96   |        78         |
| 2022-05-08 |       12072       | 3600  |  108  |        100        |
| 2022-05-09 |       11594       | 3746  |  116  |        92         |
| 2022-05-10 |       8958        | 2762  |  66   |        69         |
| 2022-05-11 |       7152        | 2156  |  33   |        51         |
| 2022-05-12 |       8462        | 2269  |  63   |        61         |
| 2022-05-13 |       7275        | 2480  |  64   |        52         |
| 2022-05-14 |       5567        | 1702  |  36   |        33         |
| 2022-05-15 |       4054        | 1218  |  22   |        32         |
| 2022-05-16 |       3759        | 1138  |  15   |        29         |
| 2022-05-17 |       3555        | 1040  |  16   |        21         |
| 2022-05-18 |       3612        |  921  |  21   |        15         |
| 2022-05-19 |       3134        |  899  |  19   |        15         |
| 2022-05-20 |       2649        |  656  |  10   |        17         |
| 2022-05-21 |       2569        |  678  |  14   |        12         |
| ... <TRUNCATED> ...                                                |
| 2023-04-17 |       2646        |  723  |  12   |        13         |
| 2023-04-18 |       2098        |  660  |   8   |        15         |
| 2023-04-19 |       2244        |  653  |   7   |        10         |
| 2023-04-20 |       1897        |  589  |  13   |        17         |
| 2023-04-21 |       2277        |  699  |  10   |        20         |
| 2023-04-22 |       2694        |  734  |  11   |        20         |
| 2023-04-23 |       2642        |  694  |   8   |        19         |
| 2023-04-24 |       3174        |  839  |  20   |        24         |
| 2023-04-25 |       3472        |  916  |  20   |        20         |
| 2023-04-26 |       4346        | 1088  |  32   |        23         |
| 2023-04-27 |       3838        |  964  |  14   |        18         |
| 2023-04-28 |       3884        |  957  |  20   |        26         |
+------------+-------------------+-------+-------+-------------------+
```

It will also save the data into a csv file in the same directory. You can modify these behaviors, including the filename, the desired columns, and date ranges etc by modifying the `yt_auth.py` file.

### Next Steps
- [ ] Add `argparse`
- [ ] Refactor code to make them parameterized functions
- [ ] Simple charting / tabular printing
- [ ] Supports other methods from YouTube API
- [ ] Provide cleaning utility for unpacking returned results