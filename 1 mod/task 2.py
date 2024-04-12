from flask import Flask
from datetime import datetime, timedelta
app = Flask(__name__)

@app.route('/get_time/now')
def get_time_now():
    current_time = 'Точное время: '
    get_time_now = datetime.now()
    return current_time + str(get_time_now)

if __name__ == '__main__':
    app.run(debug=True, port=4000)  # поменяли порт на 4000
