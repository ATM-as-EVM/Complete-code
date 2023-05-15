from MySQLdb import MySQLError
from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
import sqlite3

app = Flask(__name__)

app.secret_key = 'your secret key'

def db_connection():
    conn=None
    try:
        conn=sqlite3.connect('pin.sqlite')
    except sqlite3.Error as e:
        print(e)
    return conn

@app.route("/")
def home():
    return render_template('pin_entry.html')

@app.route('/login', methods =['POST','GET'])
def login():
    conn=db_connection()
    card_number = request.form['card_number']
    atm_pin = request.form['atm_pin']
    
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE card_number = ? AND atm_pin = ?', (card_number, atm_pin))
    conn.commit()

    if cursor.fetchone() is not None:
        return redirect(url_for('bank_or_vote'))
    else:
        error = 'Invalid card number or ATM pin. Please try again.'
        return render_template('pin_entry.html', error=error)

@app.route("/bank_or_vote")
def bank_or_vote():
    return render_template('bank_or_vote.html')

@app.route("/vote")
def vote():
    return render_template('vote.html')

if __name__=="__main__":
    app.run(debug=True)

#python app.py
