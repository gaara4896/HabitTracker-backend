from werkzeug.security import check_password_hash, generate_password_hash

from app.extensions import db

from ..common import Base


class User(Base):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(128), nullable=True, unique=True)
    password_hash = db.Column(db.String(255), nullable=True)
    email = db.Column(db.String(128), nullable=False, unique=True)
    nickname = db.Column(db.String(255), nullable=False)
    email_verified = db.Column(db.Boolean, default=False)
    habits = db.relationship("Habit", backref='user', lazy=True)

    def __init__(self, username, password, email, nickname):
        self.username = username
        self.password_hash = self.generate_password(password)
        self.email = email
        self.nickname = nickname

    def __repr__(self):
        return "<User: {}>".format(self.username)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def update_password(self, password):
        self.password_hash = self.generate_password(password)
        return True

    def generate_password(self, password):
        return generate_password_hash(
            password, method='pbkdf2:sha512:10000', salt_length=30)

    @property
    def password(self):
        raise AttributeError('`password` is not a readable attribute')
