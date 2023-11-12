import json
from flask import Flask, request, jsonify

app = Flask(__name__)

USER_SERVICE_URL = "http://user-service:8000"
BLOG_POST_SERVICE_URL = "http://blog-post-service:8000"
COMMENT_SERVICE_URL = "http://comment-service:8000"

@app.route("/")
def index():
    return jsonify({
        "message": "Welcome to the blogging platform API"
    })

@app.route("/users", methods=["GET", "POST"])
def users():
    if request.method == "GET":
        response = requests.get(f"{USER_SERVICE_URL}/users")
        return jsonify(response.json())
    elif request.method == "POST":
        user = json.loads(request.data)
        response = requests.post(f"{USER_SERVICE_URL}/users", json=user)
        return jsonify(response.json())

@app.route("/blog-posts", methods=["GET", "POST"])
def blog_posts():
    if request.method == "GET":
        response = requests.get(f"{BLOG_POST_SERVICE_URL}/blog-posts")
        return jsonify(response.json())
    elif request.method == "POST":
        blog_post = json.loads(request.data)
        response = requests.post(f"{BLOG_POST_SERVICE_URL}/blog-posts", json=blog_post)
        return jsonify(response.json())

@app.route("/comments", methods=["GET", "POST"])
def comments():
    if request.method == "GET":
        response = requests.get(f"{COMMENT_SERVICE_URL}/comments")
        return jsonify(response.json())
    elif request.method == "POST":
        comment = json.loads(request.data)
        response = requests.post(f"{COMMENT_SERVICE_URL}/comments", json=comment)
        return jsonify(response.json())

if __name__ == "__main__":
    app.run(debug=True)
