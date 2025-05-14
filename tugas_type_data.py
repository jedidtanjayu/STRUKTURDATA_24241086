
# Meminta pengguna memasukkan jumlah mahasiswa
jumlah_mahasiswa = int(input("Masukkan jumlah mahasiswa: "))

# Dictionary untuk menyimpan data
data_mahasiswa = {}

# Perulangan untuk input data setiap mahasiswa
for i in range(jumlah_mahasiswa):
    print(f"\nMahasiswa ke-{i+1}")
    nim = input("Masukkan NIM: ")         # str
    nama = input("Masukkan Nama: ")       # str
    jurusan = input("masukkan jurusan: ")    # str
    alamat = input("masukan alamat: ")   # str

    # List untuk menyimpan tuple (mata kuliah, nilai)
    daftar_nilai = []

    jumlah_matkul = int(input("Masukkan jumlah mata kuliah: "))  # int
    for j in range(jumlah_matkul):
        matkul = input(f"  Nama mata kuliah ke-{j+1}: ")         # str
        nilai = float(input(f"  Nilai untuk {matkul}: "))        # float
        daftar_nilai.append((matkul, nilai))                     # tuple dalam list

    # Simpan dalam dictionary
    data_mahasiswa[nim] = {
        "nama": nama,
        "alamat": alamat,
        "jurusan": jurusan,
        "nilai": daftar_nilai
        
    }

# Menampilkan hasil
print("\n=== Daftar Data Mahasiswa dan Nilai Rata-Rata ===")
for nim, info in data_mahasiswa.items():
    nama = info["nama"]
    alamat = info["alamat"]
    jurusan = info["jurusan"]
    nilai_matkul = info["nilai"]
    
    # Hitung rata-rata
    total_nilai = sum(nilai for _, nilai in nilai_matkul)
    rata_rata = total_nilai / len(nilai_matkul) if nilai_matkul else 0

    print(f"\nNIM       : {nim}")
    print(f"Nama      : {nama}")
    print(f"alamat    : {alamat}")
    print(f"jurusan   : {jurusan}")
    print("Nilai     :")
    for matkul, nilai in nilai_matkul:
        print(f"  {matkul} = {nilai}")
    print(f"Rata-rata : {rata_rata:.2f}")
