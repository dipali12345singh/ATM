import sqlite3

conn = sqlite3.connect("atm.db")
cursor = conn.cursor()
cursor.execute('''
       create table if not exists user(
          UserId int primary key,
          Name varchar2(20),
          MobileNumber number,
          City varchar2(20),
          AccountNumber number,
          PIN number
          )
''')
# cursor.execute('''
#           insert into user values(106,'Rajni Singh',7898933223,'Lucknow',98989132232321,4627)
# ''')


cursor.execute('select * from user')
val=cursor.fetchall()
for row in val:
    print(row)
conn.commit()
cursor.close()
conn.close()
