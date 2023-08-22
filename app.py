from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'This is working!'


app.run(port=5000, debug=True)
