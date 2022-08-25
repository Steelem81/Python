from flask import Flask, render_template, session, redirect

app = Flask(__name__)
app.secret_key = 'dundundun'

@app.route('/', methods=['GET', 'POST'])
def index():
    session['visits'] = 0
    return render_template('index.html')

@app.route('/count')
def count():
    return render_template('index.html')

@app.route('/count', methods=['POST'])
def visits():
    session['visits'] += 1
    print(session['visits'])
    return redirect('/count')

@app.route('/destroy_session', methods=['POST'])
def destroy_session():
    if 'visits' in session:
        session.pop('visits')
    else:
        print('key does not exist')
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)