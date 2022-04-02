import clock_isip as ISIP
import sys

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
def main():
    result = ISIP.get_time_isip()

    if result != None:
        result = result['clock']
    else:
        result = "null"

    return render_template("main.html", clock=result)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
