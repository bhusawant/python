# from flask import Flask, render_template, redirect, jsonify

# app = Flask(__name__)

# # Define a list of books
# books = [
#     {
#         "number": 1,
#         "title": "The Catcher in the Rye",
#         "author": "J.D. Salinger",
#         "publication": "Little, Brown and Company",
#         "ISBN": "9780316769488"
#     },
#     {
#         "number": 2,
#         "title": "To Kill a Mockingbird",
#         "author": "Harper Lee",
#         "publication": "J. B. Lippincott & Co.",
#         "ISBN": "9780446310789"
#     },
#     {
#         "number": 3,
#         "title": "1984",
#         "author": "George Orwell",
#         "publication": "Secker & Warburg",
#         "ISBN": "9780451524935"
#     }
# ]

# @app.route('/books')
# def get_books():
#     return render_template('books.html', books=books)

# @app.route('/books/<ISBN>')
# def get_book(ISBN):
#     for book in books:
#         if book['ISBN'] == ISBN:
#             return jsonify(book)
#     return redirect('/books')

# if __name__ == '__main__':
#     app.run(debug=True)








from flask import Flask, render_template, redirect, jsonify
import os

app = Flask(__name__, template_folder=os.path.abspath('templates'))


books = [
    {
        "number": 1,
        "title": "The Alchemist",
        "author": "Paulo Coelho",
        "publication": "HarperOne",
        "isbn": "978-0061122415"
    },
    {
        "number": 2,
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "publication": "HarperCollins",
        "isbn": "978-0446310789"
    },
    {
        "number": 3,
        "title": "1984",
        "author": "George Orwell",
        "publication": "Signet Classics",
        "isbn": "978-0451524935"
    }
]


@app.route('/books')
def all_books():
    return render_template('books.html', books=books)  


@app.route('/books/<isbn>')
def book_details(isbn):
    for book in books:
        if book['isbn'] == isbn:
            return jsonify(book)
    return 'Book not found'



if __name__ == '__main__':
    app.run(debug=True)
