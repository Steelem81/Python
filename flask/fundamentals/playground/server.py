from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def chekcing():
    return render_template('index.html')

@app.route('/play/<int:times>')
@app.route('/play')
def play(times=3):
    return render_template('play.html', times=times)

@app.route('/play/<int:times>/<color>')
def playing_with_color(times, color):
    return render_template('play.html', times=times, color=color)

if __name__ == '__main__':
    app.run(debug=True)