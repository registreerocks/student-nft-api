from os import environ as env

import pymongo

def _health_check():
    try:
        client = pymongo.MongoClient(
            'mongodb://mongodb:27017/', 
            username=env.get('MONGO_USERNAME'), 
            password=env.get('MONGO_PASSWORD'),
            serverSelectionTimeoutMS=1
        )
        client.server_info()
        return {
            "status": "ok",
            "info": {
                "mongo-link": {
                    "status": "up"
                }
            },
            "error": {},
            "details": {
                "mongo-link": {
                    "status": "up"
                }
            }
        }, 200
    except pymongo.errors.ServerSelectionTimeoutError as err:
        return {
            "status": "error",
            "info": {},
            "error": {
                "mongo-link": {
                    "status": "down"
                }
            },
            "details": {
                "mongo-link": {
                    "status": "down"
                }
            }
        }, 503