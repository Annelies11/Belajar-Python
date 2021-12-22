nama = input("Masukkan nama : ")
print("Halo " + nama)
npm = int(input("Masukkan 4 digit terakhir NPM anda : "))

if npm % 2 == 0 :
    print("NPM anda Genap")
    print("Pilih makanan yang anda sukai : \n1.Lontong Balap\n2.Nasi Males")
    pilih = int(input())
    if pilih == 1 :
        print("Anda memilih Lontong Balap.")
    elif pilih == 2 :
        print("Anda memilih Nasi Males.")
    else :
        print("Inputan anda salah")
else :
    print("NPM anda Ganjil")
    print("Pilih film yang anda sukai : \n1.Azab Teman Yang Suka Nanya Ketika Presentasi\n2.Tukang Bubur Naik Pickup")
    pilih = int(input())
    if pilih == 1 :
        print("Anda memilih Azab Teman Yang Suka Nanya Ketika Presentasi.")
    elif pilih == 2 :
        print("Tukang Bubur Naik Pickup.")
    else :
        print("Inputan anda salah")

    
    
 

