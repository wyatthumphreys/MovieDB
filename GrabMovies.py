#SOURCES: https://stackoverflow.com/questions/42445237/looping-through-a-json-array-in-python
import mysql.connector
import sys
import json
import urllib.request
import os
import time


conn = mysql.connector.connect(user='root', password='',
                                  host='127.0.0.1',
                                  database='MovieDB',
                               buffered = True)
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS Movies (id INT PRIMARY KEY AUTO_INCREMENT, Vote_Average TEXT, Title TEXT, Release_Date TEXT, Overview TEXT); ''')

query = "https://api.themoviedb.org/3/discover/movie?page=1&include_video=false&include_adult=false&sort_by=popularity.desc&language=en-US&api_key=6a16db157e43a17b6576a257990c575f"
jsonpage = 0
contents = urllib.request.urlopen(query)
response = contents.read()
jsonpage = json.loads(response)
for i in jsonpage['results']:
    title = i['title']
    cursor.execute("SELECT Title FROM Movies WHERE Title = '" + title + "';")
    test = cursor.rowcount
    if test != 1:
        cursor.execute('''INSERT INTO Movies (Vote_Average, Title, Release_Date, Overview) VALUES (
        "''' + str(i['vote_average']) + '''",
        "''' + i['title'] + '''",
        "''' + i['release_date'] + '''",
        "''' + i['overview'] + '''")''')

    else:
        continue

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



#Q1 = input("Looking for a bad movie, a good movie, or a great movie? Bad = 0, Good = 1, Great = 2 ")
#if Q1 == 0:
    #Q1Bad = cursor.execute('''SELECT * FROM Movies WHERE vote_average<=5.9;''')