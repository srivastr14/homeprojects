# import requests
import pip._vendor.requests as requests
import json
from datetime import datetime, time
import pytz

tz = pytz.timezone('US/Eastern')
today = datetime.today().strftime('%Y-%m-%d')
midnight = tz.localize(datetime.combine(datetime.now(tz).date(), time(0, 0)), is_dst=None).timestamp()
# print(today, midnight)

def lineup():
    awayteam = {}
    hometeam = {}
    gameline = input("Input the gameid: ")
    payload = ""
    headers = {
    'authority': "api.sofascore.com",
    'cache-control': "max-age=0",
    'sec-ch-ua-mobile': "?0",
    'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
    'accept': "*/*",
    'origin': "https://www.sofascore.com",
    'sec-fetch-site': "same-site",
    'sec-fetch-mode': "cors",
    'sec-fetch-dest': "empty",
    'referer': "https://www.sofascore.com/",
    'accept-language': "en-US,en;q=0.9",
    }
    urlline = 'https://api.sofascore.com/api/v1/event/' + gameline + '/lineups'
    response = requests.request("GET", urlline, data=payload, headers=headers)
    jsondata = json.loads(response.text)
    for player in jsondata['away']['players']:
        order = player['statistics']['battingListIndex']
        name = player['player']['name']
        jersey = player['jerseyNumber']
        position = player['position']
        values = jersey + ' ' + name + ' ' + position
        awayteam[order] = values
    for player in jsondata['home']['players']:
        order = player['statistics']['battingListIndex']
        name = player['player']['name']
        jersey = player['jerseyNumber']
        position = player['position']
        values = jersey + ' ' + name + ' ' + position
        hometeam[order] = values
    print('Away team:')
    for k, v in sorted(awayteam.items()):
        print(v)
    print('Home team:')
    for k, v in sorted(hometeam.items()):
        print(v)


def check_scores():

    lineQ = input("Looking for a lineup? yes/no: ")
    url = "https://api.sofascore.com/api/v1/sport/baseball/scheduled-events/" + today

    payload = ""
    headers = {
        'authority': "api.sofascore.com",
        'cache-control': "max-age=0",
        'sec-ch-ua-mobile': "?0",
        'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
        'accept': "*/*",
        'origin': "https://www.sofascore.com",
        'sec-fetch-site': "same-site",
        'sec-fetch-mode': "cors",
        'sec-fetch-dest': "empty",
        'referer': "https://www.sofascore.com/",
        'accept-language': "en-US,en;q=0.9",
        }

    response = requests.request("GET", url, data=payload, headers=headers)

    jsondata = json.loads(response.text)

    if lineQ == 'yes': 
        for game in jsondata['events']:
            if game['startTimestamp'] < midnight:
                continue
            if game['tournament']['name'] != "MLB, Regular Season":
                continue
            gametime = pytz.timezone('US/Eastern').localize(datetime.fromtimestamp(game['startTimestamp']))
            gameid = game['id']
            league = game['tournament']['name']
            hometeam = game['homeTeam']['name']
            awayteam = game['awayTeam']['name']
            if game['status']['description'] == 'Not started':
                print(league, '|', hometeam, "vs", awayteam, " starts at", gametime.strftime('%H:%M'), '|', gameid)
                continue
            status = game['status']['description']
            homescore = game['homeScore']['current']
            awayscore = game['awayScore']['current']
            print(league, '|', awayteam, awayscore, '-', homescore, hometeam, '|', status, '|', gameid)

        lineup()
    elif lineQ == 'no':
        for game in jsondata['events']:
            if game['startTimestamp'] < midnight:
                continue
            if game['tournament']['name'] != "MLB, Regular Season":
                continue
            gametime = pytz.timezone('US/Eastern').localize(datetime.fromtimestamp(game['startTimestamp']))
            league = game['tournament']['name']
            hometeam = game['homeTeam']['name']
            awayteam = game['awayTeam']['name']
            if game['status']['description'] == 'Not started':
                print(league, '|', hometeam, "vs", awayteam, " starts at", gametime.strftime('%H:%M'), '|', gameid)
                continue
            status = game['status']['description']
            homescore = game['homeScore']['current']
            awayscore = game['awayScore']['current']
            print(league, '|', awayteam, awayscore, '-', homescore, hometeam, '|', status)
    else:
        print("Choose yes or no")
        return check_scores()

if __name__ == "__main__":
    check_scores()