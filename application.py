from flask import Flask, render_template

application = Flask(__name__)


@application.route("/", methods=["GET", "POST"])
def home():
    return "<h3> WELCOME TO AWS DEPLOYMENT </h3>"


if __name__ == "__main__":
    application.run()