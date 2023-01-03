print ("===== Selamat datang di XXV =====")
print (int(input("Masukkan tanggal hari ini: ")))
print ("== Berikut genre film yang tersedia ==")
print ("1. Horror")
print ("2. Action")
operasi = (input("Silahkan pilih mau nonton film bergenre apa:"))

if operasi == '1':
    print("Berikut pilihan film horror yang sedang tayang ==")
    print("1. The Devil's Light")
    print("2. Pengabdi Setan")
elif operasi == '2':
    print("Berikut pilihan film action yang sedang tayang ==")
    print("1. Black Panther: Wakanda Forever")
    print("2. Avatar: The way of Water")
else :
    print("aneh")


print(input("Silahkan pilih mau nonton film apa: "))

t= 25000
y= (input("Mau memesan tiket sebanyak:"))

if y== '1':
    print("Total yang harus dibayar adalah Rp. 25000")
elif y=="2":
    jumlah= t*2
    print("Total yang harus dbayar adalah Rp.",jumlah)
elif y== '3':
    jumlah= t*3
    print("Total yang harus dibayar adalah Rp.",jumlah)



