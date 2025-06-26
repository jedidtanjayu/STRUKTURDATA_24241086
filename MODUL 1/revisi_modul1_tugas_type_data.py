# Program Rekapitulasi Nilai Mahasiswa

# Dictionary untuk menyimpan data
data_mahasiswa = {} #  Di sini kita membuat “kotak besar” untuk menyimpan semua data mahasiswa. Kotak ini namanya data_mahasiswa dan bentuknya adalah dictionary

# Input jumlah mahasiswa
jumlah_mahasiswa = int(input("Masukkan jumlah mahasiswa: ")) # Program akan bertanya: “Ada berapa mahasiswa yang mau dicatat?” Lalu kita jawab dengan angka, misalnya 3

for i in range(jumlah_mahasiswa): # Program akan mengulang sesuai jumlah mahasiswa yang dimasukkan.
    print(f"\nMahasiswa ke-{i+1}") #  Menampilkan “Mahasiswa ke-1”, “Mahasiswa ke-2”, dan seterusnya supaya tahu sedang mengisi data siapa.



    # Validasi NIM hanya angka
    while True:                                             
        nim = input("Masukkan NIM: ")
        if nim.isdigit():
            break                                   #  Program akan terus meminta NIM sampai yang dimasukkan adalah angka semua. NIM itu seperti nomor identitas mahasiswa.
        else:
            print("  ❌ NIM harus berupa angka!")




    nama = input("Masukkan Nama: ")     # Masukkan nama mahasiswa dan jumlah mata kuliah yang dia ambil (contoh: 3 pelajaran).
    jumlah_matkul = int(input("Masukkan jumlah mata kuliah: "))



    mata_kuliah = []                #  Kita buat daftar kosong untuk menyimpan pelajaran dan nilainya. Kemudian ulangi untuk setiap mata kuliah.
    for j in range(jumlah_matkul):
    
        # Validasi nama mata kuliah hanya huruf/spasi
        while True:
            matkul = input(f"  Nama Mata Kuliah ke-{j+1}: ")
            if all(c.isalpha() or c.isspace() for c in matkul) and matkul.strip() != "":    #  Nama pelajaran harus huruf saja, tidak boleh angka. Contoh benar: "Matematika", salah: "Matematika1".

                break
            else:
                print("  ❌ Nama mata kuliah harus berupa huruf dan tidak boleh mengandung angka!")

        # Validasi nilai mata kuliah harus float
        while True:
            try:
                nilai = float(input(f"  Nilai Mata Kuliah '{matkul}': "))   #  Meminta nilai dari pelajaran. Harus angka, misalnya 80 atau 75.5. Kalau salah ketik, diminta ulang.
                break
            except ValueError:
                print("  ❌ Nilai harus berupa angka (misal: 80 atau 75.5)!")

        mata_kuliah.append((matkul, nilai)) # Kita masukkan nama pelajaran dan nilainya ke dalam daftar.

    # Simpan ke dictionary sesuai struktur
    data_mahasiswa[nim] = (nama, mata_kuliah) #  Setelah semua diisi, kita simpan semua data (nama dan nilai-nilai) di kotak utama data_mahasiswa

# Menampilkan semua data
print("\n=== Rekap Data Mahasiswa ===") # Kita mulai menampilkan hasil data semua mahasiswa.

print(f"{data_mahasiswa[nim]} : nama : {nama}, matkul : {mata_kuliah}")     # Ini akan mencetak hanya data mahasiswa terakhir, tidak perlu ada di sini atau bisa dihapus.
for nim, (nama, nilai_list) in data_mahasiswa.items():  # Kita mulai melihat isi kotak satu per satu, ambil NIM, nama, dan daftar nilai.

    total_nilai = sum(nilai for _, nilai in nilai_list)             #  Kita jumlahkan semua nilai, lalu dibagi banyaknya pelajaran untuk dapat rata-rata.
    rata_rata = total_nilai / len(nilai_list) if nilai_list else 0

    print(f"\nNIM   : {nim}")
    print(f"Nama  : {nama}")
    print("Nilai Mata Kuliah:")         #  Kita tampilkan: NIM, NAMA, SEMUA NILAI PELAJARAN, Rata-rata nilai (dua angka di belakang koma)
    for matkul, nilai in nilai_list:
        print(f"  - {matkul}: {nilai}")
    print(f"Rata-rata Nilai: {rata_rata:.2f}")