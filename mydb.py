
import mysql.connector

database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'password',

)


# Prepare a cursor object
cursorObject = database.cursor()


#create database
cursorObject.execute("CREATE DATABASE nexusco")

print("All Done")