import csv
import MySQLdb

mydb = MySQLdb.connect(host='localhost',
                       user='testuser',
                       passwd='admin',
                       db='students')
cursor = mydb.cursor()
file=open('C:/Users/ayesh/OneDrive/Desktop/studentmarks.csv')
csv_data = csv.reader(file)
for row in csv_data:
    print(row)
    cursor.execute('INSERT INTO studentsmarks(names, \
          classes, mark )' \
                   'VALUES("%s", "%s", "%s")',
                   row)
#close the connection to the database.
cursor.close()
mydb.commit()
print("Done")
