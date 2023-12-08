DATABASE_USERNAME = 'admin'
DATABASE_PASSWORD = 'secretpassword'
API_KEY = 'myapikey'
DEBUG_MODE = True

def connect_to_database():
    print(f"""Connecting to database with username: 
          {DATABASE_USERNAME}, password: {DATABASE_PASSWORD}
            """)

def make_api_request():
    print(f"Making API request with API key: {API_KEY}")

if __name__ == "__main__":
    if DEBUG_MODE:
        print("Debug mode is enabled.")
    
    connect_to_database()
    make_api_request()