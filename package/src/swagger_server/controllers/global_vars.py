from os import environ as env

from pymongo import MongoClient

CLIENT = MongoClient(
  'mongodb://mongodb:27017/', 
  username=env.get('MONGO_USERNAME'), 
  password=env.get('MONGO_PASSWORD')
  )
DB = CLIENT.database
JOIN = DB.joining_db

INFURA_KEY = env.get("INFURA_KEY", 'somekey')
PRIVATE_KEY = env.get("PRIVATE_KEY", '1f7ca3635605bc57b579b5fdf73e3ac84aa91a9c8eddc57aa0e3452d1a429ff8')