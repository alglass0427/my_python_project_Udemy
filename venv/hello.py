from flask import Flask

app = Flask(__name__)

##decorator  .
@app.route("/") ####Home returned by The main Web Address   --->> @ app decorator
def hello_world():
    return "<p>Hello, World!</p>"


if __name__ == "__main__":
    app.run(debug=True, port=8080)  ##flask run


