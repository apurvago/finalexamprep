from flask import Flask, render_template, jsonify, request, redirect, url_for
from flask_mysql_connector import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root1234'
app.config['MYSQL_DB'] = 'flaskdb'

mysql = MySQL(app)

@app.route('/')
def func1():
    return render_template('loginf.html')

@app.route('/loginsql', methods=['POST', 'GET'])
def login():
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM flasktable WHERE user_id=%s AND password_user=%s", (username, password))
        account = cursor.fetchone()
        if account:
            return render_template('Aboutme.html')
            return jsonify ({"username": request.form.get("username"), "password": request.form.get("password")}, "Login successful")
        else:
            return redirect(url_for("fail"))

@app.route('/fail')
def fail():
    return "Invalid Credentials- Please enter correct username and password!"
if __name__ == '__main__':
    app.run(debug=True)
