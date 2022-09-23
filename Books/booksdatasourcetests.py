'''
   booksdatasourcetest.py

   Jack Owens and Hannah Moran, 9/22/22
'''

from booksdatasource import Author, Book, BooksDataSource
import unittest

class BooksDataSourceTester(unittest.TestCase):
    def setUp(self):
        self.data_source = BooksDataSource('books1.csv')

    def tearDown(self):
        pass

    def test_unique_author(self):
        authors = self.data_source.authors('Pratchett')
        self.assertTrue(len(authors) == 1)
        self.assertTrue(authors[0] == Author('Pratchett', 'Terry'))

    def test_unique_book(self):
        books = self.data_source.books('Moby Dick')
        self.assertTrue(len(books) == 1)
        self.assertTrue(books[0] == Book('Moby Dick'))
    
    def test_equal_booksByYear_emptyStringBooksBetweenYears(self):
        books_between_years = self.data_source.books_between_years(None, None)
        books = self.data_source.books(None, 'year')
        self.assertTrue(books_between_years == books)

    def test_startYear_lessThan_endYear(self):
        self.assertRaises(ValueError, self.books_between_years(2, 1))

    def test_nonIntegerInput_years(self):
        self.assertRaises(TypeError, self.data_source.books_between_years('abc', 2))
        self.assertRaises(TypeError, self.data_source.books_between_years(1, 'abc'))
        self.assertRaises(TypeError, self.data_source.books_between_years(1.8, 2))

    def test_nonStringInput_authors(self):
        self.assertRaises(TypeError, self.data_source.authors(2))
        self.assertRaises(TypeError, self.data_source.authors(2.4))
        self.assertRaises(TypeError, self.data_source.authors(True))

    def test_nonStringInput_books(self):
        self.assertRaises(TypeError, self.data_source.books(2))
        self.assertRaises(TypeError, self.data_source.books(2.4))
        self.assertRaises(TypeError, self.data_source.books(True))

    def test_AuthorEqual(self):
        author = self.data_source.Author('Pratchett', 'Terry')
        self.AssertTrue(self.data_source.Author.__eq__(author, author))

    def test_BookEqual(self):
        book = self.data_source.Book('Moby Dick')
        self.AssertTrue(self.data_source.Book.__eq__(book, book))
        
    def test_startYear_minimum(self):
        minimum1900 = self.data_source.books_between_years(1900, None)
        self.assertEqual(0, minimum1900.count(self.data_source.Book('Emma')))

    def test_endYear_maximum(self):
        maximum2000 = self.data_source.books_between_years(None, 2000)
        self.assertEqual(0, maximum2000.count(self.data_source.Book('All Clear')))

    def test_default_books(self):
        self.assertEqual(self.data_source.books(None), self.data_source.books(None, 'title'))

if __name__ == '__main__':
    unittest.main()

