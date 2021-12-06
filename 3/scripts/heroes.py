""""
1. id (PK)
2. name
3. attack_type -> Melee/Ranged
4. armor
5. complexity
6. type -> Strength/Intelligence/Agility (enum)
7. hp
8. mana
"""""

import requests
url = "https://api.opendota.com/api/heroStats"

resp = requests.get(url)
resp_data = resp.json()

hero_data  = []
for hero in resp_data:
    id = hero['id']
    name = hero['localized_name']
    attack_type = hero['attack_type']
    primary_attr = hero['primary_attr']
    type = "Intelligence"
    if primary_attr == "agi":
        type = "Agility"
    elif primary_attr == "str":
        type = "Strength"

    armor = hero['base_armor']
    complexity = hero['move_speed']
    hp = hero['base_health']
    mana = hero['base_mana']

    hero_data.append([id, name, attack_type, armor, complexity, type, hp, mana])

import csv
fout = open('../data/heroes.csv', 'w')
writer = csv.writer(fout)
for hero in hero_data:
    writer.writerow(hero)
fout.close()