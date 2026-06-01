from flask import Flask, jsonify, render_template, request, redirect, url_for
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user
from werkzeug.security import check_password_hash

from system_monitor import get_stats
from users import users

app = Flask(__name__)

app.secret_key = "supersecretkey"

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

class User(UserMixin):
    def __init__(self, username):
        self.id = username

@login_manager.user_loader
def load_user(user_id):
    return User(user_id)  # replace with your user lookup

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username in users and check_password_hash(users[username], password):
            user = User(username)
            login_user(user)
            return redirect(url_for("dashboard"))
        else:
            return "Invalid credentials", 401

    return render_template("login.html")


@app.route("/")
@login_required
def dashboard():

    stats = get_stats()

    return render_template(
        "dashboard.html",
        stats= stats
    )

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))

def home():
    return "Health Dashboard running"


@app.route("/home")
def home():
    return "Health Dashboard running"

@app.route("/health")
def health():
    return jsonify(get_stats())

if __name__ == '__main__':
    app.run(debug=True)
