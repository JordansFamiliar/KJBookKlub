import unittest
import json
from app import app, db, Book, Author, Genre

class TestAPIEndpoints(unittest.TestCase):
    """
    Unit tests for API endpoints.
    """

    def setUp(self):
        """
        Test for the setup of the app.
        """
        self.app = app.test_client()
        self.app.testing = True

    def tearDown(self):
        pass

    def test_get_all_books(self):
        """
        Test the GET /mysite/books endpoint to retrieve all books in the collection.
        """
        response = self.app.get('/mysite/books')
        self.assertEqual(response.status_code, 200)

    def test_get_book_by_id(self):
        """
        Test the GET /mysite/books/<book_id> endpoint to retrieve details of a specific book by ID.
        """
        response = self.app.get('/mysite/books/1')
        self.assertEqual(response.status_code, 200)

    def test_add_book(self):
        """
        Test the POST /mysite/books endpoint to add a new book to the collection.
        """
        data = {
            'title': 'Test Book',
            'publication_date': '2022-01-01',
            'isbn': '1234567890',
            'author_name': 'Test Author',
            'genre_name': 'Test Genre',
            'cover_image': 'http://example.com/cover_image.jpg'
        }
        response = self.app.post('/mysite/books', json=data)
        self.assertEqual(response.status_code, 201)

    def test_update_book(self):
        """
        Test the PUT /mysite/books/<book_id> endpoint to update details of a specific book by ID.
        """
        data = {'title': 'Updated Title'}
        response = self.app.put('/mysite/books/1', json=data)
        self.assertEqual(response.status_code, 200)

    def test_delete_book(self):
        """
        Test the DELETE /mysite/books/<book_id> endpoint to delete a book from the collection by ID.
        """
        response = self.app.delete('/mysite/books/1')
        self.assertEqual(response.status_code, 200)

    def test_get_books_by_genre_id(self):
        """
        Test the GET /mysite/genres/<genre_id>/books endpoint to retrieve all books of a specific genre.
        """
        response = self.app.get('/mysite/genres/1/books')
        self.assertEqual(response.status_code, 200)

    def test_get_books_by_author_id(self):
        """
        Test the GET /mysite/authors/<author_id>/books endpoint to retrieve all books of a specific author.
        """
        response = self.app.get('/mysite/authors/1/books')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
