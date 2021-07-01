#1. Create a DB with doctor and doctor ID & patients visited
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1609"
)

print(mydb)

dbse = mydb.cursor()


dbse.execute("CREATE DATABASE Doctors")
dbse = mydb.cursor()

dbse.execute("SHOW DATABASES")

for entry in dbse:
  print(entry)

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1609",
    database="Doctors"
)
dbse = mydb.cursor()

dbse.execute("CREATE TABLE Doctors (dr_id VARCHAR(255), patient_visit VARCHAR(255))")
dbse = mydb.cursor()

dbse.execute("SHOW TABLES")

for value in dbse:
  print(value)


dbse = mydb.cursor()

sql = "INSERT INTO Doctors (dr_id , patient_visit) VALUES (%s,%s)"
val = [
    ('Doc1','2'),
    ('Doc2','4'),
    ('Doc3','9'),
    ('Doc4','6'),
    ('Doc5','56'),
    ('Doc6','45'),
    ('Doc7','1'),
    ('Doc8','0'),
    ('Doc9','0'),
    ('Doc10','3'),
    ('Doc11','7'),
    ('Doc12','0'), 
    ('Doc13','8'),
    ('Doc14','0'),
    ('Doc15','0'),
    ('Doc16','0')    
]

dbse.executemany(sql, val)

mydb.commit()

print(dbse.rowcount, " doctors data were inserted.")

#2. Get the doctor(s) who have more than 5 patients visited

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM Doctors where patient_visit >5")

myresult = mycursor.fetchall()
print("Doctors with more than 5 visits")
for i in myresult:
  print(i)

#3. Get the doctors with no patients visit

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM Doctors where patient_visit=0")

myresult = mycursor.fetchall()
print("Doctors with 0 visits")
for i in myresult:
  print(i)
