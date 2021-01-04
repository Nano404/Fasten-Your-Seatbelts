#!/usr/bin/python
import secrets
import cgitb
import cgi
import datetime
import pymysql

#Debug console only for test purposes else comment out
cgitb.enable()

#Variables from the form
form = cgi.FieldStorage()
mac = form.getvalue("mac")
ip = form.getvalue("ip")
tnumber = form.getvalue("tnumber")
fname = form.getvalue("fname")
sname = form.getvalue("sname")

# Print necessary headers.
print("Content-Type: text/html")
print()

# Connect to the database
conn = pymysql.connect(
    db=secrets.database,
    user=secrets.username,
    passwd=secrets.password,
    host='localhost',
    port=3306)
c = conn.cursor()

#Insert entered form data into database
time = datetime.datetime.now()
insertQuery = """INSERT INTO `corendon`.`Attempt` (`ticketnumber`, `macAddress`, `ipAddress`, `firstName`, `lastName` $VALUES(%s, %s, %s, %s, %s, %s)"""
insertVar = (tnumber, mac, ip, fname, sname, time.strftime("%d/%m/%Y %H:%M"))
c.execute(insertQuery, insertVar)


#Check if user exists
checkQuery = """SELECT * FROM `User` WHERE `ticketnumber` = %s AND `firstName` = %s AND `lastName` = %s"""
checkVar = (tnumber, fname, sname)
c.execute(checkQuery, checkVar)
conn.commit() #commits the 2 database queries
checkUser = c.fetchone()

def iptable(x):
    import os
    os.system('sudo iptables -t mangle -I internet 1 -m mac --mac-source {} -j RETURN'.format(x))

#if checkUser is equal to None spit out an error
if checkUser == None:
    print(secrets.error)
else:
    iptable(mac)
    print(secrets.success)
