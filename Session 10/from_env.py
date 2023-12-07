import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Updated code using environment variables

DATABASE_USERNAME = os.getenv('DATABASE_USERNAME', 'admin')
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')
API_KEY = os.getenv('API_KEY', 'myapikey')
DEBUG_MODE = os.getenv('DEBUG_MODE').lower() in ('true', 't', 'y', 'yes')

def connect_to_database():
    print(f"Connecting to database with username: {DATABASE_USERNAME}, password: {DATABASE_PASSWORD}")

def make_api_request():
    print(f"Making API request with API key: {API_KEY}")

if __name__ == "__main__":
    if DEBUG_MODE:
        print("Debug mode is enabled.")
    
    connect_to_database()
    make_api_request()
