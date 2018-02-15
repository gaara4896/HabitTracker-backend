import hashlib

from app.extensions import db


class Base(db.Model):
    __abstract__ = True

    date_created = db.Column(db.DateTime, default=db.func.now())
    date_updated = db.Column(
        db.DateTime, default=db.func.now(), onupdate=db.func.now())

    def hash(self, word):
        return hashlib.sha512(word.encode("utf-8")).hexdigest()
