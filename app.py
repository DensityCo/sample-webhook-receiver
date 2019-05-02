from flask import Flask, Response
from datetime import datetime
app = Flask(__name__)


@app.route('/')
def homepage():
    return Response(status=200)


if __name__ == '__main__':
    app.run(debug=False, use_reloader=True)
