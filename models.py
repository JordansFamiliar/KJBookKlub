from flask_sqlalchemy import SQLAlchemy
import uuid

db = SQLAlchemy()

class Author(db.Model):
    """Model representing an author."""
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = db.Column(db.String(100), nullable=False)

class Genre(db.Model):
    """Model representing a genre."""
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)

class Book(db.Model):
    """Model representing a book."""
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    title = db.Column(db.String(200), nullable=False)
    publication_date = db.Column(db.String(20), nullable=True)
    isbn = db.Column(db.String(20))
    author_id = db.Column(db.String(36), db.ForeignKey('author.id'))
    genre_id = db.Column(db.String(36), db.ForeignKey('genre.id'))
    cover_image = db.Column(db.String(255))

    author = db.relationship('Author', backref='books')
    genre = db.relationship('Genre', backref='books')
