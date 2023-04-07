from flask import (
    Flask,
    render_template,
    request,
    session,
    redirect,
    url_for,
    send_file,
    abort,
    flash
)
from distutils.log import debug
from fileinput import filename
from constant.constant import *

from controller.admin_panel import admin_bp
from controller.upload import upload_blueprint

app = Flask(__name__)
app.secret_key = APP_SECRETE

app.register_blueprint(admin_bp, url_prefix="/")
app.register_blueprint(upload_blueprint, url_prefix="/")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
