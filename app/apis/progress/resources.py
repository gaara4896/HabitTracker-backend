from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restplus import Namespace, Resource, fields, reqparse

api = Namespace("progress", description="Progress")

habit_fields = reqparse.RequestParser()
habit_fields.add_argument("habit_id", type=int, required=True, location="form")
habit_fields.add_argument("time", type=str, required=False, location="form")


@api.route("/start")
class Start(Resource):

    @jwt_required
    @api.header("Authorization", "access_token", required=True)
    @api.doc(body=habit_fields)
    @api.expect(habit_fields)
    def post(self):
        username = get_jwt_identity()

        args = habit_fields.parse_args()
        habit_id = args.get("habit_id")
        time = args.get("time")

        return start_habit(username, habit_id, time)


@api.route("/end")
class End(Resource):

    @jwt_required
    @api.header("Authorization", "access_token", required=True)
    @api.doc(body=habit_fields)
    @api.expect(habit_fields)
    def post(self):
        username = get_jwt_identity()

        args = habit_fields.parse_args()
        habit_id = args.get("habit_id")
        time = args.get("time")

        return end_habit(username, habit_id, time)
