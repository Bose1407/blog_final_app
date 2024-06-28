import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, "C:\Users\boseb\OneDrive\Desktop\app")  # Replace with the actual path to your application directory

from app import app as application  # Assuming your Flask app instance is named 'app' in app.py

application.secret_key = '5791628bb0b13ce0c676dfde280ba245'  # Replace with your actual secret key
