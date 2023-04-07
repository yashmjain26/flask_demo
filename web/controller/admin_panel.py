import os
from flask import (
    Blueprint,
    Flask,
    render_template,
    request,
    session,
    redirect,
    url_for,
    send_file,
    abort,
    flash,
)
from constant.constant import *
from helper.authz import is_authenticated
import pandas as pd

admin_bp = Blueprint("admin_bp", __name__)


@admin_bp.route("/view_files")
@is_authenticated
def view_files():
    files_lst = []
    for _file in os.listdir(UPLOAD_PATH):
        files_lst.append(_file)

    return render_template("view_files.html", files=files_lst)


@admin_bp.route("/download/<path:filename>", methods=["GET"])
@is_authenticated
def download(filename):
    path = UPLOAD_PATH + "/" + filename
    if not os.path.isfile(path):
        abort(404)
    return send_file(path)


@admin_bp.route("/show/<path:filename>", methods=["GET"])
@is_authenticated
def show(filename):
    path = UPLOAD_PATH + "/" + filename
    if not os.path.isfile(path):
        abort(404)
    if filename.endswith(".csv"):
        data = pd.read_csv(path)
    else:
        data = pd.read_excel(path)
    return render_template("show_data.html", tables=[data.to_html()], titles=[""])


@admin_bp.route("/login", methods=["GET", "POST"])
def login():
    err = None
    if request.method == "POST":
        if (
            request.form["username"] != ADMIN_USERNAME
            and request.form["password"] != ADMIN_PASSWORD
        ):
            err = "Invalid Username or Password"
        else:
            session["logged_in"] = True
            return redirect(url_for("admin_bp.view_files"))
    return render_template("login.html", error=err)


@admin_bp.route("/logout")
def logout():
    session.pop("logged_in", None)
    flash("You were logged out")
    return render_template("login.html")
