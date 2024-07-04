import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = ""
)

cursor = mydb.cursor()
cursor.execute("Create Database muhamad_isa_firdaus")

print("Database berhasil dibuat")