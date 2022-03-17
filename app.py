import clock_isip as ISIP
from flask import Flask

app = Flask(__name__)


@app.route("/")
def main():
    html = f"<h1>{ISIP.get_clocl_isip()} WIB</h1>"
    return html


if __name__ == "__main__":
    app.run()
