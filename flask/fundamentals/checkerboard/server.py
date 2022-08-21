from flask import Flask, render_template

app = Flask(__name__)

#Is there a cleaner way to do this:
@app.route('/', defaults={'x': 8, 'y':8, 'color1': 'purple', 'color2': 'lightblue'})
@app.route('/<int:x>', defaults={'y': 8,'color1': 'purple', 'color2': 'lightblue'})
@app.route('/<int:x>/<int:y>', defaults={'color1': 'purple', 'color2': 'lightblue'})
@app.route('/<int:x>/<int:y>/<color1>', defaults={'color2': 'lightblue'})
@app.route('/<int:x>/<int:y>/<color1>/<color2>')
def index(x,y, color1, color2):
    return render_template('index.html', x=x, y=y, color1=color1, color2=color2)

if __name__ == '__main__':
    app.run(debug=True)