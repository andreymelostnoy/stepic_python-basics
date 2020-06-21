import csv, re

crimes_2015 = []
with open("Crimes.csv", "r") as f:
    reader = csv.reader(f)
    date_regex = r"\d\d/\d\d/2015"
    for row in reader:
        if re.match(date_regex, row[2]):
            crimes_2015.append(row[5])

crimes = dict((x, crimes_2015.count(x))
              for x in set(crimes_2015) if crimes_2015.count(x) > 1)

for crime in sorted(crimes.items(), key=lambda para: para[1], reverse=True):
    print(crime)
    break
# print(crimes)
