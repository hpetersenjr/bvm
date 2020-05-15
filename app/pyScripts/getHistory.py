import requests

baseURL  = "https://api.covid19api.com/"
apiUrl = baseURL + "all"
documents = requests.get( apiUrl )#.json()
filename = "allData.txt"
chunk_size = 100

with open( filename, 'wb' ) as fd:
    for chunk in documents.iter_content( chunk_size ):
        fd.write( chunk )