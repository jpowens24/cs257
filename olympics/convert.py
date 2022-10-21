'''
   convert.py

   Jack Owens, 10/11/22
'''

import csv

noc_regions = open('noc_regions.csv')
nocs = open('nocs.csv', 'r+')
nocs_csvwriter = csv.writer(nocs)
nocscolumns = ['noc', 'region']
nocs_csvwriter.writerow(nocscolumns)
firstRow = True
for line in noc_regions:
    if firstRow == True:
        firstRow = False
    else:
        noc = ''
        cursor = 0
        while line[cursor] != ',':
            noc += line[cursor]
            cursor += 1
        cursor += 1
        region = ''
        while line[cursor] != ',':
            region += line[cursor]
            cursor += 1
        row = []
        row.append(noc)
        row.append(region)
        nocs_csvwriter.writerow(row)

noc_regions.close()
nocs.close()

athlete_events = open('athlete_events.csv')
athletes = open('athletes.csv', 'r+')
athletes_csvwriter = csv.writer(athletes)
athletescolumns = ['id', 'name', 'height', 'weight', 'country', 'noc']
athletes_csvwriter.writerow(athletescolumns)

current_id = 'ID'
for line in athlete_events:
    id = ''
    cursor = 1
    while line[cursor] != '"':
        id += line[cursor]
        cursor += 1
    cursor += 3
    if id != current_id:
        current_id = id

        name = ''
        while line[cursor] != ',':
            name += line[cursor]
            cursor += 1
        cursor += 2
        name = name[:-1]

        for i in range(2):
            while line[cursor] != ',':
                cursor += 1
            cursor += 1

        height = ''
        while line[cursor] != ',':
            height += line[cursor]
            cursor += 1
        cursor += 1

        weight = ''
        while line[cursor] != ',':
            weight += line[cursor]
            cursor += 1
        cursor += 2

        country = ''
        while line[cursor] != '"':
            country += line[cursor]
            cursor += 1
        cursor += 3

        athlete_noc = ''
        while line[cursor] != '"':
            athlete_noc += line[cursor]
            cursor += 1

        row = []
        row.append(id)
        row.append(name)
        # row.append(height)
        # row.append(weight)
        row.append(country)
        row.append(athlete_noc)

        athletes_csvwriter.writerow(row)
athletes.close()
athlete_events.close()

athlete_events = open('athlete_events.csv')
medals = open('medals.csv', 'r+')
medals_csvwriter = csv.writer(medals)
medalscolumns = ['id', 'noc', 'medal']
medals_csvwriter.writerow(medalscolumns)

id = 0
for line in athlete_events:
    if id == 0:
        id += 1
    else:
        cursor = 1
        for i in range(7):
            while line[cursor] != ',':
                cursor += 1
            cursor += 1
        cursor += 1
        
        medal_noc = ''
        while line[cursor] != '"':
            medal_noc += line[cursor]
            cursor += 1
        cursor += 1
        
        for i in range(7):
            while line[cursor] != ',':
                cursor += 1
            cursor += 1

        medal = ''
        if line[cursor] != 'N':
            cursor += 1
            while line[cursor] != '"':
                medal += line[cursor]
                cursor += 1

        if medal == 'Gold' or medal == 'Bronze' or medal == 'Silver':
            row = []
            row.append(id)
            row.append(medal_noc)
            row.append(medal)

            medals_csvwriter.writerow(row)
            id += 1
medals.close()
athlete_events.close()


athlete_events = open('athlete_events.csv')
olympic_games = open('olympic_games.csv', 'r+')
games_csvwriter = csv.writer(olympic_games)
games = []
id = 0
gamescolumns = ['id', 'year', 'season', 'city']
games_csvwriter.writerow(gamescolumns)
for line in athlete_events:
    cursor = 1
    for i in range(9):
        while line[cursor] != ',': #Skip name
            cursor += 1
        cursor += 1
    year = ''
    while line[cursor] != ',':
        year += line[cursor]
        cursor += 1
    cursor += 2
    if year != '"Year"':
        season = ''
        while line[cursor] != '"':
            season += line[cursor]
            cursor += 1
        cursor += 3
        
        city = ''
        while line[cursor] != '"':
            city += line[cursor]
            cursor += 1

        row = []
        row.append(year)
        row.append(season)
        row.append(city)
        if games.count(row) == 0:
            games.append(row)
            id += 1
            newrow = []
            newrow.append(id)
            newrow.append(year)
            newrow.append(season)
            newrow.append(city)
            games_csvwriter.writerow(newrow)
olympic_games.close()
athlete_events.close()