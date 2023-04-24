import os.path

def read_book_data():
    books = []
    if not os.path.exists('bookdata.txt'):
        print('Book data file does not exist. Creating empty file...')
        with open('bookdata.txt', 'w') as file:
            pass
    else:
        with open('bookdata.txt', 'r') as file:
            for line in file:
                book = eval(line.strip())
                books.append(book)
    return books

def write_book_data(books):
    with open('bookdata.txt', 'w') as file:
        for book in books:
            file.write(str(book) + '\n')

def enter_book_details():
    books = []
    while len(books) < 3:
        print(f'Enter details for book {len(books) + 1}:')
        title = input('Title: ')
        author = input('Author: ')
        book_type = input('Type: ')
        publication = input('Publication: ')
        price = float(input('Price: '))
        book = {'Title': title, 'Author': author, 'Type': book_type, 'Publication': publication, 'Price': price}
        books.append(book)
    return books

def display_book_data():
    books = read_book_data()
    if len(books) == 0:
        print('No books to display.')
    else:
        print('Books:')
        for book in books:
            print(f'{book["Title"]} by {book["Author"]} ({book["Type"]}) - {book["Publication"]} - ₹{book["Price"]}')

books = read_book_data()
if len(books) == 0:
    books = enter_book_details()
    write_book_data(books)

display_book_data()
