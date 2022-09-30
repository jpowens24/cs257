'''
   booksdatasourcetest.py

   Jack Owens and Hannah Moran, 9/29/22
'''

from booksdatasource import BooksDataSource

import sys

if sys.argv[1] == 'books':
    if len(sys.argv) > 4:
        print('Syntax Error: too many arguments for books')
        print('NAME\n\tbooks - Search for books \nSYNOPSIS\n\tbooks <S> <C>\nDESCRIPTION\n\tbooks takes a search string <S> and prints a list of books whose titles contain the string and sorts by criteria <C>.\n\t <C> can be <title> or <year>')
    else:
        if len(sys.argv) == 2:
            listOfBooks = BooksDataSource('books1.csv').books('')
        elif len(sys.argv) == 3:
            listOfBooks = BooksDataSource('books1.csv').books(sys.argv[2])
        elif len(sys.argv) == 4:
            listOfBooks = BooksDataSource('books1.csv').books(sys.argv[2], sys.argv[3])
        for book in listOfBooks:
            print(book.title + ' ' + book.publication_year)
elif sys.argv[1] == 'authors':
    if len(sys.argv) > 4:
        print('Syntax Error: too many arguments for authors')
        print('NAME\n\tauthors - Search for authors\nSYNOPSIS\n\tauthors <S>\nDESCRIPTION\n\tauthors takes a search string S and prints a list of authors whose names contain the string sorted by last name then first name')
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
elif sys.argv[1] == 'booksinrange':
    if len(sys.argv) > 4:
        print('Syntax Error: too many arguments for booksinrange')
        print('NAME\n\tbooksinrange - Search range of years\nSYNOPSIS\n\tbooksinrange <A> <B>\nDESCRIPTION\n\tbooksinrange prints a list of books published between years <A> and <B>, inclusive')
    else:
        if len(sys.argv) == 2:
            listOfBooks = BooksDataSource('books1.csv').books_between_years('')
        elif len(sys.argv) == 3:
            if sys.argv[2].isnumeric != True:
                print('Syntax Error: start year must be a number')
                print('NAME\n\tbooksinrange - Search range of years\nSYNOPSIS\n\tbooksinrange <A> <B>\nDESCRIPTION\n\tbooksinrange prints a list of books published between years <A> and <B>, inclusive')
            else:
                listOfBooks = BooksDataSource('books1.csv').books_between_years(sys.argv[2])
                for book in listOfBooks:
                    print(book.title + ' ' + book.publication_year)
        elif len(sys.argv) == 4:
            if sys.argv[2].isnumeric != True or sys.argv[3].isnumeric != True:
                print('Syntax Error: start year and end year must be numbers')
                print('NAME\n\tbooksinrange - Search range of years\nSYNOPSIS\n\tbooksinrange <A> <B>\nDESCRIPTION\n\tbooksinrange prints a list of books published between years <A> and <B>, inclusive')
            else:
                listOfBooks = BooksDataSource('books1.csv').books_between_years(sys.argv[2], sys.argv[3])
                for book in listOfBooks:
                    print(book.title + ' ' + book.publication_year)
elif sys.argv[1] == 'use':
    print('NAME\n\tbooks - Search for books \nSYNOPSIS\n\tbooks <S> <C>\nDESCRIPTION\n\tbooks takes a search string <S> and prints a list of books whose titles contain the string and sorts by criteria <C>.\n\t <C> can be <title> or <year>\n')
    print('NAME\n\tauthors - Search for authors\nSYNOPSIS\n\tauthors <S>\nDESCRIPTION\n\tauthors takes a search string S and prints a list of authors whose names contain the string sorted by last name then first name\n')
    print('NAME\n\tbooksinrange - Search range of years\nSYNOPSIS\n\tbooksinrange <A> <B>\nDESCRIPTION\n\tbooksinrange prints a list of books published between years <A> and <B>, inclusive\n')
    print('NAME\n\tuse - Request usage statement\nSYNOPSIS\n\tuse <flag>\nDESCRIPTION\n\tGives user description of <flag> command-line argument')
else:
    pass

