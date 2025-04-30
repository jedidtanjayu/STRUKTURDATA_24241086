# Variabel global untuk menyimpan data mahasiswa
mahasiswa = []

# Fungsi Create
def tambah_mahasiswa():
    nama = input("Masukkan nama mahasiswa: ")
    mahasiswa.append(nama)
    print(f"Mahasiswa '{nama}' berhasil ditambahkan.")

# Fungsi Read
def tampilkan_mahasiswa():
    if not mahasiswa:
        print("Belum ada data mahasiswa.")
    else:
        print("Daftar Mahasiswa:")
        for i, nama in enumerate(mahasiswa):
            print(f"[{i}] {nama}")

# Fungsi Update
def ubah_mahasiswa():
    tampilkan_mahasiswa()
    try:
        indeks = int(input("Masukkan indeks mahasiswa yang ingin diubah: "))
        if 0 <= indeks < len(mahasiswa):
            nama_baru = input("Masukkan nama baru: ")
            mahasiswa[indeks] = nama_baru
            print("Data mahasiswa berhasil diperbarui.")
        else:
            print("Indeks tidak valid.")
    except ValueError:
        print("Input harus berupa angka.")

# Fungsi Delete
def hapus_mahasiswa():
    tampilkan_mahasiswa()
    try:
        indeks = int(input("Masukkan indeks mahasiswa yang ingin dihapus: "))
        if 0 <= indeks < len(mahasiswa):
            nama = mahasiswa.pop(indeks)
            print(f"Mahasiswa '{nama}' berhasil dihapus.")
        else:
            print("Indeks tidak valid.")
    except ValueError:
        print("Input harus berupa angka.")

# Fungsi Menu
def tampilkan_menu():
    print("\n--- MENU MANAJEMEN MAHASISWA ---")
    print("[1] Tampilkan Mahasiswa")
    print("[2] Tambah Mahasiswa")
    print("[3] Ubah Mahasiswa")
    print("[4] Hapus Mahasiswa")
    print("[5] Keluar")

# Main Loop
def main():
    while True:  
        tampilkan_menu()
        try:
            pilihan = int(input("Pilih menu: "))
            if pilihan == 1:
                tampilkan_mahasiswa()
            elif pilihan == 2:
                tambah_mahasiswa()
            elif pilihan == 3:
                ubah_mahasiswa()
            elif pilihan == 4:
                hapus_mahasiswa()
            elif pilihan == 5:
                print("Terima kasih, program selesai.")
                exit()
            else:
                print("Pilihan tidak valid.")
        except ValueError:  
            print("Masukkan angka saja!")

# Jalankan program
main()