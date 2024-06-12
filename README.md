# Flask Backend for Your Project

This Flask backend serves as the server-side component for your project. It provides RESTful APIs for managing tasks and authentication.

## Installation

### Prerequisites

- Python 3.7 or higher
- MongoDB installed and running locally or remotely

### Clone the Repository

```bash
git clone <repository_url>
cd <repository_name>
```
open the Directory 

the create a '.env. file for Enviroment variables  and add:-
```bash
MONGO_URI=mongodb://localhost:27017/TO-DO-LIST
GOOGLE_CLIENT_ID=12987315580-r5piiplf6vmlmebdc3dpgtbhn9uc8d9f.apps.googleusercontent.com
GOOGLE_CLIENT_SECRET=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
PORT=5000
```
```bash
pip install flask 
```
creating a virtual environment
```bash
python -m venv venv
```
Activate the environment
```bash
venv\Scripts\activate
```
run the command for install all the requiremenrs.
```bash
pip install -r requirements.txt
```
Install this dependencies :-
```bash
pip install flask_pymongo flask_cors google-auth-oauthlib google-auth PyJWT python-dotenv

pip install --upgrade Flask
```
Finally run the command :-
```bash
python app.py
```

# Data Storage or database

Use Mongo DB Server to Store the data , You Mongodb compass app in your local machine or change the mognodb url with the mongoDB atlas cluster url 
my cluster is:-
```bash
mongodb+srv://tanmoy1:tanmoy1@cluster0.3foceba.mongodb.net/
```
# Usage

Visit http://localhost:<port_number> / to access the homepage.

Use the provided RESTful APIs to manage tasks and authentication.

# API Documentation

## Authentication

POST /login: Logs in the user using Google OAuth2. Requires a JSON object with a token field containing the Google ID token.

## Task Management
GET /tasks: Retrieves all tasks for the authenticated user.

GET /tasks/<id>: Retrieves a specific task by its ID.

POST /tasks: Creates a new task. Requires a JSON object with title and description fields.

PUT /tasks/<id>: Updates an existing task by its ID. Requires a JSON object with title and description fields.

DELETE /tasks/<id>: Deletes a specific task by its ID.
