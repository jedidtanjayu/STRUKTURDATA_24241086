# 1. Tipe Data Numerik (Numeric Types)
# Integer (int)
x = 10
y = -200
z = 0
print(type(x))  # <class 'int'>
print(type(y))  # <class 'int'>
print(type(z))  # <class 'int'>

# ciri khas lainnya dari tipe data numerik adalah :
# operator penjumlahan untuk tipe data integer
a1 = 5
a2 = -180

a3 = a1 + a2
print(a3)
print(type(a3))

# Float (float)
# Tipe data float
a = 3.141592
b = -0.001
c = 1.0
d = float('inf') # memasukkan infinity sebagai float

# melihat isi variabel
print(a)
print(b)
print(c)
print(d)

# cek tipe data dari variabel
print(type(a))  # <class 'float'>
print(type(b))  # <class 'float'>
print(type(c))  # <class 'float'>
print(type(d))  # <class 'float'>

# membandingkan nilai b3 dengan yang lain
if (a < d):
    print('lebih kecil')
else:
    print('lebih besar')

# Operasi aritmatika pada float
print(a + c)
print(b ** a)
print(abs(a))

# hasil operasi aritmatika pada float
float = b * a
print(float)
print(type(float))

# mengubah hasil operasi aritmatika float menjadi integer
print(int(b * a))

# 2. Tipe Data String (str)
a = 'Halo'
b = "Python"
c = """Ini adalah
string multi-baris"""
print(type(a))  # <class 'str'>
print(type(b))  # <class 'str'>
print(type(c))  # <class 'str'>

# indexing dan slicing 
text = "Python"
print(text[0])     # Output: P
print(text[-1])    # Output: n
print(text[0:3])   # Output: Pyt
print(text[:4])    # Output: Pyth
print(text[::2])   # Output: Pto (loncat 2 karakter)

# Operasi penggabungan string
print('Hello ' + 'World')

# Operasi pengulangan string
print('Hi' * 3)

# Operasi Pengecekan string
print('a' in 'data') # menghasilkan boolean (True/False)

# Operasi panjang string
print(len('Python'))

# Fungsi dalam String
s = "python programming"
print(s.upper())       # 'PYTHON PROGRAMMING'
print(s.capitalize())  # 'Python programming'
print(s.title())       # 'Python Programming'
print(s.replace("python", "java"))  # 'java programming'
print(s.split())       # ['python', 'programming']
print(s.find("gram"))  # 10

# String Format
# F-String
# String format menggunakan F-String
name = "Adam"
age = 25
print(f"Halo, nama saya {name}, umur saya {age}")
# Format Method
# String format dengan format method
print("Halo, nama saya {}, umur saya {}".format(name, age))
# Cara Membuat List
# membuat list
angka = [1, 2, 3, 4, 5]
buah = ["apel", "jeruk", "mangga"]
campuran = [1, "dua", 3.0, True]
kosong = []

# memanggil list
print(angka)
print(buah)
print(campuran)
print(kosong)

# Indexing dan Slicing
# indexing dan slicing pada list
data = ["a", "b", "c", "d"]
print(data[0])      # Output: a
print(data[-1])     # Output: d
print(data[1:3])    # Output: ['b', 'c']
print(data[:2])     # Output: ['a', 'b']

# Operasi Pada List
# Operasi penambahan anggota list
data = [1, 2, 3, 4, 5]
data = data + [10, 20]
print(data)

# Operasi pengulangan list
list = [1, 2]
list = list * 3
print(list)

# Operasi mengukur panjang list
print(len(data))
print(len(list))

# Operasi mengecek keanggotaan pada list
print(20 in data)
print(13 in list)

# Fungsi pada list
# Fungsi pada list 
a = [3, 1, 4, 1, 5]
print(a)
a.append(9)         # Menambahkan elemen di akhir
print(a)
a.insert(2, 7)      # Menyisipkan angka 7 di indeks ke-2
print(a)
a.remove(1)         # Menghapus elemen pertama yang bernilai 1
print(a)
a.pop()             # Menghapus elemen terakhir
print(a)
a.sort()            # Mengurutkan list secara ascending
print(a)
a.reverse()         # Membalik urutan elemen
print(a)
print(a.index(4))   # Mengembalikan indeks dari nilai 4
print(a.count(1))   # Menghitung jumlah kemunculan angka 1

