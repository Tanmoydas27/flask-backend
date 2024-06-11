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

python3 -m venv venv


venv\Scripts\activate


pip install -r requirements.txt


MONGO_URI=<your_mongodb_uri>
GOOGLE_CLIENT_ID=<your_google_client_id>
GOOGLE_CLIENT_SECRET=<your_google_client_secret>
PORT=<port_number>


python app.py
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