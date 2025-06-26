# membuat wadah stack
stack = []   

# menggunakan operasi push untuk menambah elemen pada stack
# operasi menambah elemen pada array menggunakan .append()
stack.append(5)
stack.append(17)
stack.append(30)
stack.append(15)
stack.append(77)

# cetak stack
print("stack : ", stack)

# cari tau ukuran dari stack
print("ukuran stack :", len(stack))

# menggunakan operasi top cek puncak dari stack
if len(stack) != 0:
    print("pop : ", stack.pop())
    print("stack setelah dihapus : ", stack)
else: # stack = 0
    print("stack kosong")
    
# menggunakan operasi top untuk cek puncak stack
if len(stack) == 0 :
    print("stack kosong, underflow")
else:
    print("stack : ", stack)
    print("Top stack : ", stack[-1])