from module_lingkaran import rumus_lingkaran
from module_segitiga import segitiga

# tampilan awal
print("Pilih bangun ruang yang akan dihitung")
print("1. Lingkaran")
print("2. Segitiga")
print("-------------------------------------")

# proses pemiliihan dan inputan user
pilih = input("Pilih (1/2) : ")
if pilih == "1":
    jari_jari = int(input("Masukkan nilai jari - jari : "))
    hasil = rumus_lingkaran(jari_jari)
    
elif pilih == '2':
    alas = int(input("Masukkan nilai alas : "))
    tinggi = int(input("Masukkan nilai tinggi : "))
    luas = segitiga(alas,tinggi)
