import pymongo

def insertData( hostIPAddress , dbName , collectionName , documents ):
            
    client = pymongo.MongoClient("mongodb://" + hostIPAddress + "/")
    target = client[dbName][collectionName]

    target.insert_many( documents )
