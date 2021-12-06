import csv
import requests as r
import multiprocessing as mp

url = "https://www.datdota.com/api/players/single-performance?players=%s&heroes=%s"

users = []
heroes = []
threads = []

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

def process_for_user_hero(args):
    user_id=args[0]
    hero_id =args[1]
    new_url = url % (user_id, hero_id)
    print(new_url)
    resp_data = r.get(new_url).json()['data']
    
    datas = []
    for match in resp_data:
        match_id = match['matchId']
        victory = match['victory']
        kills = match['kills']
        deaths = match['deaths']
        assists = match['assists']
        
        datas.append([user_id, hero_id, match_id, victory, kills, deaths, assists])
    
    if datas:
        userheros_f = open('../trydata/userheros_%s_%s.csv' % (user_id, hero_id), 'w')
        writer = csv.writer(userheros_f)
        writer.writerow(['user_id', 'hero_id', 'match_id', 'victory', 'kills', 'deaths', 'assists'])
    
        for data in datas:
            writer.writerow(data)
    
        userheros_f.close()


if __name__ == '__main__':
    nprocs = mp.cpu_count()
    pool = mp.Pool(processes=(nprocs))
    args = []
    for i in range(len(users)):
        for j in range(len(heroes)):
            user_id = users[i]
            heroe_id = heroes[j]
            args.append([user_id, heroe_id])

    pool.map(process_for_user_hero, args)

    pool.close()
    pool.join()

    print("DONE")


