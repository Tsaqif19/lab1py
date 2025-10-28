max=0
n=input("masukkan nilai n :")

n=int(n)

while n!=0:
    if (n > max) :
        max=n
    n=input("masukkan nilai n :")
    n=int(n)
print("angka terbesar",max)
