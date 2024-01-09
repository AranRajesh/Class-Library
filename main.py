from tkinter import *
import csv
from datetime import datetime

books = {}
students = {}

# Read the book details into the books dict
with open ('books.txt') as csvfile:
    reader = csv.reader(csvfile)
    next(reader,None) # Skip header
    books = {int(rows[5]):{"Title":rows[1],"Author":rows[2], "Num Pages":rows[7], "Language":rows[6]} for rows in reader}

with open ('students.csv') as csvFile:
    reader = csv.reader(csvFile)
    next(reader,None) # Skip header
    students = {int(rows[0]):(rows[1]) for rows in reader}


def looksupBook():
    bookId = int(bookISBN.get())
    book = books[bookId]
    result = f"Title: {book['Title']}\n"
    result = result + f"Author: {book['Author']}\n"
    result = result + f"Num Of Pages: {book['Num Pages']}"
    bookResult.insert(INSERT,result+'\n')
    studentId = int(studentIdEntry.get())
    student = students[studentId]
    bookResult.insert(INSERT, 'Student: ')
    bookResult.insert(INSERT, student+'\n')

def checkoutBook():
    currentDate = datetime.today().strftime('%Y-%m-%d')
    Checkouttext= bookResult.get("1.0",'end-1c')

    with open ('test.txt', "a") as checkoutFile:
        checkoutFile.write(str(Checkouttext) + "Date: " + currentDate+"\n")
    bookResult.delete('1.0', END)
    Checkouttext = None

window = Tk()
window.title ("Library - 4th/5th Quest (Ms.Gale's class)!")
window.geometry('510x280')
lbl = Label (window, text = "Enter ISBN:", width=20, anchor='e')
lbl.grid()

bookISBN = Entry(window, width=20)
bookISBN.grid(column=1,row=0)
stuLabel = Label(window, text= "Enter Student ID: ", width=20, anchor='e')
stuLabel.grid(column=0, row=1, sticky='E')
studentIdEntry = Entry(window, width=20)
studentIdEntry.grid(column=1, row= 1)
studentButton = Button(window, text= 'Search', command=looksupBook,  width=8)
studentButton.grid(column=2, row=1)

checkoutButton = Button(window, text= 'Checkout', command=checkoutBook,width= 10).grid(column=1, row=5)

bookResult = Text(window, width=60, height=10)
bookResult.grid(column=0, columnspan=3, row=2, pady=25)


window.mainloop()
