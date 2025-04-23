# ini adalah function
def sapa():
    print("Halo, selamat datang!")

sapa()  # Memanggil fungsi
sapa()  # memanggil kedua kali
sapa()  # memanggil ketiga kali,dst

# fungsi dengan parameter
# function dengan parameter
# function dengan 1 parameter
def sapa_nama(nama):
    print(f"Halo, {nama}!")

# Pemanggilan Function
sapa_nama("diky")
sapa_nama("diky")
sapa_nama("diky")

# function dengan lebih dari 1 parameter
def luas_segitiga(alas, tinggi):
    luas = (alas * tinggi) / 2
    print("Luas segitiga: %f" % luas)

# Pemanggilan Function
luas_segitiga(4, 6)
luas_segitiga(3, 5)
luas_segitiga(2, 4)

# function dengan nilai kembali (return)
def tambah(a, b):
    return a + b

# pemanggilan fungsi
hasil = tambah(3, 5)
print("Hasil:", hasil)

# menggunakan fungsi di dalam fungsi
# rumus sisi x sisi
def luas_persegi(sisi):
    luas = sisi * sisi
    return luas


# rumus: sisi x sisi x sisi
def volume_persegi(sisi):
    volume = luas_persegi(sisi) * sisi
    return volume

# pemanggilan fungsi
vol_persegi = volume_persegi(6)
print(f"Volume Persegi = {vol_persegi}")

def student(firstname, lastname ='Mark', standard ='Fifth'):
    print(firstname, lastname, 'studies in', standard, 'Standard')

# memanggil fungsi dengan 1 parameter
student("diky")
# pemanggilan function, dengan 3 argumen
student('John', 'Gates', 'Seventh')

def kali(a: int, b: int) -> int:
    return a * b

# Pemanggilan function
print("Hasil = " ,kali(3, 4))
print("Tipe Data : ", type(kali(3,4)))

