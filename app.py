from MySQLdb import MySQLError
from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
# import pylance
app = Flask(__name__)

app.secret_key = 'your secret key'
 
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'A#'  ###
app.config['MYSQL_DB'] = 'userlogin'

@app.route("/")
@app.route("/login")
@app.route('/home', methods =['GET', 'POST'])
def home():
    msg = ''
    if request.method == 'POST' and 'atmpin' in request.form:
        atmpin = request.form['atmpin']
        cursor = MySQLError.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE atmpin = % d', (atmpin ))
        account = cursor.fetchone()
        if account:
            session['loggedin'] = True
            session['atmpin'] = account['atmpin']
            msg = 'Logged in successfully !'
            return render_template('bank_or_vote.html',msg=msg)
        else:
            msg = 'Incorrect pin'
    return render_template('pin_entry.html',msg=msg)
   
@app.route("/vote")
def vote():
    return render_template('bank_or_vote.html')
 
if __name__=="__main__":
    app.run(debug=True)

#python app.py
