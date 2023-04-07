import os
from constant.constant import *
from flask import (
    Blueprint,
    render_template,
    request,
)

upload_blueprint = Blueprint("upload_blueprint", __name__)


@upload_blueprint.route("/")
def main():
    return render_template("welcome.html")


@upload_blueprint.route("/upload_file")
def upload_file():
    return render_template("upload_file.html")


@upload_blueprint.route("/file_upload", methods=["POST"])
def file_upload():
    if request.method == "POST":
        f = request.files["file"]
        f.save(UPLOAD_PATH + "/" + f.filename)
        return render_template("file_uploaded.html", name=f.filename)
