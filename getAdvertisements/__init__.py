import azure.functions as func
import pymongo
import json
from bson.json_util import dumps

def main(req: func.HttpRequest) -> func.HttpResponse:

    try:
        url = "mongodb://myneighborlybd:YUHgrd8EDy9IkTdgbEkqz6QVDuuq6z3Qno4o0iH5K8UyyuYdE0RNADdQ8Og9EXKU5cjUbj6JxxuvgWwwkpGY1w==@myneighborlybd.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@myneighborlybd@"  # TODO: Update with appropriate MongoDB connection information
        client = pymongo.MongoClient(url)
        database = client['myneighborlybd']
        collection = database['advertisements']


        result = collection.find({})
        result = dumps(result)

        return func.HttpResponse(result, mimetype="application/json", charset='utf-8')
    except:
        print("could not connect to mongodb")
        return func.HttpResponse("could not connect to mongodb",
                                 status_code=400)

