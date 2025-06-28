# Fungsi membuat node double linked-list
def buat_node(data):
    return {'data': data, 'prev': None, 'next': None}

# Tambah node di akhir
def tambah_akhir(head, data):
    new_node = buat_node(data)
    if head is None:
        return new_node
    current = head
    while current['next'] is not None:
        current = current['next']
    current['next'] = new_node
    new_node['prev'] = current
    return head

# Cetak isi double linked-list
def cetak_dll(head):
    current = head
    print('HEAD', end=' <-> ')
    while current:
        print(current['data'], end=' <-> ')
        current = current['next']
    print('NULL')

# Hapus node awal
def hapus_awal(head):
    if head is None:
        print("Linked-list kosong!")
        return None
    print(f"Node dengan data '{head['data']}' dihapus dari awal.")
    if head['next'] is not None:
        head['next']['prev'] = None
    return head['next']

# Hapus node akhir
def hapus_akhir(head):
    if head is None:
        print("Linked-list kosong!")
        return None
    if head['next'] is None:
        print(f"Node dengan data '{head['data']}' dihapus. List kosong.")
        return None
    current = head
    while current['next'] is not None:
        current = current['next']
    print(f"Node dengan data '{current['data']}' dihapus dari akhir.")
    current['prev']['next'] = None
    return head

# Hapus berdasarkan data
def hapus_berdasarkan_data(head, target):
    if head is None:
        print("Linked-list kosong!")
        return None
    current = head
    while current is not None:
        if current['data'] == target:
            if current['prev'] is None:
                print(f"Node dengan data '{target}' dihapus (head).")
                return hapus_awal(head)
            elif current['next'] is None:
                print(f"Node dengan data '{target}' dihapus (tail).")
                current['prev']['next'] = None
            else:
                print(f"Node dengan data '{target}' dihapus (tengah).")
                current['prev']['next'] = current['next']
                current['next']['prev'] = current['prev']
            return head
        current = current['next']
    print(f"Data '{target}' tidak ditemukan dalam linked-list.")
    return head

# ===== Program Utama =====
head = None

while True:
    print("\nMENU DOUBLE LINKED-LIST")
    print("1. Tambah Node (Akhir)")
    print("2. Cetak Linked List")
    print("3. Hapus Node Awal")
    print("4. Hapus Node Akhir")
    print("5. Hapus Node Berdasarkan Nilai")
    print("6. Keluar")

    pilihan = input("Pilih menu (1-6): ")

    if pilihan == '1':
        data = int(input("Masukkan data: "))
        head = tambah_akhir(head, data)
    elif pilihan == '2':
        cetak_dll(head)
    elif pilihan == '3':
        head = hapus_awal(head)
    elif pilihan == '4':
        head = hapus_akhir(head)
    elif pilihan == '5':
        target = int(input("Masukkan data yang ingin dihapus: "))
        head = hapus_berdasarkan_data(head, target)
    elif pilihan == '6':
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak valid!")
