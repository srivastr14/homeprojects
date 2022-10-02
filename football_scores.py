import pip._vendor.requests as requests
import json
from datetime import datetime, time
import time

today = datetime.today().strftime('%Y%m%d')
# today = '20221001'

def scoreboard():
    while True:
        league = input("Which league do you want? NFL/college: ")
        if league in ['nfl', 'college']:
            break
    headers = {'content-type': 'multipart/form-data'}
    if league == 'college':
        urlline = f'https://site.api.espn.com/apis/site/v2/sports/football/college-football/scoreboard?dates={today}&limit=200'
    elif league == 'nfl':
        urlline = f'http://site.api.espn.com/apis/site/v2/sports/football/nfl/scoreboard'
    
    while True:
        choice = input("Which games do you want? all/live: ")
        if choice in ['all', 'live']:
            break
    while choice=='live':
        response = requests.request("GET", urlline, headers=headers)
        jsondata = json.loads(response.text)
        for game in jsondata['events']:
            teams = game['name']
            ascore = game['competitions'][0]['competitors'][1]['score']
            hscore = game['competitions'][0]['competitors'][0]['score'] 
            status = game['status']['type']['detail']
            if game['status']['type']['description'] == "Scheduled":
                continue
            elif game['status']['type']['description'] == "Final": 
                continue
            try:
                if game['competitions'][0]['competitors'][0]['id'] == game['competitions'][0]['situation']['possession']:
                    print(f"{teams} | {ascore}-{hscore} | {status} |", end=" ")
                    print(f"{game['competitions'][0]['situation']['downDistanceText']}, {game['competitions'][0]['competitors'][0]['team']['location']} ball")
                elif game['competitions'][0]['competitors'][1]['id'] == game['competitions'][0]['situation']['possession']:
                    print(f"{teams} | {ascore}-{hscore} | {status} |", end=" ")
                    print(f"{game['competitions'][0]['situation']['downDistanceText']}, {game['competitions'][0]['competitors'][1]['team']['location']} ball")
            except KeyError:
                print(f"{teams} | {ascore}-{hscore} | {status} | {game['competitions'][0]['situation']['lastPlay']['text']}") 
        print('\n')
        time.sleep(5)
    if choice == 'all':
        response = requests.request("GET", urlline, headers=headers)
        jsondata = json.loads(response.text)
        for game in jsondata['events']:
            teams = game['name']
            ascore = game['competitions'][0]['competitors'][1]['score']
            hscore = game['competitions'][0]['competitors'][0]['score'] 
            status = game['status']['type']['detail']
            if game['status']['type']['description'] == "Scheduled":
                print(f'{teams} | {status}')
                continue
            elif game['status']['type']['description'] == "Final": 
                print(f'{teams} | {ascore}-{hscore} | {status}')
                continue
            try:
                if game['competitions'][0]['competitors'][0]['id'] == game['competitions'][0]['situation']['possession']:
                    print(f"{teams} | {ascore}-{hscore} | {status} |", end=" ")
                    print(f"{game['competitions'][0]['situation']['downDistanceText']}, {game['competitions'][0]['competitors'][0]['team']['location']} ball")
                elif game['competitions'][0]['competitors'][1]['id'] == game['competitions'][0]['situation']['possession']:
                    print(f"{teams} | {ascore}-{hscore} | {status} |", end=" ")
                    print(f"{game['competitions'][0]['situation']['downDistanceText']}, {game['competitions'][0]['competitors'][1]['team']['location']} ball")
            except KeyError:
                print(f"{teams} | {ascore}-{hscore} | {status} | {game['competitions'][0]['situation']['lastPlay']['text']}") 

if __name__ == '__main__':
    scoreboard()