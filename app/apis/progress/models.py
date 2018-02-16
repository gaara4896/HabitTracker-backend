from datetime import datetime

from app.extensions import db

from ..common import Base


class Progress(Base):
    __tablename__ = "progresses"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    habit_id = db.Column(db.Integer, db.ForeignKey("habits.id"), nullable=False)
    start_time = db.Column(db.DateTime, default=db.func.now())
    end_time = db.Column(db.DateTime, nullable=True)
    length_seconds = db.Column(db.Integer, nullable=True)

    def __init__(self, habit_id, start_time):
        self.habit_id = habit_id
        if start_time:
            self.start_time = start_time

    def end(self, end_time):
        self.end_time = end_time if end_time else datetime.now()
        self.length_seconds = (self.end_time - self.start_time).seconds

    def __repr__(self):
        return "<Progress: {} to {}>".format(self.start_time, self.end_time)
