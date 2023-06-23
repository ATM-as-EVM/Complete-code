from MySQLdb import MySQLError
from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
from flask_mail import Mail
import sqlite3
import os
import face_auth

app = Flask(__name__)
card_number=''

# app.config['MAIL_SERVER']='smtp.gmail.com'
# app.config['MAIL_PORT'] = 465
# app.config['MAIL_USERNAME'] = 'tejaswinikshatriyas@gmail.com.com'
# app.config['MAIL_PASSWORD'] = 'password'
# app.config['MAIL_USE_TLS'] = False
# app.config['MAIL_USE_SSL'] = True
# mail = Mail(app)

app.secret_key = 'your secret key'

def db_connection():
    conn=None
    try:
        conn=sqlite3.connect('pin.sqlite')
    except sqlite3.Error as e:
        print(e)
    return conn
i=0
@app.route("/")
@app.route("/home")
def home():
    global i
    i=0
    return render_template('entry_pin.html')

@app.route('/login', methods =['POST','GET'])
def login():
    conn=db_connection()
    global card_number
    global i
    card_number = request.form['card_number']
    atm_pin = request.form['atm_pin']
    
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE card_number = ? AND atm_pin = ?', (card_number, atm_pin))
    # conn.commit()
    i+=1
    if cursor.fetchone() is not None:
        return redirect(url_for('bank_or_vote'))
    else:
        if i<3:
            error = 'Invalid card number or ATM pin. Please try again.'
            return render_template('entry_pin.html', error=error)
        else:
            error = 'Maximum limit exceeded'
            return render_template('entry_pin.html', error=error)

# @app.route("/invalid")
# def invalid():
#   msg = Message('Hello from the other side!', sender =   'tejaswinikshatriyas@gmail.com', recipients = ['to_receiver@gmail.com'])
#   msg.body = "hey, sending out email from flask!!!"
#   mail.send(msg)
#   return msg

@app.route("/bank_or_vote")
def bank_or_vote():
    return render_template('voting_interface.html')

c=0
@app.route("/validate")
def validate():
    global c
    c=0
    # global card_number
    # conn=db_connection()
    # cursor = conn.cursor()
    # cursor.execute('SELECT aadhaar_number FROM map WHERE card_number = ?', (card_number,))
    # a_temp = cursor.fetchone()

    # cursor.execute('SELECT * FROM voted_aadhaar')
    # all_aadhaar = cursor.fetchall()
    # print("Hellooo",a_temp)
    # print("Hellooo",all_aadhaar)
    # if a_temp in all_aadhaar:
    #     error = 'You have already voted'
    #     return render_template('entry_pin.html', error=error)
    # else:
    #     cursor.execute(" insert INTO voted_aadhaar VALUES(?)",(a_temp[0],))
    #     conn.commit()
    #     conn.close()
    # print("Hellooo",all_aadhaar)
    # os.system('python face_det/face_detect.py')
    # os.system('python face_det/face_auth.py {card_number}')
    
    face_auth.call_face_detect()
    # print(card_number)
    print("HIIIIII",card_number)
    res,c = face_auth.call_face_match(c,card_number)

    if res:
        return redirect(url_for('success'))
    else:
        if c<2:
            face_auth.call_face_detect()
            res,c = face_auth.call_face_match(c,card_number)
            if res and c<2:
                return redirect(url_for('success'))
            # else:
            #     face_auth.call_face_detect()
            #     res,c = face_auth.call_face_match(c,card_number)
            #     if res:
            #         return redirect(url_for('vote1'))
        return redirect(url_for('failed'))
    # # i+=1
    # 
    # result = os.system("python face_det/face_match.py")
    # if result == True:
    #     return redirect(url_for('home'))
    # else:
    #     # if i<=3:
    #     return redirect(url_for('validate'))
    #     # else:
    #     #     return redirect(url_for('login'))

@app.route("/vote")
def vote1():
    global card_number
    conn=db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT aadhaar_number FROM map WHERE card_number = ?', (card_number,))
    a_temp = cursor.fetchone()

    cursor.execute('SELECT * FROM voted_aadhaar')
    all_aadhaar = cursor.fetchall()
    print("Hellooo",a_temp)
    print("Hellooo",all_aadhaar)
    if a_temp in all_aadhaar:
        error = 'You have already voted'
        return render_template('entry_pin.html', error=error)
    else:
        cursor.execute(" insert INTO voted_aadhaar VALUES(?)",(a_temp[0],))
        conn.commit()
        conn.close()
    print("Hellooo",all_aadhaar)
    
    return render_template('voting_poll.html')

@app.route('/record_vote', methods=['POST'])
def record_vote():
    vote_data = request.json
    constituency = vote_data['constituency']
    representativeName = vote_data['representativeName']

    # Create a connection to the SQLite database
    conn = db_connection()
    c = conn.cursor()
    c.execute("SELECT count FROM votes WHERE constituency=? AND representative=?", (constituency, representativeName))
    result = c.fetchone()
    # Insert the vote into the database
    # cursor = conn.cursor()
    if result:
        # Vote already exists, increment the count
        count = result[0] + 1
        c.execute("UPDATE votes SET count=? WHERE constituency=? AND representative=?", (count, constituency, representativeName))
    else:
        # Vote does not exist, insert a new row
        c.execute("INSERT INTO votes VALUES (?, ?, 1)", (constituency, representativeName))
    # cursor.execute("INSERT INTO votes (constituency, representative) VALUES (?, ?)",
    #                (constituency, representativeName))
    conn.commit()

    # Close the connection
    conn.close()

    return redirect(url_for('done'))

@app.route('/vote/<constituency>/<representative>')
def vote(constituency, representative):
    conn=db_connection()
    c = conn.cursor()
    # Check if the vote exists in the database
    print("Hi")
    c.execute("SELECT count FROM votes WHERE constituency=? AND representative=?", (constituency, representative))
    result = c.fetchone()
    print(result)
    if result:
        # Vote already exists, increment the count
        count = result[0] + 1
        c.execute("UPDATE votes SET count=? WHERE constituency=? AND representative=?", (count, constituency, representative))
    else:
        # Vote does not exist, insert a new row
        c.execute("INSERT INTO votes VALUES (?, ?, 1)", (constituency, representative))

    # Commit changes and close the connection
    conn.commit()
    conn.close()

    return "Vote recorded successfully!"

@app.route("/done")
def done():
    return render_template('Voting_done.html')

@app.route("/success")
def success():
    return render_template('auth_success.html')

@app.route("/failed")
def failed():
    return render_template('auth_failed.html')

if __name__=="__main__":
    app.run(debug=True)

#python app.py
