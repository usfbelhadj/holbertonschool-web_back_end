#!/usr/bin/env python3
"""
Basic Babel app
"""

from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config:
    """[Config]"""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@app.route("/", methods=["GET"], strict_slashes=False)
def index():
    """
    Basic Flask app
    """
    return render_template("4-index.html")


@babel.localeselector
def get_locale():
    """
    match with our supported languages
    """
    local = request.args.get("locale")
    if local is None:
        return None
    else:
        return local
    return request.accept_languages.best_match([Config.LANGUAGES])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
