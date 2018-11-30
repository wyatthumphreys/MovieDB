import os, sqlite3, http.client

#conn = sqlite3.connector.connect(user='root', password='',
                    #              host='127.0.0.1',
                     #             database='MovieDB')
#cursor = conn.cursor()
#cursor.execute('''CREATE TABLE IF NOT EXISTS Movies (id INT PRIMARY KEY AUTO_INCREMENT, Vote_Average TEXT, Title TEXT, Release_Date TEXT, Description TEXT, Company TEXT, Apply_info TEXT, Salary FLOAT, RawMessage TEXT, Github_ID TEXT); ''')

connect = http.client.HTTPSConnection("api.themoviedb.org")

payload = "{}"

connect.request("GET", "/3/discover/movie?page=1&include_video=false&include_adult=false&sort_by=popularity.desc&language=en-US&api_key=INSERTAPIKEY", payload)

#GET GENRES BELOW
#connect.request("GET", "/3/genre/movie/list?language=en-US&api_key=INSERTAPIKEYHERE", payload)

res = connect.getresponse()
data = res.read()

print(data)

#GENRE LIST
#b'{"id":28,"name":"Action"}' \
#'{"id":12,"name":"Adventure"}' \
#'{"id":16,"name":"Animation"}' \
#'{"id":35,"name":"Comedy"}' \
#'{"id":80,"name":"Crime"}' \
#'{"id":99,"name":"Documentary"}\
#"id":18,"name":"Drama"}' \
#'{"id":10751,"name":"Family"}' \
#'{"id":14,"name":"Fantasy"}' \
#'{"id":36,"name":"History"}' \
#'{"id":27,"name":"Horror"}' \
#'{"id":10402,"name":"Music"}' \
#'{"id":9648,"name":"Mystery"}' \
#'{"id":10749,"name":"Romance"}' \
#'{"id":878,"name":"Science Fiction"}' \
#'{"id":10770,"name":"TV Movie"}' \
#'{"id":53,"name":"Thriller"}' \
#'{"id":10752,"name":"War"}' \
#'{"id":37,"name":"Western"}]}'



for page in data:
    print(page['title'])
    #cursor.execute('''INSERT INTO Jobs (PostDate, Title, Location, Description, Company, Apply_info) VALUES (
    #"''' + page['created_at'] + '''",
    #"''' + page['title'] + '''",
    #"''' + page['location'] + '''",
    #"''' + page['description'] + '''",
    #"''' + page['company'] + '''",
    #"''' + page['how_to_apply'] + '''")''')
