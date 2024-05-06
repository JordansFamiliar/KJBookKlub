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

## Setup
Ensure that the following prerequisites are installed on your system:
- **Python (version 3.7 or higher)**
- **pip (Python package manager)**
- **SQLite (lightweight relational database)**

### Installation Steps
**1. Clone this repository:**
git clone https://github.com/JordansFamiliar/KJBookKlub.git
cd KJBookKlub

**2. Create a virtual environment:**
python -m venv venv

**3. Activate virtual environment:**
(On Windows) venv\Scripts\activate
(On macOS and Linux) source venv/bin/activate

**4. Install dependencies:**
pip install -r requirements.txt

**5. Initialise database:**
flask db init
flask db migrate -m "Initial migration"
flask db upgrade

**6. Run the application**
flask run

**7. Access API**
Api can be accessed via your web browser or by using curl or fetch.


## Authors
- Jordan Williams: [jordanlw1997@gmail.com](mailto:jordanlw1997@gmail.com)
- Keitumetse Molefe: [kr.molefe98@gmail.com](mailto:kr.molefe98@gmail.com)
