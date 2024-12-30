import sqlite3

conn = sqlite3.connect('test.db')

c = conn.cursor()

#c.execute("""CREATE TABLE customers (
  #        first_name text,
   #       last_nane text, 
   #       email text
   #       )""")

#many_customer = [('Wes', 'Brown', 'email123'),
  #               ('Stepth', 'Kuewa', 'few123'),
  #               ('Giorgis', 'Vlakas', 'meptyxio'),
   #              ]

#c.executemany("INSERT INTO customers VALUES (?,?,?)", many_customer)

c.execute("SELECT * FROM customers")

items = c.fetchall()
  
for item in items:
    print(item[0])

conn.commit()

conn.close()