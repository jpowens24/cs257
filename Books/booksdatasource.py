#!/usr/bin/env python3
'''
    booksdatasource.py
    Jeff Ondich, 21 September 2022

    For use in the "books" assignment at the beginning of Carleton's
    CS 257 Software Design class, Fall 2022.
'''

import csv
import sys

class Author:
    def __init__(self, surname='', given_name='', birth_year=None, death_year=None):
        self.surname = surname
        self.given_name = given_name
        self.birth_year = birth_year
        self.death_year = death_year

    def __eq__(self, other):
        ''' For simplicity, we're going to assume that no two authors have the same name. '''
        return self.surname == other.surname and self.given_name == other.given_name

class Book:
    def __init__(self, title='', publication_year=None, authors=[]):
        ''' Note that the self.authors instance variable is a list of
            references to Author objects. '''
        self.title = title
        self.publication_year = publication_year
        self.authors = authors

    def __eq__(self, other):
        ''' We're going to make the excessively simplifying assumption that
            no two books have the same title, so "same title" is the same
            thing as "same book". '''
        return self.title == other.title

class BooksDataSource:
    def __init__(self, books_csv_file_name):
        ''' The books CSV file format looks like this:

                title,publication_year,author_description

            For example:

                All Clear,2010,Connie Willis (1945-)
                "Right Ho, Jeeves",1934,Pelham Grenville Wodehouse (1881-1975)

            This __init__ method parses the specified CSV file and creates
            suitable instance variables for the BooksDataSource object containing
            a collection of Author objects and a collection of Book objects.
        '''
        for line in books_csv_file_name:
            cursor = 0
            if line[0] == '"':
                cursor = 1
                splitChar = '"'
                y = 2
            else:
                cursor = 0
                splitChar = ","  
                y = 1 
            title = ''
            while line[cursor] != splitChar:
                title += line[cursor]
                cursor += 1
            cursor += y
            publication_year = ''
            while line[cursor] != ",":
                publication_year += line[cursor]
                cursor += 1
            cursor += 1
            authors = []
            while line[cursor] != "\n":   #Parse book's authors until end of line
                if line[cursor] == ' ':
                    cursor += 5 #skip " and "
                author_given_name = ''
                while line[cursor] != ' ':
                    author_given_name += line[cursor]
                    cursor += 1
                cursor += 1 #skip space
                author_surname = ''
                while line[cursor] != '(':
                    author_surname += line[cursor]
                    cursor += 1
                author_surname = author_surname[:-1] #remove space from end of surname
                cursor += 1 #skip open parenthesis
                author_birth_year = ''
                while line[cursor] != '-':
                    author_birth_year += line[cursor]
                    cursor += 1
                cursor += 1 #skip dash
                author_death_year = ''
                while line[cursor] != ')':
                    author_death_year += line[cursor]
                    cursor += 1
                current_author = Author(author_surname, author_given_name, author_birth_year, author_death_year)
                authors.append(current_author)
                cursor += 1 #skip space
            print(title + " " + publication_year + ' ' + authors[0].given_name + ' ' + authors[0].surname + ' ' + authors[0].birth_year + ' ' + authors[0].death_year)
        pass

    def authors(self, search_text=None):
        ''' Returns a list of all the Author objects in this data source whose names contain
            (case-insensitively) the search text. If search_text is None, then this method
            returns all of the Author objects. In either case, the returned list is sorted
            by surname, breaking ties using given name (e.g. Ann Brontë comes before Charlotte Brontë).
        '''
        return []

    def books(self, search_text=None, sort_by='title'):
        ''' Returns a list of all the Book objects in this data source whose
            titles contain (case-insensitively) search_text. If search_text is None,
            then this method returns all of the books objects.

            The list of books is sorted in an order depending on the sort_by parameter:

                'year' -- sorts by publication_year, breaking ties with (case-insenstive) title
                'title' -- sorts by (case-insensitive) title, breaking ties with publication_year
                default -- same as 'title' (that is, if sort_by is anything other than 'year'
                            or 'title', just do the same thing you would do for 'title')
        '''
        return []

    def books_between_years(self, start_year=None, end_year=None):
        ''' Returns a list of all the Book objects in this data source whose publication
            years are between start_year and end_year, inclusive. The list is sorted
            by publication year, breaking ties by title (e.g. Neverwhere 1996 should
            come before Thief of Time 1996).

            If start_year is None, then any book published before or during end_year
            should be included. If end_year is None, then any book published after or
            during start_year should be included. If both are None, then all books
            should be included.
        '''
        return []

if __name__ == '__main__':
    with open('books1.csv') as file:
        BooksDataSource(file)
