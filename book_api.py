# Import Flask
from flask import Flask, jsonify, request

# Create the Flask app
app = Flask(__name__)

# Create a list to store book data
books = {
    "book_name": "Python Basics",
    "author": "John Doe",
    "publisher": "Tech Press"
}


# Get all books
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

# Get a single book by its ID
@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    # Find the book with the matching ID
    for book in books:
        if book['id'] == book_id:
            return jsonify(book)
    return jsonify({'message': 'Book not found'}), 404

# Add a new book
@app.route('/books', methods=['POST'])
def create_book():
    # Get data from the user
    data = request.get_json()
    # Create a new book with an ID
    new_book = {
        'id': len(books) + 1,
        'book_name': data['book_name'],
        'author': data['author'],
        'publisher': data['publisher']
    }
    books.append(new_book)  # Add the book to the list
    return jsonify(new_book), 201

# Update an existing book
@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    # Find the book to update
    for book in books:
        if book['id'] == book_id:
            data = request.get_json()
            book['book_name'] = data.get('book_name', book['book_name'])
            book['author'] = data.get('author', book['author'])
            book['publisher'] = data.get('publisher', book['publisher'])
            return jsonify(book)
    return jsonify({'message': 'Book not found'}), 404

# Delete a book
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    global books
    # Keep only books that don't match the ID
    books = [book for book in books if book['id'] != book_id]
    return jsonify({'message': 'Book deleted'})

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
