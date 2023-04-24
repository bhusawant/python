import mysql.connector

# Establishing connection to the database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="Bookdb"
)

# Creating a cursor object to execute SQL queries
mycursor = mydb.cursor()

# Creating the BooksData table
mycursor.execute("CREATE TABLE BooksData (ISBN VARCHAR(255) NOT NULL PRIMARY KEY, Title VARCHAR(255) NOT NULL, Author VARCHAR(255) NOT NULL, Publication VARCHAR(255) NOT NULL, Year_of_publication INT NOT NULL, Price FLOAT NOT NULL)")

# Inserting data into the table
sql = "INSERT INTO BooksData (ISBN, Title, Author, Publication, Year_of_publication, Price) VALUES (%s, %s, %s, %s, %s, %s)"
values = [
    ('1234567890', 'The Alchemist', 'Paulo Coelho', 'HarperCollins', 1988, 10.99),
    ('0987654321', 'The Catcher in the Rye', 'J.D. Salinger', 'Little, Brown and Company', 1951, 8.99),
    ('1357908642', 'To Kill a Mockingbird', 'Harper Lee', 'J.B. Lippincott & Co.', 1960, 12.99),
    ('2468013579', 'Pride and Prejudice', 'Jane Austen', 'T. Egerton', 1813, 6.99),
    ('9753108642', 'Cryptography', 'William Stallings', 'TMH', 2002, 20.99),
    ('5647382910', 'Data Communications and Networking', 'Forouzan', 'TMH', 2001, 15.99),
    ('2468246802', 'The Lord of the Rings', 'J.R.R. Tolkien', 'Allen & Unwin', 1954, 18.99),
    ('1357924680', '1984', 'George Orwell', 'Secker & Warburg', 1949, 9.99),
    ('0864209635', 'One Hundred Years of Solitude', 'Gabriel Garcia Marquez', 'Harper & Row', 1967, 12.99),
    ('3579246801', 'The Da Vinci Code', 'Dan Brown', 'Doubleday', 2003, 14.99)
]
mycursor.executemany(sql, values)

# Committing changes to the database
mydb.commit()

# Displaying all books published by "TMH" publication
mycursor.execute("SELECT * FROM BooksData WHERE Publication = 'TMH'")
for book in mycursor:
    print(book)

# Displaying all books published between 2001-2010
mycursor.execute("SELECT * FROM BooksData WHERE Year_of_publication BETWEEN 2001 AND 2010")
for book in mycursor:
    print(book)

# Updating the price of the book titled "Cryptography" to 600
mycursor.execute("UPDATE BooksData SET Price = 600 WHERE Title = 'Cryptography'")
mydb.commit()

# Deleting the books published before 1980
mycursor.execute("DELETE FROM BooksData WHERE Year_of_publication < 1980")
mydb.commit()

# Closing the database connection
mydb.close()
