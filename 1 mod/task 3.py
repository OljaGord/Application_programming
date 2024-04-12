from flask import Flask
from datetime import datetime, timedelta
app = Flask(__name__)

@app.route('/get_time/future')
def get_time_future():
    current_time_after_hour = 'Точное время через час будет: '
    one_hour = timedelta(hours=1)
    get_time_future = datetime.now() + one_hour
    return current_time_after_hour + str(get_time_future)

if __name__ == '__main__':
    app.run(debug=True, port=4000)  # поменяли порт на 4000
