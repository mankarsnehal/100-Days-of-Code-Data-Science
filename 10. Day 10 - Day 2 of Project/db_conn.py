import mysql.connector

conn = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'snehal21',
    database = 'bank_management'
)

my_cursor = conn.cursor()