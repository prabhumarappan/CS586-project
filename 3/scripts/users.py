
"""
   1. id (PK)
   2. username
   3. email
   4. created_at
"""
url = "https://api.opendota.com/api/proPlayers"

import requests
import random
import datetime as dt
import time
import csv

resp = requests.get(url)
resp_data = resp.json()
users = {}
teams = {}
teamusers = {}

def get(url):
    try:
        return requests.get(url)
    except Exception:
        # sleep for a bit in case that helps
        time.sleep(65)
        # try again
        return get(url)

def random_time():
    start = 1291595028
    end = 1544055828
    rand_numer = random.randint(start, end)
    return dt.datetime.fromtimestamp(rand_numer).strftime("%Y-%m-%dT%H:%M:%S.%fZ")

for user in resp_data:
    id = user['account_id']
    username = user['name']

    if username is None:
        username = user['personaname']

    email = user['steamid'] + "@steam.com"
    created_at = user['last_login']
    if not created_at:
        created_at = random_time()
    if username not in users:
        users[username] = [id, username, email, created_at]

    team_id = user['team_id']
    team_name = user['team_name']
    team_date = created_at
    if team_id not in teams and team_name:
        teams[team_id] = [team_id, team_name, team_date]
    
        if team_id not in teamusers:
            teamusers[team_id] = []
        teamusers[team_id].append([team_id, id, created_at])




# for teamid in teamusers:

#     team_url = "https://api.opendota.com/api/teams/%s/players" % (teamid)
#     print(team_url)
#     teamdata_resp = get(team_url)
#     teamdata = teamdata_resp.json()
#     for user in teamdata:
#         user_id = user['account_id']
#         username = user['name']
#         if username and username not in users and user['is_current_team_member']:
#             user_api_url = "https://api.opendota.com/api/players/" + str(user_id)
#             user_api_data = get(user_api_url).json()['profile']

#             username = user_api_data['name']
#             email = user_api_data['steamid'] + "@steam.com"
#             created_at = user_api_data['last_login'] 
#             if not created_at:
#                 created_at = random_time()

#             users[username] = [id, username, email, created_at]
            
#             teamusers[teamid].append([teamid, user_id, created_at])

teamuser_f = open('./data/teamuser.csv', 'w')
teamuser_writer = csv.writer(teamuser_f)
teamuser_writer.writerow(['team_id', 'user_id', 'date_joined'])
for team_id in teamusers:
    for team in teamusers[team_id]:
        teamuser_writer.writerow(team)

user_f = open('./data/duser.csv', 'w')
user_writer = csv.writer(user_f)
user_writer.writerow(['id', 'username', 'email', 'created_at'])
for user in users:
    user_writer.writerow(users[user])

user_f.close()

team_f = open('./data/team.csv', 'w')
team_writer = csv.writer(team_f)
team_writer.writerow(['id', 'name', 'date'])
for team_id in teams:
    team_writer.writerow(teams[team_id])

team_f.close()