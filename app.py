from flask import Flask, request, jsonify
from models import db, Author, Genre, Book
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/KJBookKlub/mysite/book_collection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
migrate = Migrate(app, db)

@app.route('/mysite/books', methods=['GET'])
def get_books():
    """Endpoint to retrieve all books in the collection."""
    books = Book.query.all()
    books_data = []
    for book in books:
        book_data = {
            'id': book.id,
            'title': book.title,
            'publication_date': book.publication_date,
	    'isbn': book.isbn,
	    'author': {
		'id': book.author.id,
		'name': book.author.name
	    },
	    'genre': {
		'id': book.genre.id,
		'name': book.genre.name
	    },
	    'cover_image': book.cover_image
        }
        books_data.append(book_data)
    return jsonify(books_data)

@app.route('/mysite/books/<string:book_id>', methods=['GET'])
def get_book(book_id):
    """Endpoint to retrieve a specific book by its ID."""
    book = Book.query.get(book_id)
    if not book:
        return jsonify({'error': 'Book not found'}), 404

    book_data = {
        'id': book.id,
        'title': book.title,
        'publication_date': book.publication_date,
        'isbn': book.isbn,
        'author': {
            'id': book.author.id,
            'name': book.author.name
        },
        'genre': {
            'id': book.genre.id,
            'name': book.genre.name
        },
        'cover_image': book.cover_image
    }
    return jsonify(book_data)

@app.route('/mysite/books', methods=['POST'])
def add_book():
    """Endpoint to add a new book to the collection."""
    data = request.json

    title = data.get('title')
    publication_date = data.get('publication_date')
    isbn = data.get('isbn')
    author_name = data.get('author_name')
    genre_name = data.get('genre_name')
    cover_image = data.get('cover_image')

    if not title or not author_name or not genre_name:
        return jsonify({'error': 'Title, author name, and genre name are required'}), 400

    author = Author.query.filter_by(name=author_name).first()
    if not author:
        author = Author(name=author_name)
        db.session.add(author)
        db.session.commit()

    genre = Genre.query.filter_by(name=genre_name).first()
    if not genre:
        genre = Genre(name=genre_name)
        db.session.add(genre)
        db.session.commit()

    new_book = Book(
        title=title,
        publication_date=publication_date,
        isbn=isbn,
        author_id=author.id,
        genre_id=genre.id,
        cover_image=cover_image
    )

    db.session.add(new_book)
    db.session.commit()

    return jsonify({'message': 'Book added successfully', 'id': new_book.id}), 201

@app.route('/mysite/books/<string:book_id>', methods=['PUT'])
def update_book(book_id):
    """Endpoint to update an existing book in the collection."""
    book = Book.query.get(book_id)
    if not book:
        return jsonify({'error': 'Book not found'}), 404

    data = request.json

    if 'title' in data:
        book.title = data['title']
    if 'publication_date' in data:
        book.publication_date = data['publication_date']
    if 'isbn' in data:
        book.isbn = data['isbn']
    if 'author_id' in data:
        author = Author.query.get(data['author_id'])
        if not author:
            db.session.add(author)
            db.session.commit()
        book.author_id = data['author_id']
    if 'genre_id' in data:
        genre = Genre.query.get(data['genre_id'])
        if not genre:
            db.session.add(genre)
            db.session.commit()
        book.genre_id = data['genre_id']
    if 'cover_image' in data:
        book.cover_image = data['cover_image']

    db.session.commit()

    return jsonify({'message': 'Book updated successfully'}), 200

@app.route('/mysite/books/<string:book_id>', methods=['DELETE'])
def delete_book(book_id):
    """Endpoint to delete a book from collection."""
    book = Book.query.get(book_id)
    if not book:
        return jsonify({'error': 'Book not found'}), 404

    db.session.delete(book)
    db.session.commit()

    return jsonify({'message': 'Book deleted successfully'}), 200

@app.route('/mysite/genres/<string:genre_id>/books', methods=['GET'])
def get_books_by_genre(genre_id):
    """Endpoint to retrieve all books belonging to a specific genre."""
    genre = Genre.query.get(genre_id)
    if not genre:
        return jsonify({'error': 'Genre not found'}), 404

    books = Book.query.filter_by(genre_id=genre_id).all()
    books_data = []
    for book in books:
        book_data = {
            'id': book.id,
            'title': book.title,
            'publication_date': book.publication_date,
            'isbn': book.isbn,
            'author': {
                'id': book.author.id,
                'name': book.author.name
            },
            'genre': {
            'id': book.genre.id,
            'name': book.genre.name
            },
            'cover_image': book.cover_image
        }
        books_data.append(book_data)

    return jsonify(books_data)

@app.route('/mysite/authors/<string:author_id>/books', methods=['GET'])
def get_books_by_author(author_id):
    """Endpoint to retrieve all books written by a specific author."""
    author = Author.query.get(author_id)
    if not author:
        return jsonify({'error': 'Author not found'}), 404

    books = Book.query.filter_by(author_id=author_id).all()
    books_data = []
    for book in books:
        book_data = {
            'id': book.id,
            'title': book.title,
            'publication_date': book.publication_date,
            'isbn': book.isbn,
            'author': {
                'id': book.author.id,
                'name': book.author.name
            },
            'genre': {
                'id': book.genre.id,
                'name': book.genre.name
            },
            'cover_image': book.cover_image
        }
        books_data.append(book_data)

    return jsonify(book_data)

if __name__ == '__main__':
    app.run(debug=True)
