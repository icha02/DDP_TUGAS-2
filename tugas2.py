nama_pembeli = input("Masukkan Nama: ")
print("Pilih Produk:")
print("[1]Kipas Angin")
print("[2]TV")
print("[3]Mesin Cuci")
print("[4]AC")
print("[5]Kulkas")

pilihan = int(input("pilihan :"))
if pilihan == 1:
    nama_produk = "Kipas Angin"
    harga_kotor = 1000000
elif pilihan == 2:
    nama_produk = "TV"
    harga_kotor = 2000000
elif pilihan == 3:
    nama_produk = "Mesin Cuci"
    harga_kotor = 3000000
elif pilihan == 4:
    nama_produk = "AC"
    harga_kotor = 4000000
elif pilihan == 5:
    nama_produk = "Kulkas"
    harga_kotor = 5000000
else:
    harga = 0
jumlah_beli = int(input("Jumlah Beli :"))

if pilihan == 1 and jumlah_beli >= 5:
    diskon = harga_kotor * (20/100)
elif pilihan == 4 and jumlah_beli >= 3:
    diskon = harga_kotor * (10/100)
else:
    diskon = harga_kotor * (5/100)

ppn = (harga_kotor - diskon) * (10/100)

harga_bersih = harga_kotor - diskon + ppn

print("============")
print("Nama Pelanggan :", nama_pembeli)
print("Produk Pilihan :", nama_produk)
print("Harga Produk :", harga_kotor)
print("Diskon :", diskon)
print("PPN :", ppn)
print("Harga Bersih :", harga_bersih)
