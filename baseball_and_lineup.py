import pip._vendor.requests as requests
import json
from datetime import datetime, time
import time
import os

today = datetime.today().strftime('%Y%m%d')


# today = '20221001'

def scoreboard():
    os.system("clear")
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.5',
        'Connection': 'keep-alive',
        'Host': 'site.api.espn.com',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:105.0) Gecko/20100101 Firefox/105.0',
    }
    urlline = f'http://site.api.espn.com/apis/site/v2/sports/baseball/mlb/scoreboard?dates={today}'
    while True:
        choice = input("Which games do you want? all/live: ")
        if choice in ['all', 'live']:
            break
    while choice == 'live':
        response = requests.request("GET", urlline, headers=headers)
        jsondata = json.loads(response.text)
        for game in jsondata['events']:
            teams = game['shortName']
            ascore = game['competitions'][0]['competitors'][1]['score']
            hscore = game['competitions'][0]['competitors'][0]['score']
            status = game['status']['type']['detail']
            if game['status']['type']['description'] == "Scheduled":
                continue
            elif game['status']['type']['description'] == "Final":
                continue
            try:
                print(f"{teams} | {ascore}-{hscore} | {status} | {game['competitions'][0]['outsText']} {game['competitions'][0]['situation']['balls']}-{game['competitions'][0]['situation']['strikes']} {game['competitions'][0]['situation']['lastPlay']['text']}\n")
            except KeyError as e:
                print(f"{teams} | {ascore}-{hscore} | {status}")
                print(e)
        time.sleep(5)
        os.system("clear")
    if choice == 'all':
        response = requests.request("GET", urlline, headers=headers)
        jsondata = json.loads(response.text)
        for game in jsondata['events']:
            game_id = game['id']
            teams = game['shortName']
            ascore = game['competitions'][0]['competitors'][1]['score']
            hscore = game['competitions'][0]['competitors'][0]['score']
            status = game['status']['type']['detail']
            # balls = game['competitions'][0]['situation']['balls']
            # strikes = game['competitions'][0]['situation']['strikes']
            if game['status']['type']['description'] == "Scheduled":
                print(f'{teams} | {status}')
                continue
            elif game['status']['type']['description'] == "Final":
                print(f'{teams} | {ascore}-{hscore} | {status}')
                continue
            
            try:
                print(f"{teams} | {ascore}-{hscore} | {status} | {game['competitions'][0]['outsText']} | {game['competitions'][0]['situation']['balls']}-{game['competitions'][0]['situation']['strikes']} {game['competitions'][0]['situation']['lastPlay']['text']}")
            except KeyError:
                print(f"{teams} | {ascore}-{hscore} | {status}")
        print('\n')
        while True:
            lineup_choice= input('Do you want a lineup? y/n: ')
            if lineup_choice in ['y', 'n']:
                break
        if lineup_choice == 'y':
            os.system("clear") 
            for game in jsondata['events']:
                game_id = game['id']
                teams = game['name'] 
                print(f'{game_id} | {teams}')
            while True:
                lineup_id = input("Copy/Paste the ID of the game you want: ")
                urllineup = f'http://site.api.espn.com/apis/site/v2/sports/baseball/mlb/summary?event={lineup_id}'
                response_lineup = requests.request("GET", urllineup, headers=headers)
                if response_lineup.status_code == 200:
                    break
            try:
                os.system("clear") 
                jsonlineup = json.loads(response_lineup.text)
                print(f"This game is at {jsonlineup['gameInfo']['venue']['fullName']}")
                for pitcher in jsonlineup['boxscore']['players']:
                    if pitcher['statistics'][1]['athletes'][0]['starter']== False:
                        continue
                    pitch_team = pitcher['team']['displayName']
                    the_pitcher = pitcher['statistics'][1]['athletes'][0]['athlete']['shortName']
                    pitch_jersey = pitcher['statistics'][1]['athletes'][0]['athlete']['jersey']
                    pitch_ERA = pitcher['statistics'][1]['athletes'][0]['stats'][8]
                    print(f'SP for the {pitch_team}: {pitch_jersey}| {the_pitcher} |{pitch_ERA}')
                for team in jsonlineup['rosters']:
                    home_away = team['homeAway'].capitalize()
                    the_team = team['team']['displayName']
                    print(f'\n{home_away} team: {the_team}')
                    for player in team['roster']:
                        if player['starter'] == False:
                            continue
                        p_name = player['athlete']['displayName']
                        p_position = player['position']['abbreviation']
                        p_jersey = player['athlete']['jersey']
                        print(f'{p_jersey} | {p_name} | {p_position}')
                    print('-----------------------------')
                
                
            except KeyError:
                print("The Lineup isn't ready yet.")
                
            

if __name__ == '__main__':
    try:
        scoreboard()
    except KeyError as e:
        print(f"Looks like {e} caused an issue.")
        while True:
            restart_prog = input('Would you like to restart? y/n: ')
            if restart_prog in ['y','n']:
                break
        if restart_prog == 'y':
            scoreboard()

