url = "https://api.opendota.com/api/heroStats"


url2 = "https://www.dota2.com/datafeed/herodata?language=english&hero_id="


import requests
resp = requests.get(url)
resp_data = resp.json()

skills = []
hero_skills = []

for hero in resp_data:
    hero_id = hero['id']
    print(hero_id)
    hero_url = url2 + str(hero_id)
    hero_resp = requests.get(hero_url)
    hero_data = hero_resp.json()['result']['data']['heroes'][0]
    abilities = hero_data['abilities']
    for ability in abilities:
        id = ability['id']
        name = ability['name_loc']
        description = ability['desc_loc']
        skills.append([id, name, description])
        hero_skills.append([hero_id, id])

skill_f = open('../data/skill.csv', 'w')
import csv
skill_writer = csv.writer(skill_f)
skill_writer.writerow(['id', 'name', 'description'])
for skill in skills:
    skill_writer.writerow(skill)
skill_f.close()

heroskill_f = open('../data/heroskill.csv', 'w')
heroskill_writer = csv.writer(heroskill_f)
heroskill_writer.writerow(['hero_id', 'skill_id'])
for heroskill in hero_skills:
    heroskill_writer.writerow(heroskill)
heroskill_f.close()
    
