def tampilkan_saldo(saldo):
    print(f"saldo anda adalah Rp{saldo}")

def deposit(saldo):
    jumlah = float(input("Masukkan Jumlah Saldo yang ingin di deposit : Rp"))

    if jumlah < 0: 
        print("************************")
        print("Masukkan Nilai yang valid")
        print("************************")
        return 0
    else:
        return jumlah

def menarik_uang(saldo):
    jumlah = float(input("Masukkan Jumlah Uang yang ingin ditarik : Rp"))

    if jumlah > saldo:
        print("************************")
        print("Saldo tidak mencukupi")
        print(f"saldo anda adalah {saldo}")
        print("************************")
        return 0
    elif jumlah < 0:
        print("************************")
        print("anda tidak memiliki saldo")
        print("************************")
        return 0
    else:
        return jumlah