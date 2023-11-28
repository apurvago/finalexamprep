from flask import Flask,redirect,url_for,request,render_template, jsonify
app=Flask(__name__)

@app.route('/Ag')
def func1():
    #return jsonify()
    return render_template('redirect.html')

@app.route('/redirect_check', methods = ["POST", "GET"] )  
def validate():  
    if request.method == 'POST' and request.form['username'] == 'Apurva' and request.form['password'] == '1234': 
       return jsonify ({"username": request.form.get("username"), "password": request.form.get("password")}, "Login successful")  
    else:
       return redirect(url_for("invalid"))  

@app.route('/success')
def success():
     return "Logged in Successfully!"

@app.route('/invalid')
def invalid():
     return "Invalid credentials - login failed!"

if __name__=='__main__':
     app.run(debug=True)
