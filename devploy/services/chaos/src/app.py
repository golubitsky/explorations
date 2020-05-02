from flask import Flask
import pika

app = Flask(__name__)


def send_message():
    pass


@app.route('/health')
def health():
    return f"Hello from chaos"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
