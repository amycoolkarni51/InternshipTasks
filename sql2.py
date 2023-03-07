import mysql.connector
mydb=mysql.connector.connect(host="localhost", user="root", password="", database="Internship")
mycursor=mydb.cursor()

mycursor.execute("create table Employee(Employee_id int(10), Name varchar(100), DoB date, Salary int(10), Department_id int(10));")
sql="insert into Employee(Employee_id, Name, DoB, Salary, Department_id) VALUES(%s,%s,%s,%s,%s)"
val=[(101,'Ashish',12/12/2013,30000,201),
(102,'Shweta',15/11/2015,35000,201),
(103,'Cameron',21/9/2017,30000,201),
(104,'Charlie',20/10/2016,20000,201),
(105,'Shashwat',19/8/2014,55000,201),
(111,'Nichole',9/1/2014,25000,202),
(112,'Manish',25/8/2017,15000,202),
(113,'Cloe',13/2/2017,28000,202),
(114,'Janice',20/3/2016,30000,202),
(115,'Shree',29/8/2012,45000,202),
(121,'KAYLING',1/5/2012,60000,203),
(122,'JONAS',15/2/2015,24000,203),
(123,'SANDRINE',25/5/2014,35000,203),
(124,'Pritam',20/5/2016,30000,203),
(125,'Pawan',16/8/2017,20000,203),
(131,'Avinash',18/9/2016,30000,204),
(132,'ADNRES',14/5/2017,25000,204),
(133,'Ishwari',12/1/2014,40000,204),
(134,'MADDEN',16/2/2013,60000,204),
(135,'Pawan',15/12/2015,35000,204)]

mycursor.executemany(sql,val)
mydb.commit()
