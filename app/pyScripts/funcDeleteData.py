import pymongo

def deleteData( hostIPAddress , dbName , collectionName ):
            
    client = pymongo.MongoClient("mongodb://" + hostIPAddress + "/")
    target = client[dbName][collectionName]

    target.delete_many({})
