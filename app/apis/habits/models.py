from app.extensions import db

from ..common import Base


class Habit(Base):
    __tablename__ = "habits"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(255), nullable=False)
    period = db.Column(db.String(128), nullable=False)
    target_seconds = db.Column(db.Integer, nullable=False)
    active = db.Column(db.Boolean, default=True)

    def __init__(self, user_id, name, period, target_seconds):
        self.user_id = user_id
        self.name = name
        self.period = period
        self.target_seconds = target_seconds

    def __repr__(self):
        return "<Habit: {}>".format(self.name)

    def deactivate(self):
        self.active = False
