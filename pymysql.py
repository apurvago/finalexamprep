import mysql.connector
# Establish a connection to MySQL
conn = mysql.connector.connect(host="localhost", user="root", password="apurva1234")

# Creating a cursor
cursor = conn.cursor()

# Creating the 'Employee' database
cursor.execute("CREATE DATABASE IF NOT EXISTS Employee")
# Using the 'Employee' database
cursor.execute("USE Employee")

# Creating the 'EmpInfo' table 
cursor.execute("CREATE TABLE  EmpInfo (Emp_NO int NOT NULL, Emp_Name varchar(50), Salary int, Address varchar(100), Role_Type varchar(50))")

# Inserting the data into the table
cursor.execute("INSERT INTO EmpInfo VALUES (01, 'Patrick Jane', 350000, 'California', 'Psychic Counselor')")
cursor.execute("INSERT INTO EmpInfo VALUES (02, 'Jack Ryan', 255000, 'Langley', 'Data Analyst')")
cursor.execute("INSERT INTO EmpInfo VALUES (03, 'Teresa Lisbon', 280000, 'Los Anglelas', 'Special Agent-CBI')")
cursor.execute("INSERT INTO EmpInfo VALUES (04, 'Mathew Perry', 300000, 'New York', 'Actor-Writer')")
# Commiting the changes 
conn.commit()

# displaying data
cursor.execute("SELECT * FROM EmpInfo")
Emp = cursor.fetchall()
print("Initial data fetching:")
for i in Emp:
    print(i)
print("-------------------------------------------------")

# Altering the table to add columns 'Email' and 'Age'
cursor.execute("ALTER TABLE EmpInfo ADD COLUMN Email varchar(255)")
cursor.execute("ALTER TABLE EmpInfo ADD COLUMN Age int")

# Inserting 'Email' and 'Age' data
cursor.execute("UPDATE EmpInfo SET Email = 'pjane@gmail.com', Age = 40 WHERE Emp_NO = 01")
cursor.execute("UPDATE EmpInfo SET Email = 'jackr@gmail.com', Age = 35 WHERE Emp_NO = 02")
cursor.execute("UPDATE EmpInfo SET Email = 'lisbon@gmail.com', Age = 38 WHERE Emp_NO = 03")
cursor.execute("UPDATE EmpInfo SET Email = 'chandlerbing@gmail.com', Age = 45 WHERE Emp_NO = 04")
# Commiting the changes for adding 'Email' and 'Age'
conn.commit()

# Displaying data after adding 'Email' and 'Age'
cursor.execute("SELECT * FROM EmpInfo")
Emp = cursor.fetchall()
print("Data after altering the table:")
for i in Emp:
    print(i)
print("-------------------------------------------------")

# Deleteing the 'Age' column
cursor.execute("ALTER TABLE EmpInfo DROP COLUMN Age")

# Commiting the changes for deleting 'Age'
conn.commit()

#data display after deleting a column
cursor.execute("SELECT * FROM EmpInfo")
Emp = cursor.fetchall()
print("Data after deleting:")
for i in Emp:
    print(i)
print("-------------------------------------------------")
# Closing the cursor and the connection
cursor.close()
conn.close()
