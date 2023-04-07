from functools import wraps
from flask import session, render_template


def is_authenticated(fuc):
    @wraps(fuc)
    def wrapped(*args, **kwargs):
        if not session.get("logged_in"):
            return render_template("login.html")
        return fuc(*args, **kwargs)

    return wrapped
