{\rtf1\ansi\ansicpg1252\cocoartf2709
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 from flask import Flask, request, jsonify\
import requests\
\
app = Flask(__name__)\
comments = \{\}\
\
@app.route('/comments', methods=['POST'])\
def create_comment():\
    data = request.get_json()\
    comment_id = len(comments) + 1\
    comments[comment_id] = data\
    return jsonify(comments[comment_id]), 201\
\
@app.route('/comments', methods=['GET'])\
def get_all_comments():\
    return jsonify(comments)\
\
@app.route('/comments/<int:comment_id>', methods=['PUT'])\
def update_comment(comment_id):\
    data = request.get_json()\
    comments[comment_id].update(data)\
    return jsonify(comments[comment_id])\
\
if __name__ == '__main__':\
    app.run(port=5003, debug=True)\
}