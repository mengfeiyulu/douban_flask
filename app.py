from flask import Flask,render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')
@app.route('/index')
def index1():
    return render_template('index.html')

@app.route('/movie')
def moive():
    return render_template('movie.html')

@app.route('/score')
def score():
    return render_template('score.html')

@app.route('/word')
def word():
    return render_template('word.html')

@app.route('/team')
def team():
    return render_template('team.html')


if __name__ == '__main__':
    app.run()
