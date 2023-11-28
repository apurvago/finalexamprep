from flask import Flask, render_template, request, redirect, url_for     #import the Flask class from the flask module
from flask_mysqldb import MySQL        

app = Flask(__name__)    #creates a Flask application object — app — in the current Python module #pass the __name__ variable, Flask route returns the value of __name__ so we can verify its value when we run the Flask application

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'apurva1234'
app.config['MYSQL_DB'] = 'flaskdb1'

mysql = MySQL(app)

@app.route('/')  #mapping URL to specific func
def func1():
    return render_template('loginf.html')

@app.route('/loginf', methods=['POST', 'GET'])
def login():
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        cursor = mysql.connection.cursor()                          #Cursor thus provides a means for Flask to interact with the database tables. It can scan the database for data, execute SQL queries, and delete table records.
        cursor.execute("SELECT * FROM flasktable WHERE user_id=%s AND password_user=%s", (username, password))
        account = cursor.fetchone()
        if account:
            return render_template('aboutme.html')
        else:
            return redirect(url_for("fail"))

@app.route('/fail')
def fail():
    return "Invalid Credentials- Please enter correct username and password!"
if __name__ == '__main__':
    app.run(debug=True)
