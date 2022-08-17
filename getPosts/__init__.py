import logging
import azure.functions as func
import pymongo
import json
from bson.json_util import dumps


def main(req: func.HttpRequest) -> func.HttpResponse:

    logging.info('Python getPosts trigger function processed a request.')

    try:
        url = "mongodb://myneighborlybd:YUHgrd8EDy9IkTdgbEkqz6QVDuuq6z3Qno4o0iH5K8UyyuYdE0RNADdQ8Og9EXKU5cjUbj6JxxuvgWwwkpGY1w==@myneighborlybd.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@myneighborlybd@"  # TODO: Update with appropriate MongoDB connection information
        client = pymongo.MongoClient(url)
        database = client['myneighborlybd']
        collection = database['posts']

        result = collection.find({})
        result = dumps(result)

        return func.HttpResponse(result, mimetype="application/json", charset='utf-8', status_code=200)
    except:
        return func.HttpResponse("Bad request.", status_code=400)