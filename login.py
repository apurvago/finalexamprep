from flask import Flask,render_template,url_for,request

app=Flask(__name__)

@app.route('/Ag')
def func1():
    return render_template('login.html')

if __name__=='__main__':
     app.run(debug=True)
