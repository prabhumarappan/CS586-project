import csv

matches_f = open("../data/matches.csv", 'r')
matches = {}
matches_reader = csv.reader(matches_f)
for user in matches_reader:
    try:
        matches[user[0]] = True
    except Exception as e:
        print(e)
matches_f.close()

users_f = open("../data/duser.csv", 'r')
users = {}
users_reader = csv.reader(users_f)
for user in users_reader:
    try:
        users[user[0]] = True
    except Exception as e:
        print(e)
users_f.close()

inp = open("../data/userheros.csv", 'r')

output_teamusers = []

inp_reader = csv.reader(inp)
for itr, data in enumerate(inp_reader):
    if itr == 0:
        continue
    if data[2] in matches and data[0] in users:
        output_teamusers.append(data)
    else:
        print("HELLO")

inp.close()

out = open('../data/userheros2.csv', 'w')
out_writer = csv.writer(out)
for data in output_teamusers:
    out_writer.writerow(data)
out.close()