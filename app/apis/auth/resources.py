from flask_jwt_extended import fresh_jwt_required, get_jwt_identity, jwt_refresh_token_required
from flask_restplus import Namespace, Resource, fields, reqparse

from .controllers import login, register, refresh, change_password, reset_password

api = Namespace("auth", description="Authentication")

user_fields = reqparse.RequestParser()
user_fields.add_argument("username", type=str, required=True, location="form")

auth_fields = user_fields.copy()
auth_fields.add_argument("password", type=str, required=True, location="form")

register_fields = auth_fields.copy()
register_fields.add_argument("email", type=str, required=True, location="form")
register_fields.add_argument("nickname", type=str, required=True, location="form")

password_change_fields = reqparse.RequestParser()
password_change_fields.add_argument(
    "password_new", type=str, required=True, location="form")

password_fields = reqparse.RequestParser()
password_fields.add_argument(
    "password", type=str, required=True, location="form")


@api.route("/register")
class Register(Resource):

    @api.doc(body=register_fields)
    @api.expect(register_fields)
    def post(self):
        args = register_fields.parse_args()

        username = args.get("username")
        password = args.get("password")
        email = args.get("email")
        nickname = args.get("nickname")

        return register(username, password, email, nickname)


@api.route("/login")
class Login(Resource):

    @api.doc(body=auth_fields)
    @api.expect(auth_fields)
    def post(self):
        args = auth_fields.parse_args()

        username = args.get("username")
        password = args.get("password")

        return login(username, password)


@api.route("/fresh-login")
class FreshLogin(Resource):

    @api.doc(body=auth_fields)
    @api.expect(auth_fields)
    def post(self):
        args = auth_fields.parse_args()

        username = args.get("username")
        password = args.get("password")

        return login(username, password, fresh=True)


@api.route("/refresh")
class Refresh(Resource):

    @jwt_refresh_token_required
    @api.header("Authorization", "refresh token", required=True)
    def post(self):
        identity = get_jwt_identity()

        return refresh(identity)


@api.route("/change-password")
class ChangePassword(Resource):

    @fresh_jwt_required
    @api.header("Authorization", "fresh access token", required=True)
    @api.doc(body=password_change_fields)
    @api.expect(password_change_fields)
    def post(self):
        args = password_change_fields.parse_args()

        username = get_jwt_identity()
        password_new = args.get("password_new")

        return change_password(username, password_new)


@api.route("/reset-password")
class ResetPassword(Resource):

    @api.doc(body=user_fields)
    @api.expect(user_fields)
    def post(self):
        args = user_fields.parse_args()

        username = args.get("username")

        return reset_password(username)
