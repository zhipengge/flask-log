from flask import Flask, render_template
from flask_socketio import SocketIO
import threading
import time
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


def log_info(s: str):
    socketio.emit('log_message', {'data': s})

def get_current_time()->str:
    now = datetime.now()
    now_str = now.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
    return now_str

def write_log():
    while True:
        time.sleep(1)
        cur_time = get_current_time()
        log_info(f"log at {cur_time}")


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    threading.Thread(target=write_log).start()
    socketio.run(app, port=8000, debug=True)