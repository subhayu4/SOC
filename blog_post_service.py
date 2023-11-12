import json
from flask import Flask, request, jsonify
import psycopg2

app = Flask(__name__)

DATABASE_URL = "postgresql://localhost:5432/blog_post_service"

# Create a connection to the database
connection = psycopg2.connect(DATABASE_URL)
cursor = connection.cursor()

# Get all blog posts from the database
def get_all_blog_posts():
  cursor.execute("SELECT * FROM blog_posts")
  blog_posts = cursor.fetchall()
  return blog_posts

# Get blog post by ID from the database
def get_blog_post_by_id(blog_post_id):
  cursor.execute("SELECT * FROM blog_posts WHERE id = %s", (blog_post_id,))
  blog_post = cursor.fetchone()
  return blog_post

# Create a new blog post in the database
def create_blog_post(blog_post):
  cursor.execute("INSERT INTO blog_posts (title, content, author_id) VALUES (%s, %s, %s)", (blog_post["title"], blog_post["content"], blog_post["author_id"]))
  connection.commit()

# Update an existing blog post in the database
def update_blog_post(blog_post):
  cursor.execute("UPDATE blog_posts SET title = %s, content = %s, author_id = %s WHERE id = %s", (blog_post["title"], blog_post["content"], blog_post["author_id"], blog_post["id"]))
  connection.commit()

# Delete a blog post from the database
def delete_blog_post(blog_post_id):
  cursor.execute("DELETE FROM blog_posts WHERE id = %s", (blog_post_id,))
  connection.commit()

# API route to get all blog posts
@app.route("/blog-posts", methods=["GET"])
def get_blog_posts():
  blog_posts = get_all_blog_posts()

  blog_post_jsons = []
  for blog_post in blog_posts:
    blog_post_json = {
      "id": blog_post[0],
      "title": blog_post[1],
      "content": blog_post[2],
      "author_id": blog_post[3]
    }
    blog_post_jsons.append(blog_post_json)

  return jsonify(blog_post_jsons)

# API route to get a blog post by ID
@app.route("/blog-posts/<int:blog_post_id>", methods=["GET"])
def get_blog_post(blog_post_id):
  blog_post = get_blog_post_by_id(blog_post_id)

  if blog_post is not None:
    blog_post_json = {
      "id": blog_post[0],
      "title": blog_post[1],
      "content": blog_post[2],
      "author_id": blog_post[3]
    }
    return jsonify(blog_post_json)
  else:
    return jsonify({
      "message": "Blog post not found"
    })

# API route to create a new blog post
@app.route("/blog-posts", methods=["POST"])
def create_blog_post():
  blog_post = json.loads(request.data)

  create_blog_post(blog_post)

  return jsonify({
    "message": "Blog post created successfully"
  })

# API route to update an existing blog post
@app.route("/blog-posts/<int:blog_post_id>", methods=["PUT"])
def update_blog_post(blog_post_id):
  blog_post = json.loads(request.data)
  blog_post["id"] = blog_post_id

  update_blog_post(blog_post)

  return jsonify({
    "message": "Blog post updated successfully"
  })

# API route to delete a blog post
@app.route("/blog-posts/<int:blog_post_id>", methods=["DELETE"])
def delete_blog_post(blog_post_id):
  delete_blog_post(blog_post_id)

  return jsonify({
    "message": "Blog post deleted successfully"
  })

if __name__:()
