def fibonnaci(n):
    if(n==0):
        return 1
    elif(n==1):
        return 1
    return fibonnaci(n-2) - fibonnaci(n-1)
x = int(input("Masukkan angka : "))
fibonnaci(x)
