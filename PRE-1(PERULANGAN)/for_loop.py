# PERULANGAN
# for-loop
'''
   for-loop digunakan untuk perulangan
   yang diketahui jumlah perulangannya
   Counted-loop

   syntax :
   for kondisi :
     aksi 1 - bagian dari loop
    aksi 2 - bukan bagian dari loop
'''

a = 0
a += 1
print(a)
a += 1
print(a)
a += 1
print(a)
a += 1
print(a)

# boros line of code
 
# perulangan menggunakan list
angka = [0,1,5,7,10]
for i in angka :
 print(f"i saat ini ->{i}")
print("ini akhir dari loop") 

# perulangan menggunakan range
angka_range = range(5) # diulang 5 kali

for i in angka_range:
    print(f"i saat ini->{i}")
print("akhir dari loop 2\n")

angka2_range = range(1,10) # diulang 9 kali
print (list, {angka2_range})
for i in angka2_range:
   print(f"i saat ini->{i}")
print("ini akhir dari loop 3\n")

# perulangan menggunakan string
string = "Mandalika"
print(string)

for i in string :
   print(f"i saat ini ->{i}")
print("ini akhir dari loop 4\n")
