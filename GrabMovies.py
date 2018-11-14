import os, sqlite3, http.client

conn = http.client.HTTPSConnection("api.themoviedb.org")

payload = "{}"

conn.request("GET", "/3/movie/%7Bmovie_id%7D/release_dates?api_key=%3C%3Capi_key%3E%3E", payload)

res = conn.getresponse()
data = res.read()

print(data)
