import csv

users_f = open("../data/duser.csv", 'r')
users = {}
users_reader = csv.reader(users_f)
for user in users_reader:
    try:
        users[user[0]] = True
    except Exception as e:
        print(e)
users_f.close()

inp = open("../data/teamuser.csv", 'r')

output_teamusers = []

inp_reader = csv.reader(inp)
for itr, data in enumerate(inp_reader):
    if itr == 0:
        continue
    if data[1] in users:
        output_teamusers.append(data)
    else:
        print(data[1])

inp.close()

# print(output_teamusers)