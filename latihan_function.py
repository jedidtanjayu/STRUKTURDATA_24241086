# variabel global untuk menyimpan data buku
buku = []
# Fungsishow_data()
# Fungsi untuk menampilkan semua data buku
def show_data():
    if len(buku) <=0 :
        print("DATA BUKU BELUM ADA")
    else:
        for indeks in range(len(buku)):
            print("[%d] %s" % (indeks, buku[indeks]))
# Fungsiinsert_data()
def insert_data():
    buku_baru = input("Judul Buku : ")
    buku.append(buku_baru)
# Fungsiedit_data()
def edit_data():
    show_data()
    indeks = int(input("Inputkan ID Buku : "))
    if(indeks > len(buku)):
        print("ID Buku Tidak Ditemukan")
    else:
        judul_baru = input("Judul Baru : ")
        buku[indeks] = judul_baru
# Fungsidelete_data()
def delete_data():
    show_data()
    indeks = int(input("Inputkan ID Buku : "))
    if(indeks > len(buku)):
        print("ID Buku Tidak Ditemukan")
    else:
        buku.remove(buku[indeks])
        print(f"Buku dengan ID {indeks} Terhapus")
# 
def show_menu():
    print("\n")
    print(5*"-","MENU", 5*"-")
    print("[1] Show Data")
    print("[2] Insert Data")
    print("[3] Edit Data")
    print("[4] Delete Data")
    print("[5] Exit")
    
    menu = int(input("PILIH MENU : "))
    print("\n")
    if menu == 1:
        show_data()
    elif menu == 2:
        insert_data()
    elif menu == 3:
        edit_data()
    elif menu == 4:
        delete_data()
    elif menu == 5:
        exit()
    else:
        print("Pilihan Anda Salah!")

if __name__ == "__main__":
    while(True):
        show_menu()