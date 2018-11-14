import os, sqlite3, http.client


connect = http.client.HTTPSConnection("api.themoviedb.org")

payload = "{}"

connect.request("GET", "/3/discover/movie?page=1&include_video=false&include_adult=false&sort_by=popularity.desc&language=en-US&api_key=INSERTAPIKEYHERE", payload)

res = connect.getresponse()
data = res.read()

print(data)