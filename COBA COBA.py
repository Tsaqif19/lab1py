print ("Nama = Yharis Arkan Tsaqif")

max = None

while True:
    n = int(input("Masukkan bilangan: "))
    
    
    if n == 0:
        break
    
    if (max is None) or (n > max):
        max = n

if max is not None:
    print(f"\nBilangan terbesar adalah: {max}")
else:
    print("\nTidak ada bilangan yang dimasukkan.")