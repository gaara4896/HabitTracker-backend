import dateutil.parser
from flask import jsonify
from sqlalchemy import desc

from app.extensions import db
from .models import Progress
from ..habits.models import Habit
from ..users.models import User


def get_progress(username, progress_id=None):
    user = User.query.filter_by(username=username).first()

    if not progress_id:
        result = []
        for habit in user.habits:
            for progress in habit.progresses:
                result.append({
                    "id": progress.id,
                    "habit_id": habit.id,
                    "start_time": progress.start_time.isoformat(),
                    "end_time": progress.end_time.isoformat() if progress.end_time else "",
                    "length_seconds": progress.length_seconds if progress.length_seconds else "",
                    "removed": progress.removed if progress.removed else False
                })
    else:
        progress = db.session.query(Progress).with_parent(
            db.session.query(Habit).with_parent(user).outerjoin(Habit.progresses).filter(
                Habit.progresses.any(Progress.id == progress_id)
            ).first()
        ).filter_by(id=progress_id).first()

        if not progress:
            response = jsonify(error={
                "message": "Progress {!s} not found".format(habit_id)
            })
            response.status_code = 404
            return response

        result = {
            "id": progress.id,
            "habit_id": progress.habit_id,
            "start_time": progress.start_time.isoformat(),
            "end_time": progress.end_time.isoformat() if progress.end_time else "",
            "length_seconds": progress.length_seconds if progress.length_seconds else "",
            "removed": progress.removed if progress.removed else False
        }

    return jsonify(success={
        "result": result
    })


def update_progress(username, progress_id, start_time, end_time):
    progress = db.session.query(Progress).with_parent(
        db.session.query(Habit).with_parent(
            User.query.filter_by(username=username).first()
        ).outerjoin(Habit.progresses).filter(
            Habit.progresses.any(Progress.id == progress_id)
        ).first()
    ).filter_by(id=progress_id).first()

    if not progress:
        response = jsonify(error={
            "message": "Progress {!s} not found".format(progress_id)
        })
        response.status_code = 404
        return response

    try:
        if start_time:
            progress.update_start_time(dateutil.parser.parse(start_time))
        if end_time:
            progress.update_end_time(dateutil.parser.parse(end_time))
        db.session.commit()
    except ValueError:
        response = jsonify(error={
            "message": "Time are not formatted as ISO format"
        })
        response.status_code = 400
        return response

    return jsonify(success={
        "message": "Successfully update progress {!s}".format(progress_id)
    })


def delete_progress(username, progress_id, restore=False):
    progress = db.session.query(Progress).with_parent(
        db.session.query(Habit).with_parent(
            User.query.filter_by(username=username).first()
        ).outerjoin(Habit.progresses).filter(
            Habit.progresses.any(Progress.id == progress_id)
        ).first()
    ).filter_by(id=progress_id).first()

    if not progress:
        response = jsonify(error={
            "message": "Progress {!s} not found".format(progress_id)
        })
        response.status_code = 404
        return response

    progress.removed = not restore
    db.session.commit()

    return jsonify(success={
        "message": "Successfully {} progress {!s}".format("restore" if restore else "remove", progress_id)
    })


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
