import logging
from src.allocation.service_layer import unit_of_work
from flask import make_response, jsonify

logger = logging.getLogger(__name__)


def get_users_info(uow: unit_of_work.AbstractUnitOfWork):
    with uow:
        results = uow.users.get_user_info()

    if not results:
        return jsonify({"error": "No users were found"}), 404

    return jsonify([dict(r) for r in results])




def get_role(role_id: int, uow: unit_of_work.AbstractUnitOfWork):
    
    if role_id is not None and not isinstance(role_id, int):
        try:
            role_id = int(role_id)
        except ValueError:
            response = {
                "error": "role_id must be an integer value"
            }
            return make_response(jsonify(response), 400)
    else:
            return make_response(jsonify({"error": "role_id must not be null"}), 404)
        
    with uow:
        result = uow.users.get_role_by_id(role_id)

    if not result:
        return make_response(jsonify({"error": "Not found"}), 404)

    return result


