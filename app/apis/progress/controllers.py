import dateutil.parser
from flask import jsonify
from sqlalchemy import desc

from app.extensions import db
from .models import Progress
from ..habits.models import Habit
from ..users.models import User


def start_habit(username, habit_id, time):
    habit = Habit.query.with_parent(
        User.query.filter_by(username=username).first()
    ).filter_by(id=habit_id).first()

    if not habit:
        response = jsonify(error={
            "message": "Habit {!s} not found".format(habit_id)
        })
        response.status_code = 404
        return response

    progress = db.session.query(Progress).with_parent(habit).\
        order_by(desc(Progress.date_created)).first()

    if progress.end_time == None if progress else False:
        response = jsonify(error={
            "message": "Habit {!s} had not end yet".format(habit_id)
        })
        response.status_code = 400
        return response

    try:
        progress = Progress(
            habit_id=habit_id,
            start_time=dateutil.parser.parse(time) if time else None
        )
        db.session.add(progress)
        db.session.commit()
    except ValueError:
        response = jsonify(error={
            "message": "Time are not formatted as ISO format"
        })
        response.status_code = 400
        return response

    return jsonify(success={
        "message": "Successfully started habit"
    })


def end_habit(username, habit_id, time):
    habit = Habit.query.with_parent(
        User.query.filter_by(username=username).first()
    ).filter_by(id=habit_id).first()

    if not habit:
        response = jsonify(error={
            "message": "Habit {!s} not found".format(habit_id)
        })
        response.status_code = 404
        return response

    progress = db.session.query(Progress).with_parent(habit).\
        order_by(desc(Progress.date_created)).first()

    if progress.end_time if progress else True:
        response = jsonify(error={
            "message": "Habit {!s} had not started yet".format(habit_id)
        })
        response.status_code = 400
        return response

    try:
        progress.end(dateutil.parser.parse(time) if time else None)
        db.session.commit()
    except ValueError:
        response = jsonify(error={
            "message": "Time are not formatted as ISO format"
        })
        response.status_code = 400
        return response

    return jsonify(success={
        "message": "Successfully ended habit"
    })
