'''
   booksdatasourcetest.py

   Jack Owens and Hannah Moran, 9/29/22
'''

from booksdatasource import BooksDataSource

import sys

def printUsageStatement():
    print('NAME\n\tbooks - Search for books \nSYNOPSIS\n\tbooks <S> <C>\nDESCRIPTION\n\tbooks takes a search string <S> and prints a list of books whose titles contain the string and sorts by criteria <C>.\n\t <C> can be <title> or <year>\n')
    print('NAME\n\tauthors - Search for authors\nSYNOPSIS\n\tauthors <S>\nDESCRIPTION\n\tauthors takes a search string S and prints a list of authors whose names contain the string sorted by last name then first name\n')
    print('NAME\n\tbooksinrange - Search range of years\nSYNOPSIS\n\tbooksinrange <A> <B>\nDESCRIPTION\n\tbooksinrange prints a list of books published between years <A> and <B>, inclusive\n')
    print('NAME\n\tuse - Request usage statement\nSYNOPSIS\n\tuse <flag>\nDESCRIPTION\n\tGives user description of <flag> command-line argument')

if len(sys.argv) == 1:
    listOfBooks = BooksDataSource('books1.csv').books('')
    for book in listOfBooks:
            print(book.title + ' ' + book.publication_year)
elif sys.argv[1] == '--books' or sys.argv[1] == '-b':
    if len(sys.argv) > 4:
        raise Exception('\nSyntax Error: too many arguments for books\n\nTo get help,\n Enter: python3 book.py --help\n')
    else:
        if len(sys.argv) == 2:
            listOfBooks = BooksDataSource('books1.csv').books('')
        elif len(sys.argv) == 3:
            listOfBooks = BooksDataSource('books1.csv').books(sys.argv[2])
        elif len(sys.argv) == 4:
            listOfBooks = BooksDataSource('books1.csv').books(sys.argv[2], sys.argv[3])
        for book in listOfBooks:
            print(book.title + ' ' + book.publication_year)
elif sys.argv[1] == '--authors' or sys.argv[1] == '-a':
    if len(sys.argv) > 3:
        raise Exception('\nSyntax Error: too many arguments for authors\n\nTo get help,\n Enter: python3 book.py --help\n')
    else:
        if len(sys.argv) == 2:
            listOfAuthors = BooksDataSource('books1.csv').authors('')
        elif len(sys.argv) == 3:
            listOfAuthors = BooksDataSource('books1.csv').authors(sys.argv[2])
        for author in listOfAuthors:
            if author.death_year != None:
                print(author.given_name + ' ' + author.surname + ' ' + author.birth_year + '-' + author.death_year)
            else:
                print(author.given_name + ' ' + author.surname + ' ' + author.birth_year + '-')
elif sys.argv[1] == '--range' or sys.argv[1] == '-r':
    if len(sys.argv) > 4:
        raise Exception('\nSyntax Error: too many arguments for range\n\nTo get help,\n Enter: python3 book.py --help\n')
    else:
        if len(sys.argv) == 2:
            listOfBooks = BooksDataSource('books1.csv').books_between_years('')
        elif len(sys.argv) == 3:
            if sys.argv[2].isnumeric() != True:
                raise Exception('\nSyntax Error: start year must be a number\n\nTo get help,\n Enter: python3 book.py --help\n')
                
            else:
                listOfBooks = BooksDataSource('books1.csv').books_between_years(sys.argv[2])
                for book in listOfBooks:
                    print(book.title + ' ' + book.publication_year)
        elif len(sys.argv) == 4:
            if sys.argv[2].isnumeric() != True or sys.argv[3].isnumeric() != True:
                raise Exception('\nSyntax Error: start year and end year must be numbers\n\nTo get help,\n Enter: python3 book.py --help\n')
            elif sys.argv[2] > sys.argv[3]:
                raise Exception('\nSyntax Error: start year must be less than end year\n\nTo get help,\n Enter: python3 book.py --help\n')
            else:
                listOfBooks = BooksDataSource('books1.csv').books_between_years(sys.argv[2], sys.argv[3])
                for book in listOfBooks:
                    print(book.title + ' ' + book.publication_year)
elif sys.argv[1] == '-help' or sys.argv[1] == '-h':
    printUsageStatement()
else:
    raise Exception("\nInvalid Input: '" + sys.argv[1] + "' is not a function\n\nTo get help,\n Enter: python3 book.py --help\n")
    printUsageStatement()
