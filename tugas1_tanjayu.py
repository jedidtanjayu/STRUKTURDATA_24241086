def segitiga_sama_sisi(jumlah_baris):
    for i in range(1, jumlah_baris + 1):
        spasi = ' ' * (jumlah_baris - i)
        bintang = '*' * (2 * i - 1)
        print(spasi + bintang)

try:
    baris = int(input("Masukkan jumlah baris: "))
    segitiga_sama_sisi(baris)
except ValueError:
    print("Harap masukkan angka yang valid.")
