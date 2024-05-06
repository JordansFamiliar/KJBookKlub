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