# List Bersarang (Nested List)
# membuat matriks dari list bersarang
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# memanggil matriks
print(matrix)
# memanggil elemen list pada indeks [1][2]
print(matrix[1][2])  # Output: 6

# Looping List
# Contoh looping list
buah = ["apel", "jeruk", "mangga"]

# For Loop
for item in buah:
    print(item)

# Mengakses indeks dan elemen
for i, item in enumerate(buah):
    print(f"{i}: {item}")

# List Comprehension
# Buat list kuadrat dari 0-9
kuadrat = [x**2 for x in range(10)]
print(kuadrat)  # [0, 1, 4, 9, ..., 81]

# Filter hanya bilangan genap
genap = [x for x in range(10) if x % 2 == 0]
print(genap)  # [0, 2, 4, 6, 8]

# Latihan List
data_mahasiswa = []
jumlah = int(input("Input jumlah mahasiswa: "))
# perulangan untuk memasukkan nama mahasisqa
for i in range(jumlah):
    print(f"\nMahasiswa ke-{i+1}:")
    nama = input("Nama: ")
    nilai = list(map(int, input("Masukkan 3 nilai dipisahkan spasi: ").split()))
    rata2 = sum(nilai) / len(nilai)
    data_mahasiswa.append([nama, nilai, rata2])


# Tampilkan semua data
print("\nData Mahaiswa:")
print("Nama\tNilai\t\tRata-rata")
for siswa in 'data_siswa':
    print(f"{siswa[0]}\t{siswa[1]}\t{siswa[2]:.2f}")

# Tampilkan siswa yang lulus
print("\nMahasiswa Lulus (>= 75):")
for siswa in 'data_siswa':
    if siswa[2] >= 75:
        print(f"{siswa[0]} - {siswa[2]:.2f}")

# Tuples
# Cara Membuat Tuple di Python
t = (nilai_satu, "objek_dua") # type: ignore
t = (1234, 'Hello World')
t1 = (1, 2, 3)
t2 = "a", "b", "c"        # Tanpa tanda kurung juga valid
t3 = ()                   # Tuple kosong
t4 = (5,)                 # Tuple satu elemen (perlu koma!)

# membuat tuple singleton 
satu = ('Isi',)
dua = "ini adalah tuple?",

# cek tipe datanya
print(type(satu))
print(type(dua))

# jika tidak pakai koma
satu = ('Isi')
dua = "ini adalah tuple?"

# cek tipe datanya
print(type(satu))
print(type(dua))

# Indexing dan Slicing Tuple
# membuat tuple
nama = ('Adam', 'Bachtiar', 'Maulachela')

# mengakses indeks ke 1 dari tuple
print(nama[1])
# Membuat Tuple
t = (1, 5, 10, 15)

# mengubah isi elemen tuple
t[0] = 0

# membuat tuple
angka = (10, 20, 30, 40)

# Memotong tuple
print(angka[1:3]) 
print(angka[:2])
print(angka[2:])

# Operasi pada Tuple
# penggabungan tuple
print((1, 2) + (3, 4))

# pengulangan tuple
print(('A',) * 3)

# cek panjang tuple
data = (1, 2, 4, 5)
print(len(data))

# cek keanggotaan tuple
print(3 in data)

# Tuple Bersarang (Nested Tuple)
t = (1, 2, (3, 4))
print(t[2][0])  # Output: 3

tuple1 = "aku", "mahasiswa", "PTI UNDIKMA"
tuple2 = "selama", 3, "tahun"
tuple3 = (tuple1, tuple2) # <- nested tuple

print(tuple3)

# tuple berisi list
t = ([1,2,3,4], True)

print (t)

# Sequence Unpacking
# mula-mula kita buat tuple seperti ini
web = 123, "PTI UNDIKMA", "https://fsttundikma.id"

# lalu di-unpacking
id_web, nama, url = web

# maka sekarang tiga variabel tersebut akan bernilai
# sesuai yang ada di dalam tuple
#
# mari kita cetak
print(id_web)
print(nama)
print(url)

# Latihan Tuple
#Buatlah program yang:

