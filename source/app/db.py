import mysql.connector
from availability import *


dbHost = 'localhost'
dbUser = 'smartSpaceUser'
dbPassword = 'Aa1.aaaaaa'
dbName = 'smart_space'

db = mysql.connector.connect(
    host = dbHost,
    user = dbUser,
    password = dbPassword,
)
sqlCursor= db.cursor()


def setup():
    sqlCursor.execute('CREATE DATABASE IF NOT EXISTS smart_space')
    sqlCursor.execute('USE smart_space')
    sqlCursor.execute('CREATE TABLE IF NOT EXISTS availability (id INT AUTO_INCREMENT PRIMARY KEY, timestamp DATETIME, freeSlots INT, usedSlots INT)')

def addAvailability(availability: Availability):
    sqlCursor.execute('INSERT INTO availability (timestamp, freeSlots, usedSlots) VALUES (%s, %s, %s)', (availability.timestamp, availability.freeSlots, availability.usedSlots))
    db.commit()

setup()