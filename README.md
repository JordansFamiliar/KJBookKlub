# Book Collection API

## Description
The Book Collection API is a RESTful web service built with Flask and SQLAlchemy that allows users to manage a collection of books. Users can perform operations such as adding, updating, deleting, and retrieving books from the collection. Each book entry includes details such as title, publication date, ISBN, author, genre, and cover image.

## Technologies Used
- Python
- Flask
- SQLAlchemy
- SQLite

## Endpoints
- **GET /mysite/books**: Retrieve all books in the collection.
- **GET /mysite/books/<book_id>**: Retrieve details of a specific book by ID.
- **POST /mysite/books**: Add a new book to the collection.
- **PUT /mysite/books/<book_id>**: Update details of a specific book by ID.
- **DELETE /mysite/books/<book_id>**: Delete a book from the collection by ID.
- **GET /mysite/genres/<genre_id>/books**: Retrieve all books of a specific genre.
- **GET /mysite/authors/<author_id>/books**: Retrieve all books of a specific author.

## Authors
- Jordan Williams: [jordanlw1997@gmail.com](mailto:jordanlw1997@gmail.com)
- Keitumetse Molefe: [kr.molefe98@gmail.com](mailto:kr.molefe98@gmail.com)
