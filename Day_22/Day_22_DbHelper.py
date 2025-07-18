# Database Helper class -- THIS IS A GENERAL DATABASE PROGRAM : CAN BE USED EVERYWHERE JUST BY CHANGING DB NAME

# WRITE - INSERT / UPDATE / DELETE  (ALL 3 IT CAN DO)

# TO CREATE MYSQL ON ONLINE SERVER, USING AWS --- BUT ITS PAID AFTER 1 YEAR FREE 

import mysql.connector as db          # db can be named kuchbhi

class DBHelper:

    def __init__(self):

        # 1. Create Connection
        # if we are using database through anyother location, then we get URL, password, host, --- in place of host , add URL, (cloud database configured )
        self.connection  = db.connect(
            user='root',
            password='Samiya@2025',
            host='127.0.0.1',             
            # port = '3306', sometimes we need to pass port , default port is 3306
            database='mydatabase'
)
        print('DB HELPER CLASS, CONNECTION CREATED .........') 


        # 2. Create Cursor from Connection
        self.cursor = self.connection.cursor()
        print('[DB Helper] Cursor Created...')

        # 3. Prepare SQL i.e. take sql query as input in the function
        # 4. Execute the SQL Query
        # Insert/Update/Delete Query

        def write(self, sql_query):
            self.cursor.execuet(sql_query)
            print('[DB Helper] SQL Query Executed...')

        # Select Query
        def read(self, sql_query):
            self.cursor.execute(sql_query)
            rows = self.cursor.fetchall()
            print('[DB Helper] SQL Query Executed. Rows Fetched: ', len(rows))
            return rows
        
        def close(self):
            self.connection.close()
            print('[DB Helper] DB Connection Closed...')

