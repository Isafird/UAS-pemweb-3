import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    db = "muhamad_isa_firdaus"
)

cursor = mydb.cursor()
sql1 = """Create Table anime(tahun Varchar(10) Primary Key, judul Varchar(40), genre Varchar(20), studio Varchar(20))"""
sql2 = """Create Table buku(tahun_terbit Varchar(10) Primary Key, judul_buku Varchar(30), genre_buku Varchar(20), penerbit Varchar(20))"""

cursor.execute(sql1)
cursor.execute(sql2)

print("Tabel berhasil dibuat")