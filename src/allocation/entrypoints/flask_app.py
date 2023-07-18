from flask import Flask, request, jsonify
from src.allocation import bootstrap, views
from src.allocation.entrypoints.dto.userDTO import UserDTO

app = Flask(__name__)
bus = bootstrap.bootstrap()


@app.route("/add_user", methods=["POST"])
def add_user():
        dto = UserDTO(**request.json)
        bus.handle(dto.getCommand())
        return "OK"
    

@app.route("/users", methods=["GET"])
def get_users_info_route():
    result = views.get_users_info(bus.uow)
    return result

@app.route("/role", methods=["GET"])
def get_role():
    role_id = request.args.get("role_id")
    result = views.get_role(role_id, bus.uow)
    return result
