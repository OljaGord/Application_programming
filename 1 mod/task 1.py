from flask import Flask
app = Flask(__name__)


@app.route('/hello_world')
def hello_world():
    hello_world = 'Привет, мир!'
    return hello_world

if __name__ == '__main__':
    app.run(debug=True, port=4000)  # поменяли порт на 4000
