from flask_sqlalchemy import SQLAlchemy
import uuid
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


# Define database models
class Author(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=uuid.uuid4)
    name = db.Column(db.String(100), nullable=False)
    birth_date = db.Column(db.String(20))
    nationality = db.Column(db.String(50))

    @staticmethod
    def generate_id():
        return str(uuid.uuid4())

class Genre(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=uuid.uuid4)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)

    @staticmethod
    def generate_id():
        return str(uuid.uuid4())

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    publication_date = db.Column(db.String(20))
    isbn = db.Column(db.String(20))
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'))
    genre_id = db.Column(db.Integer, db.ForeignKey('genre.id'))
    cover_image = db.Column(db.String(255))

    author = db.relationship('Author', backref='books')
    genre = db.relationship('Genre', backref='books')

    @staticmethod
    def generate_id():
        return str(uuid.uuid4())
