import csv
import requests as r

url = "https://www.datdota.com/api/players/single-performance?players=%s&heroes=%s"

users = []
heroes = []

users_f = open('../data/duser.csv', 'r')
heroes_f = open('../data/heroes.csv', 'r')
users_reader = csv.reader(users_f)
heroes_reader = csv.reader(heroes_f)

for user in users_reader:
    users.append(user[0])

for heroe in heroes_reader:
    heroes.append(heroe[0])

users = users[1:]
heroes = heroes[1:]

users_f.close()
heroes_f.close()

userheros = []

for i in range(len(users)):
    for j in range(len(heroes)):
        user_id = users[i]
        heroe_id = heroes[j]

        new_url = url % (user_id, heroe_id)

        print(new_url)
        
        resp_data = r.get(new_url).json()['data']
        for match in resp_data:
            match_id = match['matchId']
            victory = match['victory']
            kills = match['kills']
            deaths = match['deaths']
            assists = match['assists']

            userheros.append([user_id, heroe_id, match_id, victory, kills, deaths, assists])


userheros_f = open('userheros.csv', 'w')
writer = csv.writer(userheros_f)
writer.writerow(['user_id', 'hero_id', 'match_id', 'victory', 'kills', 'deaths', 'assists'])
for userhero in userheros:
    writer.writerow(userhero)
userheros_f.close()