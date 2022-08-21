from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/dojo')
def dojo():
    return 'Dojo!'

@app.route('/say/<name>')
def say_hi(name):
    print(name)
    return f'Hi {name}'

@app.route('/repeat/<int:num>/<word>')
def repeating_words(num, word):
    return f'{word * num}'

if __name__=='__main__':
    app.run(debug=True)