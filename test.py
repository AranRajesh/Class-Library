from datetime import datetime

currentDate = datetime.today().strftime('%Y-%m-%d')
studentId=29387762
BookId=9780060589462

with open ('test.txt', "a") as checkoutFile:
    checkoutFile.write(str(studentId) + "," + str(BookId) + "," + currentDate+"\n")
