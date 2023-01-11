import json
import os

def check_login(email, password):
    login_data = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'static', 'docs', 'users.json')
    with open(login_data) as f:
        users = json.load(f)["users"]
    for user in users:
        if user['email'] == email and user['password'] == password:
            return 200
    return 400

