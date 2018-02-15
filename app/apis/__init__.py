from flask import jsonify
from flask_restplus import Api
from jwt.exceptions import InvalidTokenError
from flask_jwt_extended.exceptions import JWTExtendedException

from app.extensions import jwt
from .auth.resources import api as auth


class MyApi(Api):
    def handle_error(self, e):
        if isinstance(e, InvalidTokenError):
            return jsonify(
                collections.OrderedDict([
                    ('status_code', e.status_code),
                    ('error', e.error),
                    ('description', e.description),
                ])), e.status_code, e.headers
        if isinstance(e, JWTExtendedException):
            return jsonify(
                collections.OrderedDict([
                    ('status_code', e.status_code),
                    ('error', e.error),
                    ('description', e.description),
                ])), e.status_code, e.headers
        return super(MyApi, self).handle_error(e)


api = MyApi(
    title='habittracker',
    version='1.0',
    description='None',
    doc='/docs',
    prefix='/api',
    ui=False)

api.add_namespace(auth, path="/auth")


@jwt.expired_token_loader
def expired_token_callback():
    return jsonify(error="The token has expired"), 401


@jwt.invalid_token_loader
def invalid_token_callback(msg):
    return jsonify(error="The token is Invalid"), 401


@jwt.unauthorized_loader
def unauthorized_loader(msg):
    return jsonify(error="No token presented"), 401