#Menerima input data mata kuliah dalam bentuk tuple (kode, nama, sks).
#simpan semua mata kuliah ke dalam list.
#Tampilkan daftar mata kuliah dan total SKS yang diambil.
#Penyelesainnya : Lakukan inisialisasi list penampung data
matkul_list = []
jumlah = int(input("Input jumlah mata kuliah: "))
for i in range(jumlah):
    print(f"\nMata kuliah ke-{i+1}:")
    kode = input("Kode: ")
    nama = input("Nama: ")
    sks = int(input("SKS: "))
    matkul = (kode, nama, sks)
    matkul_list.append(matkul)

print("\nDaftar Mata Kuliah:")
for m in matkul_list:
    print(m)

total_sks = sum(m[2] for m in matkul_list)
print(f"\nTotal SKS: {total_sks}")

# Dictionary
aku = {
    "nama": "Adam Bachtiar Maulachela",
}

# Cara membuat Dictionary
# contoh jika 1 item
nama_dict = {
    "key": "value"
}

# contoh jika lebih dari 1 item
nama_dict = {
    "key1": "value",
    "key2": "value",
    "key3": "value"
}

# membuat dictionary
dict = {
    "nama"      : "Adam Bachtiar Maulachela",
    "NIDN"      : 62708078505,
    "Prodi"     : "Pendidikan Teknologi Informasi",
    "mat_kul"    : ['Algoritma dan Pemrograman', 'Struktur Data', 'PBO'],
    "status"    : True,
    "sosmed"    : {
        "Github"    : "@adamMaulachela",
        "twiter"    : '_',
        "instagram" : '-'
    }
}

# Fungsi atau Method Dictionary
# Mengakses Nilai Dictionary
# mengakses dict menggunakan key
print("Nama Saya adalah %s" % dict['nama'])
print("Akun Github saya %s" % dict['sosmed']['Github'])

# cara lainnya dengan menggunakan .get
print("NIDN Saya adalah %s" % dict.get('NIDN'))

# Mengubah Nilai Item Dictionary
nama_dict['kunci'] = 'Nilai_baru'
# Mengubah nilai item dictionary dict dengan key
data['status'] = False

# Cek hasil perubahan
print(data['status'])

# Mengubah nilai item dictionary dengan .update
data.update({"sosmed" : {"twitter" : "@adammaulachaila"}})

# cek hasil perubahan
print(data['sosmed']['twitter'])

# Menghapus Nilai Item Dictionary
# Menghapus menggunakan perintah del
del data['status']

# cek hasil penghapusan data 
print(data)

# Menghapus item menggunkan method pop()
data.pop("sosmed")

# cek hasil penghapusan data 
print(data)

data.clear()

# Menambahkan item pada dictionary
# membuat dictionary
mahasiswa = {
    "name" : "Adam Bachtiar Maulachela"
}

# menambahkan nim
mahasiswa.update({
    "nidn" : "0708078505"
})

# melihat hasilnya
print(mahasiswa)

# Looping Dictionary
# mencetak data pada dict secara berulang-ulang setiap key
for key in mahasiswa:
    print(key, mahasiswa[key])

# Atau:
for key, value in mahasiswa.items():
    print(f"{key}: {value}")

# Latihan Dictionary
data_mahasiswa = {
    "NIM001": {"nama": "Rina", "jurusan": "TI"},
    "NIM002": {"nama": "Budi", "jurusan": "SI"}
}

data_mahasiswa = {}
jumlah = int(input("Jumlah mahasiswa: "))

for i in range(jumlah):
    print(f"\nMahasiswa ke-{i+1}:")
    nim = input("NIM: ")
    nama = input("Nama: ")
    jurusan = input("Jurusan: ")
    data_mahasiswa[nim] = {
        "nama": nama,
        "jurusan": jurusan
    }

data_mahasiswa["22001"] = {"nama": "Rina", "jurusan": "TI"}

print("\nCari data mahasiswa")
cari = input("Masukkan NIM: ")
if cari in data_mahasiswa:
    mhs = data_mahasiswa[cari]
    print(f"Nama: {mhs['nama']}, Jurusan: {mhs['jurusan']}")
else:
    print("Mahasiswa tidak ditemukan.")

print("\nDaftar Seluruh Mahasiswa:")
for nim, info in data_mahasiswa.items():
    print(f"NIM: {nim} → {info['nama']} ({info['jurusan']})")

