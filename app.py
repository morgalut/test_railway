from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Peace of Mind App is Live!"

@app.route('/health')
def health():
    return "OK", 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))

