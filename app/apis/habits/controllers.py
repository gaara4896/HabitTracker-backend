from flask import jsonify

from app.extensions import db
from .models import Habit
from ..users.models import User


def get_habits(username):
    user = User.query.filter_by(username=username).first()

    if not user:
        response = jsonify(error={
            "message": "User {} does not exists".format(username)
        })
        response.status_code = 404
        return response

    habits = Habit.query.filter_by(user_id=user.id, active=True).all()
    result = []
    for habit in habits:
        result.append({
            "name": habit.name,
            "period": habit.period,
            "target_seconds": habit.target_seconds
        })

    return jsonify(success={
        "result": result
    })


def add_habits(username, name, period, target_seconds):
    user = User.query.filter_by(username=username).first()

    if not user:
        response = jsonify(error={
            "message": "User {} does not exists".format(username)
        })
        response.status_code = 404
        return response

    habit = Habit(
        user_id=user.id,
        name=name,
        period=period,
        target_seconds=target_seconds)

    db.session.add(habit)

    try:
        db.session.commit()
    except Exception as e:
        print(e)
        response = jsonify(error={
            "message": "Unable to commit"
        })
        response.status_code = 500
        return response

    return jsonify(success={
        "message": "Successfully added habit {}".format(name)
    })
