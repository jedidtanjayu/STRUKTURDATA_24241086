# membuat node double linked-list
def buat_node(data):
    return {'data': data, 'prev': None, 'next': None}

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

def cetak_dll(head):
    current = head
    print('HEAD', end=' <-> ')
    while current:
        print(current['data'], end=' <-> ')
        current = current['next']
    print('NULL')

def hapus_awal(head):
    if head is None:
        print("Linked-list kosong!")
        return None
    print(f"Node dengan data '{head['data']}' dihapus dari awal.")
    if head['next'] is not None:
        head['next']['prev'] = None
    return head['next']

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

# Menghapus node berdasarkan data
def hapus_berdasarkan_data(head, target):
    if head is None:
        print("Linked-list kosong!")
        return None
    current = head
    while current is not None:
        if current['data'] == target:
            # Jika node di awal
            if current['prev'] is None:
                print(f"Node dengan data '{target}' dihapus (head).")
                return hapus_awal(head)
            # Jika node di akhir
            elif current['next'] is None:
                print(f"Node dengan data '{target}' dihapus (tail).")
                current['prev']['next'] = None
            # Node di tengah
            else:
                print(f"Node dengan data '{target}' dihapus (tengah).")
                current['prev']['next'] = current['next']
                current['next']['prev'] = current['prev']
            return head
        current = current['next']
    print(f"Data '{target}' tidak ditemukan dalam linked-list.")
    return head

head = None
for nilai in [10, 20, 30, 40, 50]:
    head = tambah_akhir(head, nilai)

print("Linked-list awal:")
cetak_dll(head)

head = hapus_awal(head)
cetak_dll(head)

head = hapus_akhir(head)
cetak_dll(head)

head = hapus_berdasarkan_data(head, 30)
cetak_dll(head)

head = hapus_berdasarkan_data(head, 99)
cetak_dll(head)

# Selesai