# !/usr/bin/env python3

# Virgil Anderson
# Project: Logs Analysis

import datetime
import psycopg2


# DB Query Function
def connect(query):
    DBNAME = "news"
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(query)
    results = c.fetchall()
    db.close()
    return(results)


# Most popular 3 article query
def get_article():
    query = ("SELECT title, count(*) AS num FROM articles JOIN log "
             "ON log.path LIKE concat('%', articles.slug) "
             "GROUP BY articles.title ORDER BY num DESC limit 3")
    ARTICLE = connect(query)
    return(ARTICLE)


# Top authors query
def get_author():
    query = ("SELECT authors.name, count(*) AS num "
             "FROM (articles JOIN log ON log.path "
             "LIKE concat('%', articles.slug)) AS pop_art "
             "JOIN authors ON pop_art.author = authors.id "
             "GROUP BY authors.name ORDER BY num DESC")
    AUTHOR = connect(query)
    return(AUTHOR)


# Days with error over 1 percent query
def get_error():
    query = ("SELECT time, Percent "
             "FROM (select daily_err.time, "
             "daily_err.errors, daily_que.queries, "
             "ROUND(daily_err.errors * 100.0 / daily_que.queries, 1) "
             "AS Percent FROM daily_err JOIN daily_que ON daily_err.time "
             " = daily_que.time) AS days WHERE Percent >= 1")
    ERROR = connect(query)
    return(ERROR)


# Store queries in variables
AUTHOR = get_author()
ARTICLE = get_article()
ERROR = get_error()

# Print the query information to the console
# Top article query
print("Top 3 Articles: \n")
for ARTICLE in ARTICLE:
    a = str(ARTICLE[0])
    b = str(ARTICLE[1])
    article = (a, ", ", b, " views")
    x = ''.join(article)
    print(x)

# Top author query
print("\nMost Popular Authors: \n")
for AUTHOR in AUTHOR:
    c = str(AUTHOR[0])
    d = str(AUTHOR[1])
    author = (c, ", ", d, " views")
    y = ''.join(author)
    print(y)

# Days with an error rate > 1% query
print("\nDays with error rate > 1%: \n")
for ERROR in ERROR:
    x = ERROR[0]
    month = str(x.strftime("%b"))
    day = str(x.strftime("%d"))
    year = str(x.strftime("%Y"))
    date = (month, day, year)
    e = ' '.join(date)
    f = str(ERROR[1])
    error = (e, ", ", f, "% error")
    z = ''.join(error)
    print(z)
