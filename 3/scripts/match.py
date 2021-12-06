import requests as r
import csv
import datetime as dt

teams_f = open('../data/team.csv', 'r')
teams_reader = csv.reader(teams_f)
teams = []
for team in teams_reader:
    teams.append(team[0])
teams_f.close()

teams = teams[1:]

print(teams)

all_matches = {}

url = "https://www.datdota.com/api/matchfinder/classic?team-a=%s&team-b=%s"

for i in range(len(teams)):
    for j in range(len(teams)):
        if i == j:
            continue
        team_id_a = teams[i]
        team_id_b = teams[j]
        new_url = url % (team_id_a, team_id_b)
        print(new_url)
        matches = r.get(new_url).json()['data']['matches']
        for match in matches:
            print("MATCH IS THERE")
            match_id = match['matchId']
            start = dt.datetime.fromtimestamp(match['date']/1000).strftime("%Y-%m-%dT%H:%M:%S.%fZ")
            duration = match['duration']
            radTeamId = match['radTeamId']
            direTeamId = match['direTeamId']
            radVictory = match['radVictory']

            if match_id not in all_matches:
                all_matches[match_id] = [match_id, start, duration, radTeamId, direTeamId, radVictory]

matches_f = open('../data/matches.csv', 'w')
matches_writer = csv.writer(matches_f)
matches_writer.writerow(['match_id', 'start', 'duration', 'radTeamId', 'direTeamId', 'radVictory'])
for match_id in all_matches:
    matches_writer.writerow(all_matches[match_id])
matches_f.close()