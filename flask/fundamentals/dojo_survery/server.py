from flask import Flask, render_template, redirect, session, request

app = Flask(__name__)
app.secret_key = "pepperonipizza"

@app.route('/')
def index():
    session.clear()
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    session['name'] = request.form['name']
    session['dojo_loc'] = request.form['dojo_loc']
    session['fav_lang'] = request.form['fav_lang']
    session['comments'] = request.form['comments']
    return redirect('/result')

@app.route('/result')
def result():
    return render_template('result.html')

if __name__ == '__main__':
    app.run(debug=True)