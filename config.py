import os
from dotenv import load_dotenv

# Load the environment variables
load_dotenv()

# Access the environment variables
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
