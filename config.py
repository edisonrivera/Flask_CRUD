from dotenv import load_dotenv
import os
load_dotenv()
user = os.environ['MYSQL_USER']
password = os.environ['MYSQL_PASSWORD']
host = os.environ['MYSQL_HOST']
database = os.environ['MYSQL_DATABASE']

path_connection = f"mysql://{user}:{password}@{host}/{database}"