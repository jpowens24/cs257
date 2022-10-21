'''
   booksdatasourcetest.py

   Jack Owens, 10/20/22
'''

import sys
import psycopg2
import config

def get_connection():
    try:
        return psycopg2.connect(database=config.database,
                                user=config.user,
                                password=config.password)
    except Exception as e:
        print(e, file=sys.stderr)
        exit()

def get_athletes_by_noc(search_text):
    ''' Returns a list of the names of all athletes in the database
        whose noc contains (case-insensitively) the specified search string. '''
    athletes = []
    try:
        query = '''SELECT given_name
                   FROM athletes
                   WHERE athletes.noc = %s'''
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query, (search_text,))
        for row in cursor:
            given_name = row[0]
            athletes.append(f'{given_name}')

    except Exception as e:
        print(e, file=sys.stderr)

    connection.close()
    return athletes
    
def get_athletes_with_country():
    ''' Returns a list of the names of all athletes in the database
        whose noc contains (case-insensitively) the specified search string. '''
    athletes = []
    try:
        query = '''SELECT given_name, country
                   FROM athletes'''
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query)
        for row in cursor:
            given_name = row[0]
            country = row[1]
            athletes.append(f'{given_name}, {country}')

    except Exception as e:
        print(e, file=sys.stderr)

    connection.close()
    return athletes

def get_nocs_medals():
    ''' Returns a list of the NOCs who have won a gold medal and the number of medals they have won. '''
    nocs = []
    try:
        connection = get_connection()
        cursor = connection.cursor()
        query = "SELECT noc FROM medals WHERE medals.medal = 'Gold' ORDER BY medals.noc"
        cursor.execute(query)
        current_noc_name = ''
        current_noc_medals = 1
        for row in cursor:
            noc_name = row[0]
            if noc_name == current_noc_name:
                current_noc_medals += 1
            else:
                nocs.append(f'{current_noc_name}, {current_noc_medals}')
                current_noc_medals = 1
                current_noc_name = noc_name

    except Exception as e:
        print(e, file=sys.stderr)

    connection.close()
    return nocs

def print_usage_statement():
    usage_statement = '''Jack Owens

NAME
	olympics - Request data from olympics database
SYNOPSIS
	python3 olympics.py [criteria] [string]
DESCRIPTION
	-h, --help
        prints the help statement to the user
    -n, --noc <string>
        prints a list of athletes whose NOC matches the seach string, case-insensitive
    -m, --medal
        prints a list of NOCs in decreasing order of the number of gold medals they have won
    -c, --country
        prints a list of athletes next to their respective country'''

    print(usage_statement)

def sort_medals(list):
    sortedMedals = []
    medalTuples = []
    for medal in list:
        medalTuples.append(medal.split())
    medalTuples.remove([',', '1'])
    for medalTuple in medalTuples:
        medalTuple[1] = int(medalTuple[1])
    medalTuples = sorted(medalTuples, key=lambda x: x[1])
    for medalTuple in medalTuples:
        medalString = medalTuple[0] + ' ' + str(medalTuple[1])
        sortedMedals.append(medalString)
    return sortedMedals

def main():
    if len(sys.argv) == 1:
        print('Invalid Syntax. To get help enter: python3 olympics.py --help')
    elif len(sys.argv) == 2:
        if sys.argv[1] == '-c' or sys.argv[1] == '--country':
            listOfAthletes = get_athletes_with_country()
            for athlete in listOfAthletes:
                print(athlete)
        elif sys.argv[1] == '-m' or sys.argv[1] == '--medal':
            listOfMedals = get_nocs_medals()
            sortedMedals = sort_medals(listOfMedals)
            for medal in sortedMedals:
                print(medal)
        elif sys.argv[1] == '-h' or sys.argv[1] == '--help':
            print_usage_statement()
        else:
            print('Invalid Syntax. To get help enter: python3 olympics.py --help')
    elif len(sys.argv) == 3:
        if sys.argv[1] == '-n' or sys.argv[1] == '--noc':
            listOfAthletes = get_athletes_by_noc(sys.argv[2])
            for athlete in listOfAthletes:
                print(athlete)
        else:
            print('Invalid Syntax: To get help enter: python3 olympics.py --help')

if __name__ == '__main__':
    main()