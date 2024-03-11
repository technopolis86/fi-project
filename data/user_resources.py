from flask_restful import reqparse, abort, Resource
from flask import jsonify
from .import db_session
from .users import User

parser = reqparse.RequestParser()
parser.add_argument("id", type=int)
parser.add_argument("team_leader_id", type=int)
parser.add_argument("job")
parser.add_argument("work_size", type=int)
parser.add_argument("collaborators")
parser.add_argument("start_date")
parser.add_argument("end_date")
parser.add_argument("is_finished", type=bool)


class UsersResource(Resource):
    def get(self, users_id):
        abort_if_users_not_found(users_id)
        session = db_session.create_session()
        users_id = session.query(User).get(users_id)
        return jsonify({'users': users_id.to_dict(
            only=("id",
                  "surname",
                  "name",
                  "age",
                  "position",
                  "speciality",
                  "address",
                  "email",
                  "hashed_password"))})

    def delete(self, users_id):
        abort_if_users_not_found(users_id)
        session = db_session.create_session()
        users = session.query(User).get(users_id)
        session.delete(users)
        session.commit()
        return jsonify({'success': 'OK'})


def abort_if_users_not_found(users_id):
    session = db_session.create_session()
    users = session.query(User).get(users_id)
    if not users:
        abort(404, message=f"Users {users_id} not found")


class UsersListResource(Resource):
    def get(self):
        session = db_session.create_session()
        users = session.query(User).all()
        return jsonify({'users': [item.to_dict(
            only=("id",
                  "surname",
                  "name",
                  "age",
                  "position",
                  "speciality",
                  "address",
                  "email",
                  "hashed_password")) for item in users]})

    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        users = User(
            id=args["id"],
            surname=args["surname"],
            name=args["name"],
            age=args["age"],
            position=args["position"],
            speciality=args["speciality"],
            address=args["address"],
            email=args["email"],
            hashed_password=args["hashed_password"]
        )
        session.add(users)
        session.commit()
        return jsonify({'success': 'OK'})
