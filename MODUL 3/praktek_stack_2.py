# membua program stack array dengan inputan user
# langkah 1 - siapkan wadah stack
tumpukan = []

# langkah 2 - push elemen ke stack input user
while True:
    isi_elemen = input("masukkan elemen ketik selesai")
    if isi_elemen.lower() == 'selesai':
        break
    stack = tumpukan.append(isi_elemen)
    print("Tumpukan : ", tumpukan)
    
# langkah 3 - pop hapus elemen paling atas input user
for i in range(len(tumpukan)) : # stack = 5 range(5)
    # cek stack kosong?
    if len(tumpukan) != 0:
        hapus = input("apakah hapus elemen [ya/tidak]?")
        if hapus.lower() == 'tidak':
            break
        print("pop : ", tumpukan.pop())
        print("sisa elemen pada stack : ", tumpukan)
    else:
        print("stack kosong, underflow")