import datetime
date = input().split()
for i in range(len(date)):
    date[i] = int(date[i])
days = int(input())

result = datetime.date(*date) + datetime.timedelta(days=days)
print(result.year, result.month, result.day)
