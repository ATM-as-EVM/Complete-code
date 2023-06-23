
import sqlite3
import base64
conn=sqlite3.connect("pin.sqlite")

cursor=conn.cursor()

# cursor.execute(""" CREATE TABLE users (
#   card_number text NOT NULL,
#   atm_pin text NOT NULL
# )""")

# cursor.execute(""" INSERT INTO users VALUES('123456789','1234')""")
# cursor.execute(""" INSERT INTO users VALUES('9876543210','1234')""")
# cursor.execute(""" INSERT INTO users VALUES('1112223333','1234')""")
# cursor.execute(""" INSERT INTO users VALUES('9988776655','1234')""")
#------------------------

# cursor.execute(""" CREATE TABLE if not exists aadhaar (
#   aadhaar_number text NOT NULL,
#   name text NOT NULL,
#   addr text not null,
#   dob date not null,
#   gender char(1) not null,
#   mobile_no number not null,
#   image text not null
# )""")
# img='C:\\Users\\ankit\OneDrive\\Pictures\\Camera Roll\\ankitha.jpg'

# # with open('C:\\Users\\ankit\OneDrive\\Pictures\\Camera Roll\\ankitha.jpg', 'rb') as file:
# #         image_data = file.read()
# cursor.execute("INSERT INTO aadhaar VALUES (?, ?, ?, ?, ?, ?, ?)",
#                ('111122223333', 'Ankitha', 'Street1,Village2,Taluk3',
#                 '2002-04-21', 'F', 9876543210, img))
#-----------------------

# Create a table to store votes
# cursor.execute('''CREATE TABLE IF NOT EXISTS votes
#              (constituency TEXT, representative TEXT, count INTEGER)''')
#------------------------

# cursor.execute('''CREATE TABLE IF NOT EXISTS map
#            (aadhaar_number TEXT, card_number TEXT)''')

# cursor.execute(""" INSERT INTO map VALUES('111122223333','123456789')""")
#------------------------
# file = open('C:\\Users\\ankit\OneDrive\\Pictures\\Camera Roll\\ankitha.jpg','rb').read()
# file = base64.b64encode(file)
# # args = ('111122223333', 'Ankitha', 'Street1,Village2,Taluk3','2002-04-21', 'F', 9876543210, file)
# cursor.execute("INSERT INTO aadhaar VALUES (?, ?, ?, ?, ?, ?, ?)",
#                ('111122223333', 'Ankitha', 'Street1,Village2,Taluk3',
#                 '2002-04-21', 'F', 9876543210, file))

# cursor.execute('''CREATE TABLE IF NOT EXISTS voted_aadhaar
#            (aadhaar_number TEXT)''')

# img='C:\\Users\\ankit\\Downloads\\tej.jpg'
# cursor.execute("INSERT INTO aadhaar VALUES (?, ?, ?, ?, ?, ?, ?)",
#                ('222233334444', 'Tej', 'Street2,Village2,Taluk3',
#                 '2002-08-15', 'F', 9876543211, img))

# cursor.execute(""" INSERT INTO map VALUES('222233334444','9876543210')""")

cursor.execute(""" delete from voted_aadhaar""")

conn.commit()
conn.close()


