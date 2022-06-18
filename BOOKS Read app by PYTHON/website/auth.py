from flask import Blueprint, render_template, redirect, url_for, request, flash
from .models import User
from werkzeug.security import generate_password_hash,check_password_hash
from. import db
from flask_login import login_required, logout_user, login_user, current_user
from .sender import sender

auth = Blueprint("auth", __name__)

@auth.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash("Logged in successfully",category="success")
                login_user(user, remember=True)
                return redirect(url_for("views.my_books"))
            else:
                flash("incorrect password", category="error")
        else:
            flash("user does not exist",category="error")
    return render_template("login.jinja2", user=current_user)

@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login"))

@auth.route("/sign-up", methods=["POST", "GET"])
def sign_up():
    if request.method == "POST":
        email = request.form.get("email")
        firstname = request.form.get("firstname")
        surname = request.form.get("surname")
        middlename = request.form.get("middlename")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        user = User.query.filter_by(email=email).first()
        if user:
            flash("Email exists", "error")
        elif len(email) < 4:
            flash('Invalid email', category="error")
        elif len(firstname) < 2:
            flash('First name must be more than 1 character', category="error")
        elif len(surname) < 3:
            flash('Surname must be more than 1 character', category="error")
        elif len(middlename) < 1:
            flash('Middle name must be more than 1 character', category="error")
        elif len(password1) < 7:
            flash('Password is too short', category="error")
        elif password1 != password2:
            flash('Password must match', category="error")
        else:
            new_user = User(email=email, firstname=firstname,lastname=surname,middlename=middlename,password=generate_password_hash(password1, method="sha256"))
            db.session.add(new_user)
            db.session.commit()
            sender(email)
            flash("Account Created", category="success")
            login_user(new_user, remember=True)
            return redirect(url_for('views.my_books'))

    return render_template("signup.jinja2", user= current_user)
