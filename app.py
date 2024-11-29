from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Peace of Mind App is Live!"

if __name__ == '__main__':
    app.run()
