from flask import Flask,jsonify

app = Flask(__name__)

# users = ['Michal Kowalski','Andrzej Glowacki','Leon Nowak','Roksana Ron']

users ={'1':'Michal Kowalski',
        '2':'Andrzej Glowacki',
        '3':'Leon Nowak',
        '4':'Roksana Nowicka'}

user_passed = {}

@app.route('/users')
def list_current_users():
    return jsonify(users)
    print(users)

@app.route('/users/add/<int:id>/<string:name>')
def add_user(id, name):
    users[id] = name
    return jsonify(users)

# @app.route('/users/delete/<int:id>')
# def delete_user(id):
#     if id in users.key:
#         return True

    # users.pop(id, None)
    # return jsonify(users)
    # return 'User with id %d deleted' % id


# @app.route('/user/<username>')
# def show_user_profile(username):
#     # show the user profile for that user
#     return 'User %s' % username

# @app.route('/post/<int:post_id>')
# def show_post(post_id):
#     # show the post with the given id, the id is a int
#     return 'Post %d' % post_id

# @app.route('/path/<path:subpath>')
# def show_subpath(subpath):
#     # show the subpath after /path/
#     return 'Subpath %s' %subpath

if __name__ == '__main__':
    app.run()