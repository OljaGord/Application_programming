from datetime import datetime

from flask import Flask

app = Flask(__name__)

@app.route('/hello-world/<username>')
def hello_world(username):
    weekdays = ('понедельника', 'вторника', 'среды', 'четверга', 'пятницы', 'субботы', 'воскресенья')
    weekday = datetime.today().weekday()
    if weekday == 2 or weekday == 4 or weekday == 5:
        ending = 'й'
    else:
        ending = 'го'
    return f'Привет {username}!Хороше{ending} {weekdays[weekday]}!'

if __name__ == '__main__':
    app.run(debug=True)