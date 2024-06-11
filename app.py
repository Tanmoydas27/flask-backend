from flask import Flask, request, jsonify, redirect, url_for, session
from flask_cors import CORS
from flask_pymongo import PyMongo, ObjectId
from google.oauth2 import id_token # type: ignore
from google.auth.transport import requests as google_requests # type: ignore
import jwt # type: ignore
from functools import wraps
import datetime
import config


app = Flask(__name__)
app.config["MONGO_URI"] = config.MONGO_URI
app.config["SESSION_TYPE"] = 'filesystem'
app.secret_key ='your-secret-key'
SECRET_KEY = 'your-secret-key'

CORS(app, origins=config.FONTEND_API )
mongo = PyMongo(app)
db = mongo.db.tasks

@app.route("/login", methods=["POST"])
def login():
    token = request.json.get('token')
    try:
        idInfo = id_token.verify_oauth2_token(token, google_requests.Request(), config.GOOGLE_CLIENT_ID)
        user_id = idInfo['sub']

        payload = {
            'user_id' : user_id,
            'exp' : datetime.datetime.now(datetime.UTC) + datetime.timedelta(hours=48)
        }
        jwt_token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')

        return jsonify(success=True, message="User logged in", token=jwt_token)
    except ValueError as e:
        return jsonify(error=str(e)), 400


def token_required(f):
    @wraps(f) 
    def decorated(*args, **kwargs):
        token = None

        if 'Authorization' in request.headers:
            token = request.headers['Authorization'].split(" ")[1]
    
        if not token:
            return jsonify(error ="Token is missing!"), 401
        
        try:
            data = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
            current_user_id = data['user_id']
        except jwt.ExpiredSignatureError:
            return jsonify(error="Token has expired!"), 401
        except jwt.InvalidTokenError:
            return jsonify(error="Invalid token!"), 401
        
        return f(current_user_id, *args, **kwargs)
    return decorated


@app.route("/", methods=["GET"])
def home():
    return jsonify(message="Home Route In this Server")

@app.route("/tasks", methods=["GET"])
@token_required
def get_all_tasks(current_user_id):
    try:
        tasks = []
        for task in db.find({"user_id": current_user_id}):
            tasks.append({
                "_id": str(task["_id"]),
                "title": task["title"],
                "description": task["description"],
                "completed": task.get("completed", False),  
            })
        return jsonify(tasks)
    except Exception as e:
        return jsonify(error=str(e)), 500

@app.route("/tasks/<id>", methods=["GET"])
@token_required
def get_task_by_id(current_user_id,id: str):
    try:
        task = db.find_one({"_id": ObjectId(id), "user_id": current_user_id,})
        if task:
            task["_id"] = str(task["_id"])
            task["completed"] = task.get("completed", False)
            return jsonify(task=task, success=True)
        return jsonify(error="Task not found"), 404
    except Exception as e:
        return jsonify(error=str(e)), 500


@app.route("/tasks", methods=["POST"])
@token_required
def create_task(current_user_id):
    
    try:
        task = db.insert_one({
            "title": request.json["title"],
            "description": request.json["description"],
            "completed": request.json.get("completed", False),
            "user_id" : current_user_id  
        })
        return jsonify(id=str(task.inserted_id), success=True, message="task created successfully.")
    except Exception as e:
        return jsonify(error=str(e)), 500


@app.route("/tasks/<id>", methods=["DELETE"])
@token_required
def delete_task(current_user_id, id: str):
    
    try:
        db.delete_one({"_id": ObjectId(id),"user_id": current_user_id})
        return jsonify(message="Task Deleted Successfully", id=id, success=True)
    except Exception as e:
        return jsonify(error=str(e)), 500


@app.route("/tasks/<id>", methods=["PUT"])
@token_required
def update_task(current_user_id,id: str):
    
    try:
        update_data = {
            "title": request.json["title"],
            "description": request.json["description"],
            "completed": request.json.get("completed", False)
        }
        db.update_one({"_id": ObjectId(id),"user_id": current_user_id}, {"$set": update_data})
        return jsonify(message="task updated successfully", id=id, success=True)
    except Exception as e:
        return jsonify(error=str(e)), 500


if __name__ == "__main__":
    app.run(debug=True, port=int(config.PORT))
