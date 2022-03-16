from flask import Flask, render_template

application = Flask(__name__)


@application.route("/", methods=["GET", "POST"])
def home():
    response = 1
    return render_template("home.html", data=response)


if __name__ == "__main__":
    application.run()