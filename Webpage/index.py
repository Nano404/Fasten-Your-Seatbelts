#!/usr/bin/python

# Turn on debug mode.
import cgitb
import cgi
cgitb.enable()

form = cgi.FieldStorage()
ip = form.getvalue("ip")
tnumber = form.getvalue("tnumber")
fname = form.getvalue("fname")
sname = form.getvalue("sname")

# Print necessary headers.
print("Content-Type: text/html")
print()

# Connect to the database.
import pymysql
conn = pymysql.connect(
    db='corendon',
    user='admin',
    passwd='W@chtw00rd123',
    host='localhost',
    port=3306)

c = conn.cursor()

# Insert entered form data into database
insertQuery = """INSERT INTO `corendon`.`Attempt` (`ticketnumber`, `ipAddr`,  `fname`, `lname`)
                VALUES(%s, %s, %s, %s)"""
insertVar = (tnumber, ip, fname, sname)
c.execute(insertQuery, insertVar)

conn.commit()

