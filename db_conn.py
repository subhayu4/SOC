import pymysql

DATABASE_URL = {
    "host": "localhost",
    "port": 3306,
    "database": "blog_service",
    "user": "subhayu",
    "password": "Sar@1"
}

# Create a database connection object
connection = pymysql.connect(host="localhost", port=3306, database="blog_service", user="subhayu", password="Sar@1")
