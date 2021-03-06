#Wyatt Humphreys | wlhumphreys@student.rtc.edu
#12/6/18 This program grabs data from themoviedb, puts it into a SQL database, and asks what kind of movies you want to watch
#SOURCES: https://stackoverflow.com/questions/42445237/looping-through-a-json-array-in-python
import mysql.connector
import sys
import json
import urllib.request
import os
import time

#Creates and setsup SQL DB. Setup so no movie can be accidently added twice.
conn = mysql.connector.connect(user='root', password='',
                                  host='127.0.0.1',
                                  database='MovieDB',
                               buffered = True)
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS Movies (id INT PRIMARY KEY AUTO_INCREMENT, Vote_Average TEXT, Title TEXT, Release_Date TEXT, Overview TEXT); ''')

#Query the website
query = "https://api.themoviedb.org/3/discover/movie?page=1&include_video=false&include_adult=false&sort_by=popularity.desc&language=en-US&api_key="
jsonpage = 0
contents = urllib.request.urlopen(query)
response = contents.read()
jsonpage = json.loads(response)
#Put the data into the DB
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

#Get ready for questions
cursor.execute("SELECT Title,vote_average FROM Movies WHERE vote_average<=5.9;")
Q1Bad = cursor.fetchall()
cursor.execute("SELECT Title,vote_average FROM Movies WHERE vote_average>=6.0 && vote_average<=7.0;")
Q1Good = cursor.fetchall()
cursor.execute("SELECT Title,vote_average FROM Movies WHERE vote_average>=7.1;")
Q1Great = cursor.fetchall()

#Ask the questions
Q1 = input("Looking for a bad movie, a good movie, or a great movie? Bad = 0, Good = 1, Great = 2 ")
if Q1 == "0":
    print("You will be shown bad movies: ")
    for x in Q1Bad:
        print(x)
elif Q1 == "1":
    print("You will be shown good movies: ")
    for x in Q1Good:
        print(x)
elif Q1 == "2":
    print("You will be shown great movies: ")
    for x in Q1Great:
        print(x)
else:
    print("Because your input was invalid, you will be shown Great movies:  ")
    for x in Q1Great:
        print(x)