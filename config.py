import os
from dotenv import load_dotenv

load_dotenv()

db_host = os.environ.get('DB_HOST', default='localhost')
db_name = os.environ.get('DB_NAME', default='notes')
db_user = os.environ.get('DB_USERNAME', default='notes')
db_password = os.environ.get('DB_PASSWORD', default='')
db_port = os.environ.get('DB_PORT', default='5432')

# we put the false for track modifications, because we dont want warnings about it in the output
SQLALCHEMY_TRACK_MODIFICATIONS = False

SQLALCHEMYDATABASEURI = f"postgres://{db_user}:{db_password}@{db_name}:{db_port}/{db_name}"

