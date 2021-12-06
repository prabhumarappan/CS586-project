import requests as r
import random
import datetime as dt
import csv

url = "https://www.datdota.com/api/teams/performances?default=true"

teams = []

team_resp = r.get(url)
team_data = team_resp.json()['data']

def random_time():
    start = 1291595028
    end = 1544055828
    rand_numer = random.randint(start, end)
    return dt.datetime.fromtimestamp(rand_numer).strftime("%Y-%m-%dT%H:%M:%S.%fZ")

for team in team_data:
    team_id = team['team']['valveId']
    if team_id >= 0:
        name = team['team']['name']
        date = random_time()
        teams.append([team_id, name, date])

team_f = open('../data/team.csv', 'w')
team_writer = csv.writer(team_f)
team_writer.writerow(['id', 'name', 'date'])
for team in teams:
    team_writer.writerow(team)
team_f.close()

team_users = {}
users = {}
team_api = "https://www.datdota.com/api/players/performances?teams=%s"
for team in teams:
    team_id = team[0]
    team_api_new = team_api % team_id
    print(team_api_new)
    if team_id not in team_users:
        team_users[team_id] = []
    team_api_data = r.get(team_api_new).json()['data']
    for user in team_api_data:
        user_id = user['steamId']
        username = user['nickname']
        if username not in users and username:
            wins = user['wins']
            losses = user['losses']
            total = user['total']
            email = '%s@steam.com' % user_id
            created_at = random_time()

            users[username] = ([user_id, username, wins, losses, total, email, created_at])
            team_users[team_id].append([team_id, user_id, created_at])
    
user_f = open('../data/duser.csv', 'w')
user_writer = csv.writer(user_f)
user_writer.writerow(['id', 'username', 'wins', 'losses', 'total', 'email', 'created_at'])
for user in users:
    user_writer.writerow(users[user])
user_f.close()



teamuser_f = open('../data/teamuser.csv', 'w')
teamuser_writer = csv.writer(teamuser_f)
teamuser_writer.writerow(['team_id', 'user_id', 'date_joined'])
for team_id in team_users:
    for team in team_users[team_id]:
        teamuser_writer.writerow(team)
teamuser_f.close()