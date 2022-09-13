from flask import Flask
from flask import request
import json

app = Flask(__name__)


# ADMIN METHODS BY REST API TEMPLATE

@app.route('/fma', methods=["GET"])
def basic_path():
    return "This is our basic type", 200


@app.route('/fma/admin/users/<user_email>', methods=["GET"])
def get_all_users(user_email) -> json:
    if "@" not in user_email:
        return {}
    dic = {"1": "one", "2": "two"}  # suppose to be dictionary of all users
    return dic


@app.route('/fma/admin/operations/<user_email>', methods=["GET"])
def get_all_operations(user_email) -> json:
    if "@" not in user_email:
        return {}
    dic = {"1": "one", "2": "two"}  # suppose to be dictionary of all users
    return dic


@app.route('/fma/admin/users/<user_email>', methods=["DELETE"])
def delete_all_users(user_email):
    return f'Hello {user_email}'


@app.route('/fma/admin/items/<user_email>', methods=["DELETE"])
def delete_all_items(user_email):
    return f'Hello {user_email}'


@app.route('/fma/admin/operations/<user_email>', methods=["DELETE"])
def delete_all_operations(user_email):
    return f'Hello {user_email}'


# ITEMS METHODS BY REST API TEMPLATE
# -------------------------------------------

@app.route('/fma/items/<user_email>', methods=["POST"])
def get_items_of_specific_search_by_user(user_email) -> json:
    return request.data


@app.route('/fma/items/<user_email>/<item_id>', methods=["GET"])
def get_specific_item(user_email, item_id) -> json:
    return {}


@app.route('/fma/items/store/<user_email>', methods=["POST"])
def store_item(user_email) -> json:
    return request.data


@app.route('/fma/items/<user_email>/<item_id>', methods=["PUT"])
def update_item(user_email, item_id) -> json:
    return request.data


# OPERATIONS METHODS BY REST API TEMPLATE
# -------------------------------------------

@app.route('/fma/operations', methods=["POST"])
def invoked_operation() -> json:
    return request.data


@app.route('/fma/operations/async', methods=["POST"])
def invoked_async_operation() -> json:
    return request.data


# USERS METHODS BY REST API TEMPLATE
# -------------------------------------------


@app.route('/fma/users/login/<user_email>', methods=["GET"])
def get_user_details(user_email) -> json:
    return {}


@app.route('/fma/users', methods=["POST"])
def create_new_user() -> json:
    return request.data


@app.route('/fma/users/<user_email>', methods=["PUT"])
def update_user_details() -> json:
    return request.data


if __name__ == '__main__':
    app.run(port=5500)
