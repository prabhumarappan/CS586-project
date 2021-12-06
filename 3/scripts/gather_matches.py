import csv
import glob

files = glob.glob("../data/matches/matches_*")

matches = {}

for file in files:
    f_open= open(file, 'r')
    reader = csv.reader(f_open)
    data = []
    for x in reader:
        data.append(x)
    data = data[1:]
    for d in data:
        matches[d[0]] = d
    f_open.close()

f_out = open("../data/matches.csv", 'w')
writer = csv.writer(f_out)
writer.writerow(['match_id','start','duration','radTeamId','direTeamId','radVictory'])
for match_id in matches:
    writer.writerow(matches[match_id])
f_out.close()