### YouTube API (Python)
This is a repository hosting the code examples demonstrated in the tutorial on my youtube channel. The link will be updated when the video goes live - subscribe to my channel to know when it does:
- [Samuel Chan | YouTube](https://www.youtube.com/samuelchan)

### Usage
There are two main Python scripts: `yt_auth.py` and `yt_public.py`. 

1. Install the dependencies `pip install -r requirements.txt`

1. Execute the scripts
    - To run `yt_auth`, you will need store your secrets as `client_secret_desktop_temp.json` in the same directory. 
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
python yt_public.py

# returns:
{'kind': 'youtube#channelListResponse', 'etag': '5AtqmD44H4QfpPsqQ4Wnihwsngc', 'pageInfo': {'totalResults': 1, 'resultsPerPage': 5}, 'items': [{'kind': 'youtube#channel', 'etag': 'GB2ykHK9DVB-53aKbVA6YAUXNkE', 'id': 'UCzIxc8Vg53_ewaRIk3shBug', 'statistics': {'viewCount': '57498', 'subscriberCount': '961', 'hiddenSubscriberCount': False, 'videoCount': '59'}}]}
```

```bash
python yt_auth.py

# returns:
+------------+-------------------+-------+-------+-------------------+
|    date    | estMinutesWatched | views | likes | subscribersGained |
+------------+-------------------+-------+-------+-------------------+
| 2022-04-01 |        380        |  142  |   1   |         2         |
| 2022-04-02 |        272        |  124  |   6   |         3         |
| 2022-04-03 |        456        |  162  |   3   |         3         |
| 2022-04-04 |        487        |  154  |   2   |         1         |
| 2022-04-05 |        360        |  152  |   2   |         2         |
| 2022-04-06 |        557        |  171  |   2   |         1         |
| 2022-04-07 |        399        |  192  |   2   |         2         |
| 2022-04-08 |        560        |  178  |   2   |         2         |
| 2022-04-09 |        362        |  149  |   1   |         2         |
| 2022-04-10 |        554        |  147  |   1   |         3         |
| 2022-04-11 |        616        |  197  |   8   |         7         |
| 2022-04-12 |        620        |  202  |   9   |         3         |
| 2022-04-13 |        487        |  258  |   4   |         7         |
| 2022-04-14 |        706        |  218  |   7   |         3         |
| 2022-04-15 |        829        |  270  |   5   |         9         |
| 2022-04-16 |        722        |  207  |   4   |         5         |
| 2022-04-17 |        766        |  232  |  11   |        10         |
| 2022-04-18 |        763        |  262  |   8   |         8         |
| 2022-04-19 |        797        |  278  |   5   |         5         |
| 2022-04-20 |        606        |  213  |   5   |         3         |
| 2022-04-21 |        519        |  210  |   2   |         2         |
| 2022-04-22 |        769        |  259  |   3   |         4         |
| 2022-04-23 |        571        |  193  |   4   |         2         |
| 2022-04-24 |        453        |  200  |   2   |         3         |
| 2022-04-25 |        839        |  230  |   5   |         0         |
| 2022-04-26 |        533        |  234  |   7   |         4         |
| 2022-04-27 |        664        |  252  |   3   |         3         |
| 2022-04-28 |        793        |  234  |   7   |         3         |
| 2022-04-29 |        520        |  181  |   2   |         2         |
| 2022-04-30 |        632        |  195  |   1   |         6         |
+------------+-------------------+-------+-------+-------------------+
```

### Next Steps
- [ ] Add `argparse`
- [ ] Refactor code to make them parameterized functions
- [ ] Simple charting / tabular printing
- [ ] Supports other methods from YouTube API