import mysql.connector
mydb=mysql.connector.connect(host="localhost", user="root", password="", database="Internship")
mycursor=mydb.cursor()
mycursor.execute("""SELECT * FROM employee
WHERE Salary >
ALL(SELECT avg(Salary)FROM employee);""")
ans1=mycursor.fetchall()
print("\nList of HODs whose salary is greater than average salary of HODs")
for j in ans1:
    print(j)