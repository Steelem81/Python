from flask import Flask, render_template, request, redirect, session
import datetime as dt

app = Flask(__name__) 
app.secret_key = 'dundundun'

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    purchased = {'strawberry': int(request.form['strawberry']), 'raspberry':int(request.form['raspberry']), 'apple': int(request.form['apple'])}
    session['first_name'] = request.form['first_name']
    session['last_name'] = request.form['last_name']
    session['student_id'] = request.form['student_id']
    session['total'] = sum(purchased.values())
    session['submitted_at'] = dt.datetime.now()
    print(f"Charging {session['first_name']} {session['last_name']} for {session['total']} fruits")
    return render_template("checkout.html", purchased = purchased)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    