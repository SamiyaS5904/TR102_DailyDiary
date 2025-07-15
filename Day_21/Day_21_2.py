# WE NEED TO MAKE CONNECTION BETWEEN PYTHON, SQL

# 1. WE NEED TO KNOW MYSQL USERNAME, PASSWORD
# 2. USE LIBRARY API's 
#     Cursor
# 
import mysql.connector as db

# 1. Create Connection
connection  = db.connect(
    user='root',
    password='Samiya@2025',
    host='127.0.0.1',
    database='gw2025'
)

print('Conenction Created :)')
print(connection, type(connection), id(connection))

# 2. Obtain Cursor from Conenction
cursor = connection.cursor()

# 3. Execute SQL Statement
# 3.1 Command to be execute from Python Program
# sql = "insert into Visitor values(null, 'Harry', '+91 99999 22222', 'Redwood Shores', 'Fionna', 'Web Dev', '2025-07-14')"
# sql = "update Visitor set name='John Watson', address='Country Homes' where serial_no = 2;"
# sql = "delete from Visitor where serial_no = 3"
 

# This query will fetch all rows from the Visitor table. 
sql = "select * from Visitor"

# 3.2 Execute the SQL Statement
# cursor.execute(sql)

# 3.3 Commit the Transaction
# connection.commit()

cursor.execute(sql)
rows = cursor.fetchall()
for row in rows:
    print(row)

print('SQL Query Executed :)')

# 4. Close connection -> Released the memory resources
connection.close()
print('Connection Closed :)')

