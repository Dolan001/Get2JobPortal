import os

MONGO_DBNAME = 'get2job'

MONGO_URL = os.environ.get('MONGO_URL')
if not MONGO_URL:
    MONGO_URL = "mongodb://localhost:27017/get2job"

MONGO_URI = MONGO_URL