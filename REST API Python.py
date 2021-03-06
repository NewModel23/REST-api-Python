
# Crear REST api utilizando flask

from flask import Flask, jsonify, request
app = Flask(__name__)

books = [
    {
         'name': 'Green Eggs and Ham',
         'price': 7.99,
         'isbn': 9780394800165
    },
    {
        'name': 'The Cat In The Hat',
        'price': 6.99,
        'isbn': 9782371000193
    }
    ]


@app.route('/') 
def hello():
    return 'Hello rulas1'


# GET /Store
@app.route('/books')
def get_books():
    return jsonify({'books': books})
    



@app.route('/books/<int:isbn>')
def get_book_by_isbn(isbn):
    return_value = {}
    for book in books:
        if book["isbn"] == isbn:
            return_value = {
                    'name': book["name"],
                    'price': book["price"]
                    }
            return jsonify(return_value)


app.run(port=5000)

