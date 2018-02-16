from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restplus import Namespace, Resource, fields, reqparse

from .controllers import get_habits, add_habit, update_habit, activate_habit

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

update_fields = reqparse.RequestParser()
update_fields.add_argument("name", type=str, required=False, location="form")
update_fields.add_argument(
    "period",
    choices=("daily", "weekly", "monthly", "yearly"),
    help="Can only be 'daily', 'weekly', 'monthly', 'yearly'",
    required=False,
    location="form")
update_fields.add_argument("target_seconds", type=int, required=False, location="form")


@api.route("/")
class Habits(Resource):

    @jwt_required
    @api.header("Authorization", "access_token", required=True)
    def get(self):
        username = get_jwt_identity()

        return get_habits(username)


@api.route("/<int:habit_id>")
class Habit(Resource):

    @jwt_required
    @api.header("Authorization", "access_token", required=True)
    def get(self, habit_id):
        username = get_jwt_identity()

        return get_habits(username, habit_id=habit_id)

    @jwt_required
    @api.header("Authorization", "access_token", required=True)
    def post(self, habit_id):
        username = get_jwt_identity()

        return activate_habit(username, habit_id, True)

    @jwt_required
    @api.header("Authorization", "access_token", required=True)
    @api.doc(body=update_fields)
    @api.expect(update_fields)
    def put(self, habit_id):
        username = get_jwt_identity()

        args = update_fields.parse_args()
        name = args.get("name")
        period = args.get("period")
        target_seconds = args.get("target_seconds")

        return update_habit(username, habit_id, name, period, target_seconds)

    @jwt_required
    @api.header("Authorization", "access_token", required=True)
    def delete(self, habit_id):
        username = get_jwt_identity()

        return activate_habit(username, habit_id, False)


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

        return add_habit(username, name, period, target_seconds)
