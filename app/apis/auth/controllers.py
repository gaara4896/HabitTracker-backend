import secrets
import string

from flask import jsonify
from flask_jwt_extended import create_access_token, create_refresh_token
from flask_mail import Message
from sqlalchemy.exc import IntegrityError

from app.extensions import db, mail

from ..users.models import User


def register(username, password, email, nickname):
    user = User(
        username=username,
        password=password,
        email=email,
        nickname=nickname
    )
    db.session.add(user)

    try:
        db.session.commit()
    except IntegrityError:
        response = jsonify(
            error="The username {!r} already exists.".format(username))
        response.status_code = 400
        return response

    return jsonify(success="Success created user " + username)


def login(username, password):
    user = User.query.filter_by(username=username).first()

    if not user:
        response = jsonify(error="No user exist")
        response.status_code = 400
        return response

    if(user.check_password(password)):
        return jsonify(success={
            "access_token": create_access_token(identity=username, fresh=True),
            "refresh_token": create_refresh_token(identity=username)
        })
    else:
        response = jsonify(error="Wrong password")
        response.status_code = 400
        return response


def refresh(identity):
    return jsonify(access_token=create_access_token(identity=identity, fresh=False))


def change_password(username, password_new):
    user = User.query.filter_by(username=username).first()

    if not user:
        response = jsonify(error="No user exist")
        response.status_code = 400
        return response

    user.update_password(password_new)
    db.session.commit()

    return jsonify(success="Successful update password")


def reset_password(username):
    user = User.query.filter_by(username=username).first()

    if not user:
        response = jsonify(error="No user exist")
        response.status_code = 400
        return response

    alphabet = string.ascii_letters + string.digits
    new_password = "".join(secrets.choice(alphabet) for i in range(10))
    print(new_password)
    user.update_password(new_password)
    db.session.commit()

    msg = Message("New password", recipients=[user.email])
    msg.body = "Dear " + user.username + ", \n\n" + \
        "Your new password is: " + new_password
    mail.send(msg)

    return jsonify(success="Please check email")
