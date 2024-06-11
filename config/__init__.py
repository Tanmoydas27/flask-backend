from dotenv import load_dotenv
import os

load_dotenv()  

MONGO_URI = os.getenv("MONGO_URI")
GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")
PORT = os.getenv("PORT")
FONTEND_API  = os.getenv("FONTEND_API ")


config = {
    "MONGO_URI": MONGO_URI,
    "GOOGLE_CLIENT_ID": GOOGLE_CLIENT_ID,
    "GOOGLE_CLIENT_SECRET" : GOOGLE_CLIENT_SECRET,
    "PORT" : PORT,
    "FONTEND_API": FONTEND_API 
}