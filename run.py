# run.py
import os
from app import create_app
from dotenv import load_dotenv
from app.onboarding import onboard_users

load_dotenv()  # Load environment variables from .env file

app = create_app()

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)