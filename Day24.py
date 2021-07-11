#1. Create a JSON of all object types and import the JSON into a SQL Database
#Note: The JSON file should have values of all Datatypes

import json
json_data=[
    {'name':"Puneet Singh",'age':20,'Permanent_staff':True,'salary':690.00,'dept_desgn':'Front End Developer'},
     {'name':"Ashveen",'age':15,'Permanent_staff':False,'salary':550.00,'dept_desgn':"Backend Developer"},
     {'name':"Manpreet",'age':14,'Permanent_staff':True,'salary':800.00,'dept_desgn':'Full Stack'},
     {'name':"Simran",'age':23,'Permanent_staff':False,'salary':400.00,'dept_desgn':'Cloud Engineer'},
     {'name':"Anchal",'age':21,'Permanent_staff':True,'salary':520.00,'dept_desgn':'Secretary'}
    
]
res =json.dumps(json_data)
import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1609"
)

print(mydb)
dbse = mydb.cursor()

dbse.execute("CREATE DATABASE JSONRECORDS")
dbse = mydb.cursor()

dbse.execute("SHOW DATABASES")

for entry in dbse:
  print(entry)

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1609",
    database="jsonrecords"
)
dbse = mydb.cursor()

dbse.execute("CREATE TABLE employee (name VARCHAR(255),age INT, permanent_staff VARCHAR(255), salary DOUBLE, dept_and_designation VARCHAR(255))")
dbse = mydb.cursor()

dbse.execute("SHOW TABLES")

for value in dbse:
  print(value)
dbse = mydb.cursor()

dbse.execute("SHOW COLUMNS FROM employee")

for value in dbse:
  print(value)

dbse = mydb.cursor()
sql = "INSERT INTO employee (name ,age, permanent_staff,salary,dept_designation) VALUES (%(name)s,%(age)s,%(permanent_staff)s,%(salary)s,%(dept_designation)s)"
for i in res:
    dbse.execute(sql,i)
    
mydb.commit()
dbse.close()
mydb.close()