import clock_isip as ISIP

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
def main():
    clock = ISIP.get_clocl_isip()
    return render_template("main.html", clock=clock)


if __name__ == "__main__":
    app.run()
