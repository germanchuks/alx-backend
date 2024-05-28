#!/usr/bin/env python3
"""Basic Flask app"""

from flask import Flask, render_template, request, g
from flask_babel import Babel
import pytz
from pytz.exceptions import UnknownTimeZoneError
from datetime import datetime


class Config:
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """Returns user if passed and ID exists otherwise None."""
    user_id = request.args.get('login_as')
    if user_id and user_id.isdigit():
        return users.get(int(user_id))
    return None


@app.before_request
def before_request():
    """Set g.user before executing other functions"""
    g.user = get_user()


@babel.localeselector
def get_locale():
    """Determine the best match with our supported languages."""
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale

    if g.user:
        user_locale = g.user.get('locale')
        if user_locale in app.config['LANGUAGES']:
            return user_locale

    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone():
    """Find the for timezone from URL parameters, user settings or
    default to UTC"""
    timezone = request.args.get('timezone')
    if timezone:
        try:
            return pytz.timezone(timezone).zone
        except UnknownTimeZoneError:
            pass

    if g.user:
        user_timezone = g.user.get('timezone')
        if user_timezone:
            try:
                return pytz.timezone(user_timezone).zone
            except UnknownTimeZoneError:
                pass

    return app.config['BABEL_DEFAULT_TIMEZONE']


@app.route('/')
def index():
    """Outputs `Hello world` as header"""
    user_timezone = get_timezone()
    current_time = datetime.now(pytz.timezone(user_timezone)).strftime('%c')
    return render_template('index.html', current_time=current_time)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
