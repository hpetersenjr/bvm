import json , requests
from funcDeleteData import *
from funcInsertData import *
from datetime import datetime

baseURL  = "https://api.covid19api.com/"
dbName = "testDB"
collectionName = "baseDataZA"
documentList = []

with open('../app/ip.txt', 'r') as file:
    hostIPAddress = file.read().replace('\n', '')

with open('allData.txt', 'r') as file:
    data = json.loads(file.read().replace('\n', ''))

for dictItem in data:
    del dictItem['Province']
    del dictItem['City']
    del dictItem['CityCode']
    del dictItem['Lat']
    del dictItem['Lon']
    dictItem['Date'] = datetime.strptime( dictItem['Date'] , '%Y-%m-%dT%H:%M:%SZ')

for dictItem in data:
    if dictItem['CountryCode'] == 'ZA':
        documentList.append( dictItem )

deleteData( hostIPAddress , dbName , collectionName )

insertData( hostIPAddress , dbName , collectionName , documentList )

print("Done!")

