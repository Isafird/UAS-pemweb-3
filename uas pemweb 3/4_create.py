import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    db = "muhamad_isa_firdaus"
)

cursor = mydb.cursor()
sql1 = "Insert Into anime (tahun, judul, genre, studio) Values (%s, %s, %s, %s)"
val1 = [("2024", "Demon Slayer: Hashira Training Arc", "Aksi", "Ufotable"), ("2023", "Frieren: Beyond Journey's End", "Fantasi", "Madhouse"), ("2022", "Chainsaw Man", "Aksi", "MAPPA"), ("2021", "Mushoku Tensei: Jobless Reincarnation", "petualangan", "Bind")]

sql2 = "Insert Into buku (tahun_terbit, judul_buku, penulis, penerbit) Values (%s, %s, %s, %s)"
val2 = [("2011", "Hujan Kepagian", "Nugroho Notosusanto", "Balai Pustaka"), ("2002", "Sangkuriang", "Yuliadi Soekardi", "CV. Pustaka Setia"), ("2008", "Sang Pemimpi", "Andrea Hirata", "PT. Bentang Pustaka"), ("2009", "Negeri 5 Menara", "Ahmad Fuadi", "PT. Gramedia Pustaka Utama")]

for x in val1:
    cursor.execute(sql1, x)

for x in val2:
    cursor.execute(sql2, x)

mydb.commit()
print("Data berhasil ditambahkan")