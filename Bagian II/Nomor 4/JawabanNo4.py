x = int(input("Masukkan panjang baris : "))
y = int(input("Masukkan lebar baris : "))
matriks = []
for row in range(x):
    a=[]
    for column in range(y):
        a.append(int(input()))
    matriks.append(a)

for row in range(y):
    for column in range(x):
        print(matriks[row][column], end=" ")
    print()