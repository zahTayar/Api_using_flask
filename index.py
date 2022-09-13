from flask import Flask

app = Flask(__name__)


@app.route('/', methods=["GET"])
def index():
    return "maybe you should bring us something to drink?", 200


if __name__ == '__main__':
    app.run(port=5500)
