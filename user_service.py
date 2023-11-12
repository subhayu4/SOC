import json
from flask import Flask, request, jsonify
import psycopg2

app = Flask(__name__)

DATABASE_URL = "postgresql://localhost:5432/user_service"

# Create a connection to the database
connection = psycopg2.connect(DATABASE_URL)
cursor = connection.cursor()

# Get all users from the database
def get_all_users():
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    return users

# Create a new user in the database
def create_user(user):
    cursor.execute("INSERT INTO users (username, email) VALUES (%s, %s)", (user["username"], user["email"]))
    connection.commit()

# Get user by ID from the database
def get_user_by_id(user_id):
    cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
    user = cursor.fetchone()
    return user

# Update an existing user in the database
def update_user(user):
    cursor.execute("UPDATE users SET username = %s, email = %s WHERE id = %s", (user["username"], user["email"], user["id"]))
    connection.commit()

# Delete a user from the database
def delete_user(user_id):
    cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
    connection.commit()

# API route to get all users
@app.route("/users", methods=["GET"])
def users():
    if request.method == "GET":
        users = get_all_users()

        user_jsons = []
        for user in users:
            user_json = {
                "id": user[0],
                "username": user[1],
                "email": user[2]
            }
            user_jsons.append(user_json)

        return jsonify(user_jsons)
    elif request.method == "POST":
        user = json.loads(request.data)

        create_user(user)

        return jsonify({
            "message": "User created successfully"
        })

# API route to get a user by ID
@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = get_user_by_id(user_id)

    if user is not None:
        user_json = {
            "id": user[0],
            "username": user[1],
            "email": user[2]
        }
        return jsonify(user_json)
    else:
        return jsonify({
            "message": "User not found"
        })

# API route to update an existing user
@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    user = json.loads(request.data)
    user["id"] = user_id

    update_user(user)

    return jsonify({
        "message": "User updated successfully"
    })

# API route to delete a user
@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    delete_user(user_id)

    return jsonify({
        "message": "User deleted successfully"
    })

if __name__ == "__main__":
    app.run(debug=True)
