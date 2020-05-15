import pymongo
from funcDeleteData import *
from funcInsertData import *

with open('../app/ip.txt', 'r') as file:
    hostIPAddress = file.read().replace('\n', '')

dbName = "testDB"
collectionName = "authTable"

auth1 = { "username":"admin" , "password":"admin" } 
auth2 = { "username":"test" , "password":"test" }

insertlist = [ auth1 , auth2 ]

deleteData( hostIPAddress , dbName , collectionName )

insertData( hostIPAddress , dbName , collectionName , insertlist )

print("Done!")