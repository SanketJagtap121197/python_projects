
import sqlite3
# for sql querries and connectivity to python

connection = sqlite3.connect("sqlite.db")  
# This will create a connection with database and and also if the database is not present it will create it automatically

# Now we can use some sql querries

connection.execute
('''
CREATE TABLE student
(
student_id INT AUTO_INCREMENT PRIMARY KEY,
student_name VARCHAR(50),
student_class VARCHAR(10),
student_email VARCHAR(30),  
)
''')
# we used tripple ''' ''' single quote so that the output will be printed as we can see here not like normal print by '' or ""

connection.close()