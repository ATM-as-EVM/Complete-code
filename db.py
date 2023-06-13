import sqlite3

conn=sqlite3.connect("pin.sqlite")

cursor=conn.cursor()

# cursor.execute(""" CREATE TABLE users (
#   card_number text NOT NULL,
#   atm_pin text NOT NULL
# )""")

cursor.execute(""" INSERT INTO users VALUES('123456789','1234')""")
conn.commit()
conn.close()

