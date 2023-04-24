# Q) Create a dataframe having following columns:
# • ISBN (unique number for each book)
# • Title 
# • Author 
# • Publication
# • Year Published
# • Price
# • Copies sold of first edition
# • Copies sold in second edition
# • Copies sold in third edition
# You can use any of the studied approach to create dataframe. Add 
# minimum 10 records to the dataframe. Perform following 
# operations on dataframe using appropriate functions:
# 1. Display the number of rows and columns in dataframe
# 2. Give the descriptive statistics of the created dataset.
# 3. Display distinct publication names for the dataset.
# 4. Display the book title and author names published by “Metro 
# Publication”
# 5. Rename columns “Copies sold in first edition”, “Copies sold in 
# second edition” and “Copies sold in third edition”to FE, SE and 
# TE respectively
# 6. Add a column “Average sale” to your dataframe derived as 
# (average of FE, SE and TE) * Price.
# 7. Display the details of books grouped by author.
# 8. For each group obtained in above query display maximum 
# value of Average sale.
# 9. Reshape your dataframe such that rows will show ‘Author’, 
# column will show “Publication” and values will be ‘Title’ of 
# book.       





import pandas as pd

data = {
    'ISBN': ['978-0-201-63361-0', '978-0132350884', '978-0321751041', '978-0201616224', '978-0470624547', '978-1593275990', '978-0134671716', '978-0134093413', '978-0321982384', '978-0596007126'],
    'Title': ['Design Patterns: Elements of Reusable Object-Oriented Software', 'Clean Code: A Handbook of Agile Software Craftsmanship', 'The C Programming Language', 'Effective C++: 55 Specific Ways to Improve Your Programs and Designs', 'Code Complete: A Practical Handbook of Software Construction', 'Python Crash Course', 'The Pragmatic Programmer: From Journeyman to Master', 'Cracking the Coding Interview: 189 Programming Questions and Solutions', 'Head First Design Patterns', 'Learning Python'],
    'Author': ['Erich Gamma, Richard Helm, Ralph Johnson, John Vlissides', 'Robert C. Martin', 'Brian W. Kernighan, Dennis M. Ritchie', 'Scott Meyers', 'Steve McConnell', 'Eric Matthes', 'Andrew Hunt, David Thomas', 'Gayle Laakmann McDowell', 'Elisabeth Freeman, Kathy Sierra, Bert Bates', 'Mark Lutz'],
    'Publication': ['Addison-Wesley Professional', 'Prentice Hall', 'Prentice Hall', 'Addison-Wesley Professional', 'Microsoft Press', 'No Starch Press', 'Addison-Wesley Professional', 'CareerCup', "O'Reilly Media", "O'Reilly Media"],
    'Year Published': [1994, 2008, 1988, 1997, 2004, 2015, 1999, 2015, 2004, 2003],
    'Price': [45.55, 35.99, 69.99, 54.99, 49.99, 29.95, 49.99, 39.99, 54.99, 49.99],
    'Copies sold in first edition': [100000, 50000, 80000, 60000, 90000, 70000, 40000, 60000, 70000, 80000],
    'Copies sold in second edition': [80000, 40000, 60000, 40000, 70000, 50000, 30000, 50000, 50000, 60000],
    'Copies sold in third edition': [60000, 30000, 40000, 30000, 50000, 40000, 20000, 40000, 40000, 50000]
}

df = pd.DataFrame(data)


# 1. Display the number of rows and columns in dataframe
print('Rows:', df.shape[0])
print('Columns:', df.shape[1])

# 2. Give the descriptive statistics of the created dataset.
print(df.describe())

# 3. Display distinct publication names for the dataset.
print(df['Publication'].unique())

# 4. Display the book title and author names published by “Metro Publication”
print(df.loc[df['Publication'] == 'Metro Publication', ['Title', 'Author']])


# 5. Rename columns
df = df.rename(columns={'Copies sold in first edition': 'FE', 'Copies sold in second edition': 'SE', 'Copies sold in third edition': 'TE'})

# 6. Add a column “Average sale”
df['Average sale'] = (df['FE'] + df['SE'] + df['TE']) / 3 * df['Price']

# 7. Display details of books grouped by author
grouped_by_author = df.groupby('Author')
print(grouped_by_author.apply(lambda x: x[['Title', 'Publication', 'FE', 'SE', 'TE', 'Price', 'Average sale']]))

# 8. Display maximum value of Average sale for each group
max_average_sale = grouped_by_author['Average sale'].max()
print(max_average_sale)

# 9. Reshape dataframe
reshaped_df = df.pivot(index='Author', columns='Publication', values='Title')
print(reshaped_df)
