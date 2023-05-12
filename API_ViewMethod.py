from flask import Flask, jsonify, request
from flask.views import MethodView

app = Flask(__name__)

# A simple in-memory data store
USERS = {
    1: 'Surendra',
    2: 'DEV',
}

class UserAPI(MethodView):
    def get(self, user_id):
        if user_id is None:
            # return a list of users
            return jsonify(USERS), 200
        else:
            # expose a single user
            if user_id in USERS:
                return jsonify({user_id: USERS[user_id]}), 200
            else:
                return jsonify({'error': 'Not found'}), 404

    def post(self):
        # create a new user
        user_id = max(USERS.keys()) + 1
        USERS[user_id] = request.json.get('name')
        return jsonify({user_id: USERS[user_id]}), 201

user_view = UserAPI.as_view('user_api')
app.add_url_rule('/users/', defaults={'user_id': None},
                 view_func=user_view, methods=['GET',])
app.add_url_rule('/users/', view_func=user_view, methods=['POST',])
app.add_url_rule('/users/<int:user_id>', view_func=user_view,
                 methods=['GET',])

if __name__ == '__main__':
    app.run(debug=True)
# Code for data loading process