import requests as r
import csv
import datetime as dt
import multiprocessing as mp

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

def process_for_each(args):
    team_id_a = args[0]
    team_id_b = args[1]
    new_url = url % (team_id_a, team_id_b)
    print(new_url)
    matches = r.get(new_url).json()['data']['matches']

    datas = []
    
    for match in matches:
        print("MATCH IS THERE")
        match_id = match['matchId']
        start = dt.datetime.fromtimestamp(match['date']/1000).strftime("%Y-%m-%dT%H:%M:%S.%fZ")
        duration = match['duration']
        radTeamId = match['radTeamId']
        direTeamId = match['direTeamId']
        radVictory = match['radVictory']

        datas.append([match_id, start, duration, radTeamId, direTeamId, radVictory])

    if datas:
        matches_f = open('../data/matches/matches_%s_%s.csv'%(team_id_a, team_id_b), 'w')
        matches_writer = csv.writer(matches_f)
        matches_writer.writerow(['match_id', 'start', 'duration', 'radTeamId', 'direTeamId', 'radVictory'])
        for data in datas:
            matches_writer.writerow(data)
        matches_f.close()

if __name__ == '__main__':
    nprocs = mp.cpu_count()
    pool = mp.Pool(processes=(nprocs))
    args = []
    for i in range(len(teams)):
        for j in range(len(teams)):
            if i == j:
                continue
            team_id_a = teams[i]
            team_id_b = teams[j]
            args.append([team_id_a, team_id_b])

    pool.map(process_for_each, args)

    pool.close()
    pool.join()

    print("DONE")