import os

# General Flask app settings
DEBUG = os.environ.get('DEBUG', None)
SECRET_KEY = os.environ.get('SECRET_KEY', None)
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', None)

# Redis connection
REDIS_SERVER = os.environ.get('REDIS_SERVER', '127.0.0.1')
REDIS_PORT = os.environ.get('REDIS_PORT', 6379)
REDIS_DB = os.environ.get('REDIS_DB', 0)

# Twilio API credentials
TWILIO_ACCOUNT_SID = os.environ.get('TWILIO_ACCOUNT_SID', None)
TWILIO_AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN', None)
TWILIO_NUMBER = os.environ.get('TWILIO_NUMBER', '+17707286825')
