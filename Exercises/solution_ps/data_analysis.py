import csv
from collections import Counter, defaultdict
from readrides import read_rides_as_dictionary
from pprint import pprint

rows_dict = read_rides_as_dictionary('../../Data/ctabus.csv')
# print(rows_dict[0])


# Q1
routes_unique = []
for i in rows_dict:
    routes_unique.append((i['route']))
    
# print(len(set(routes_unique))) # Q1 - 181

# Q2
routes22_unique = []
routes22_unique = [int(i['rides']) for i in rows_dict if (i['route'] == '22') & (i['date']=='02/02/2011')]
# print(sum(routes22_unique))

# Q3
rides_route = Counter()
for i in rows_dict:
    # rides_int = int(i['rides'])
    rides_route[i['route']] += int(i['rides'])

# for route, count in rides_route.most_common():
#     print('%5s %10d' % (route, count))
# pprint(rides_route)

# Q4

rides_route_year = defaultdict(Counter)
for i in rows_dict:
    # rides_int = int(i['rides'])
    year_data = i['date'].split('/')[2]
    if year_data in ['2001', '2011']:
        rides_route_year[year_data][i['route']] += int(i['rides'])

diffs = rides_route_year['2011'].copy()
diffs.subtract(rides_route_year['2001'])
print(diffs)

for i in diffs.most_common(5):
    print(i)

for i in diffs.most_common()[-5:]:
    print(i)
# for i in rides_route_year:
#     rides_route_year_01_11 