from flask_restplus import Api
from jwt.exceptions import InvalidTokenError
from flask_jwt_extended.exceptions import JWTExtendedException


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
