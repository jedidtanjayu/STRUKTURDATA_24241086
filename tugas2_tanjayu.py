def deret_ganjil(batas):
    print(f"Deret bilangan ganjil sampai {batas}:")
    for i in range(1, batas + 1):
        if i % 2 != 0:
            print(i, end=' ')

try:
    batas = int(input("Masukkan batas akhir deret: "))
    deret_ganjil(batas)
except ValueError:
    print("Harap masukkan angka yang valid.")
