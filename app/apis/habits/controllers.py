from flask import jsonify

from app.extensions import db
from .models import Habit
from ..users.models import User


def get_habits(username, habit_id=None):
    user = User.query.filter_by(username=username).first()

    if not habit_id:
        result = []
        for habit in user.habits:
            result.append({
                "id": habit.id,
                "name": habit.name,
                "period": habit.period,
                "target_seconds": habit.target_seconds,
                "active": habit.active
            })
    else:
        habit = Habit.query.with_parent(user).filter_by(id=habit_id).first()

        if not habit:
            response = jsonify(error={
                "message": "Habit {!s} not found".format(habit_id)
            })
            response.status_code = 404
            return response

        result = {
            "id": habit.id,
            "name": habit.name,
            "period": habit.period,
            "target_seconds": habit.target_seconds,
            "active": habit.active
        }

    return jsonify(success={
        "result": result
    })


def add_habit(username, name, period, target_seconds):
    user = User.query.filter_by(username=username).first()

    habit = Habit(
        user_id=user.id,
        name=name,
        period=period,
        target_seconds=target_seconds)

    db.session.add(habit)

    try:
        db.session.commit()
    except:
        response = jsonify(error={
            "message": "Unable to commit"
        })
        response.status_code = 500
        return response

    return jsonify(success={
        "message": "Successfully added habit {}".format(name)
    })


def update_habit(username, habit_id, name, period, target_seconds):
    user = User.query.filter_by(username=username).first()

    habit = Habit.query.with_parent(user).filter_by(id=habit_id).first()

    if not habit:
        response = jsonify(error={
            "message": "Habit {!s} not found".format(habit_id)
        })
        response.status_code = 404
        return response

    habit.name = name if name else habit.name
    habit.period = period if period else habit.period
    habit.target_seconds = target_seconds if target_seconds else habit.target_seconds

    db.session.commit()

    return jsonify(success={
        "message": "Successfully update habit {!s}".format(habit_id)
    })


def activate_habit(username, habit_id, active):
    user = User.query.filter_by(username=username).first()

    habit = Habit.query.with_parent(user).filter_by(id=habit_id).first()

    if not habit:
        response = jsonify(error={
            "message": "Habit {!s} not found".format(habit_id)
        })
        response.status_code = 404
        return response

    habit.active = active
    db.session.commit()

    return jsonify(success={
        "message": "Successfully {} habit {!s}".format("activate" if active else "deactivate", habit_id)
    })
