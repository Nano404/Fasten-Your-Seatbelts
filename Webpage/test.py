#!/usr/bin/python

# Turn on debug mode.
import cgitb
import cgi
cgitb.enable()

#Variables from the form
#form = cgi.FieldStorage()
#ip = form.getvalue("ip")
#tnumber = form.getvalue("tnumber")
#fname = form.getvalue("fname")
#sname = form.getvalue("sname")

# Print necessary headers.
print("Content-Type: text/html")
print()

# Connect to the database.
import pymysql
conn = pymysql.connect(
    db='corendon',
    user='nino',
    passwd='W@chtw00rd123',
    host='localhost',
    port=3306)

c = conn.cursor()

#Check if user excists

checkQuery = """SELECT ticketnummer, voornaam, achternaam FROM User
WHERE ticketnummer="123532" AND voornaam="Nino" AND achternaam="snoek";"""
test=c.execute(checkQuery)
if test != 0:
    print("logged In!! Click here to get redirected to the homepage 192.168.1.55")
else:
    print("Try again")
print (c.fetchall())

conn.commit()
