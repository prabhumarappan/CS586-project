import csv
import glob

files = glob.glob("../trydata/userheros_*")

user_heros = []

for file in files:
    f_open= open(file, 'r')
    reader = csv.reader(f_open)
    data = []
    for x in reader:
        data.append(x)

    user_heros.extend(data[1:])
    f_open.close()

f_out = open("../data/userheros.csv", 'w')
writer = csv.writer(f_out)
writer.writerow(['user_id','hero_id','match_id','victory','kills','deaths','assists'])
for userhero in user_heros:
    writer.writerow(userhero)
f_out.close()