import sqlite3
import os
try:
    os.remove('databases.db')
    print("Databases removed")
except OSError as error:
    print("Databases does'nt exist....processsing")

conn=sqlite3.connect('databases.db')
c=conn.cursor()

c.execute("""CREATE TABLE user(
                                 name TEXT NOT NULL,
                                 password VARCHAR(128) NOT NULL,
                                 gmail  TEXT NOT NULL,
                                 contact TEXT NOT NULL,
                                 PRIMARY KEY(name,password,gmail,contact))
                                 
         """)
conn.commit()
c.execute("""CREATE TABLE garbage(
                                 name TEXT NOT NULL,
                                 email VARCHAR ,
                                 pincode INTEGER,
                                 contact INTEGER)
                                 
         """)
manyusers = [
                ('ZONE 1','1@gmail.com',452009,9691608494 ),
               ('ZONE 2','2@gmail.com',452010,8889199054 ),
               ('ZONE 3','3@gmail.com',452011,9174330184 ),
               ('ZONE 4','4@gmail.com',452012,9179004559 ),
               ('ZONE 5','5@gmail.com',452013,6261797661 )
            ]
c.executemany("INSERT INTO garbage values (?,?,?,?)", manyusers)
conn.commit()
conn.close()
print("New database databses.db created with one tables: user")
print("No data inserted into the tables")
print("Script ran successfully")