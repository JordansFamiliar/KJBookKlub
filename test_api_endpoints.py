import unittest
import json
from app import app, db, Book, Author, Genre

class TestAPIEndpoints(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def tearDown(self):
        pass

    def test_get_all_books(self):
        response = self.app.get('/mysite/books')
        self.assertEqual(response.status_code, 200)

    def test_get_book_by_id(self):
        response = self.app.get('/mysite/books/1')
        self.assertEqual(response.status_code, 200)

    def test_add_book(self):
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
        data = {'title': 'Updated Title'}
        response = self.app.put('/mysite/books/1', json=data)
        self.assertEqual(response.status_code, 200)

    def test_delete_book(self):
        response = self.app.delete('/mysite/books/1')
        self.assertEqual(response.status_code, 200)

