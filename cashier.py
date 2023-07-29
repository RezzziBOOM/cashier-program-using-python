import datetime

print("----------------- SELAMAT DATANG -----------------")
print("==================================================")
print("----------- PROGRAM CASHIER REZZI BOOM -----------")

kasir = input("Masukkan Nama Kasir: ")
id_kasir = int(input("Masukkan Id Kasir: "))

def sapa(kasir):
    print("\n\t------ Hai " + kasir + ". Selamat menjadi kasir ------\n\t")

sapa(kasir)

pembeli = input("Masukkan nama Pembeli: ")

def fungsimakanan():
    pesanan_makanan = []

    print("""
================================================
                PROGRAM KASIR 
                    REZZZ
================================================
Kode |      Menu Makanan     |       Harga      |
-------------------------------------------------
1.       Lele Goreng        Rp.20.000
2.       Ayam Goreng        Rp.20.000
3.       Ayam Bakar         Rp.20.000
4.       Nasi               Rp.5.000
=================================================
""")
    while True:
        nomor = int(input("Masukkan Pilihan: "))
        porsi = int(input("Masukkan Jumlah Porsi: "))

        if nomor == 1:
            totalmkn = porsi * 20000
            print(porsi, " Porsi Lele Goreng = Rp", totalmkn)
            jenis_mkn = "Lele Goreng"
        elif nomor == 2:
            totalmkn = porsi * 20000
            print(porsi, " Porsi Ayam Goreng = Rp", totalmkn)
            jenis_mkn = "Ayam Goreng"
        elif nomor == 3:
            totalmkn = porsi * 20000
            print(porsi, " Porsi Ayam Bakar = Rp", totalmkn)
            jenis_mkn = "Ayam Bakar"
        elif nomor == 4:
            totalmkn = porsi * 5000
            print(porsi, " Porsi Nasi = Rp", totalmkn)
            jenis_mkn = "Nasi"
        else:
            print("Pilihan tidak ada, silakan masukkan lagi!!")
            continue

        pesanan_makanan.append((jenis_mkn, porsi, totalmkn))

        lanjut = input('Tambah pesanan makanan? (y/n): ')
        if lanjut == 'n':
            break

    return pesanan_makanan


def fungsiminuman():
    pesanan_minuman = []

    print("""
================================================
               
================================================
Kode |      Menu Minuman      |       Harga      |
-------------------------------------------------
1.       Es Teh Manis        Rp.5.000
2.       Es Jeruk            Rp.5.000
3.       Es Kelapa           Rp.5.000
4.       Es Mangga           Rp.5.000
=================================================
""")
    while True:
        nomor = int(input("Masukkan Pilihan: "))
        gelas = int(input("Masukkan Jumlah Gelas: "))

        if nomor == 1:
            totalmnm = gelas * 5000
            print(gelas, " Gelas Es Teh Manis = Rp", totalmnm)
            jenismnm = "Es Teh Manis"
        elif nomor == 2:
            totalmnm = gelas * 5000
            print(gelas, " Gelas Es Jeruk = Rp", totalmnm)
            jenismnm = "Es Jeruk"
        elif nomor == 3:
            totalmnm = gelas * 5000
            print(gelas, " Gelas Es Kelapa = Rp", totalmnm)
            jenismnm = "Es Kelapa"
        elif nomor == 4:
            totalmnm = gelas * 5000
            print(gelas, " Gelas Es Mangga = Rp", totalmnm)
            jenismnm = "Es Mangga"
        else:
            print("Pilihan tidak ada, silakan masukkan lagi!!")
            continue

        pesanan_minuman.append((jenismnm, gelas, totalmnm))

        lanjut = input('Tambah pesanan minuman? (y/n): ')
        if lanjut == 'n':
            break

    return pesanan_minuman


pesan_makanan = input("Apakah Anda ingin memesan makanan? (y/n): ")
pesan_minuman = input("Apakah Anda ingin memesan minuman? (y/n): ")

pesanan_makanan = []
pesanan_minuman = []

if pesan_makanan.lower() == 'y':
    pesanan_makanan = fungsimakanan()

if pesan_minuman.lower() == 'y':
    pesanan_minuman = fungsiminuman()

totalsemua = sum([harga for _, _, harga in pesanan_makanan + pesanan_minuman])

print("\nTotal harus Dibayar: Rp", totalsemua)
uang = int(input("Uang Tunai Pembeli: Rp "))
kembalian = int(uang - totalsemua)
print("Kembalian :", kembalian)
tanggal_sekarang = datetime.datetime.now()

print("\n==================================")
print("============== C E T A K ===============")
print("========== S T R U K   B E L I =========")
print("Nama Kasir\t:", kasir)
print("Id Kasir\t:", id_kasir)
print("==================================")
print("==================================")
print("Pembeli\t\t:", pembeli)
print("Tanggal\t\t:", tanggal_sekarang.strftime("%Y-%m-%d %H:%M:%S"))
print("==================================")
print("==================================")

if pesan_makanan.lower() == 'y':
    print("Beli Makanan:")
    for makanan in pesanan_makanan:
        print(f"{makanan[1]} Porsi {makanan[0]} (Rp{makanan[2]})")

print("==================================")
print("==================================")

if pesan_minuman.lower() == 'y':
    print("Beli Minuman:")
    for minuman in pesanan_minuman:
        print(f"{minuman[1]} Gelas {minuman[0]} (Rp{minuman[2]})")

print("==================================")
print("==================================")

print("Total Bayar\t: Rp", totalsemua)
print("Dibayar\t\t: Rp", uang)
print("Kembalian\t: Rp", kembalian)
print("==================================")
print("==================================")
print("== ======== T E R I M A K A S I H =========")