from flask import Flask
app = Flask(__name__)


@app.route('/counter')
def counter():
    global count
    count = count + 1
    return f'Страничка открывалась <i> <b> {count} </b> </i> раз время работы сервера.'

if __name__ == '__main__':
    app.run(debug=True, port=4000)  # поменяли порт на 4000