from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restplus import Namespace, Resource, fields, reqparse

from .controllers import get_habits, add_habits

api = Namespace("habits", description="Habit")

habit_fields = reqparse.RequestParser()
habit_fields.add_argument("name", type=str, required=True, location="form")
habit_fields.add_argument(
    "period",
    choices=("daily", "weekly", "monthly", "yearly"),
    help="Can only be 'daily', 'weekly', 'monthly', 'yearly'",
    required=True,
    location="form")
habit_fields.add_argument("target_seconds", type=int, required=True, location="form")


@api.route("/")
class Habit(Resource):

    @jwt_required
    @api.header("Authorization", "access_token", required=True)
    def get(self):
        username = get_jwt_identity()

        return get_habits(username)


@api.route("/add")
class AddHabit(Resource):

    @jwt_required
    @api.header("Authorization", "access_token", required=True)
    @api.doc(body=habit_fields)
    @api.expect(habit_fields)
    def post(self):
        username = get_jwt_identity()

        args = habit_fields.parse_args()
        name = args.get("name")
        period = args.get("period")
        target_seconds = args.get("target_seconds")

        return add_habits(username, name, period, target_seconds)
