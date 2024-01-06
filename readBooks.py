import csv

books = {}
with open ('Class Library/books.txt') as csvFile:
    reader = csv.reader(csvFile)
    next(reader,None) # Skip header
    books={int(rows[5]):{"Title":rows[1],"Author":rows[2], "Num Pages":rows[7], "Language":rows[6]} for rows in reader}

bookID = int(input("ISBN number:"))
book = books[bookID]
print (f"Title: {book['Title']}, Author: {book['Author']}, Num Of Pages: {book['Num Pages']}")