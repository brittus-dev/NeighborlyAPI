import azure.functions as func
import pymongo
import json
from bson.json_util import dumps
from bson.objectid import ObjectId

def main(req: func.HttpRequest) -> func.HttpResponse:

    id = req.params.get('id')

    if id:
        try:
            url = "mongodb://myneighborlybd:YUHgrd8EDy9IkTdgbEkqz6QVDuuq6z3Qno4o0iH5K8UyyuYdE0RNADdQ8Og9EXKU5cjUbj6JxxuvgWwwkpGY1w==@myneighborlybd.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@myneighborlybd@"  # TODO: Update with appropriate MongoDB connection information
            client = pymongo.MongoClient(url)
            database = client['myneighborlybd']
            collection = database['posts']

            query = {'_id': ObjectId(id)}
            result = collection.find_one(query)
            result = dumps(result)

            return func.HttpResponse(result, mimetype="application/json", charset='utf-8')
        except:
            return func.HttpResponse("Database connection error.", status_code=500)

    else:
        return func.HttpResponse("Please pass an id parameter in the query string.", status_code=400)