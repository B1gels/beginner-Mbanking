import system
#*main function

def main():
    saldo = 0
    program = True

    while program:
        print("************************")
        print("===BANKING PROGRAM===")
        print("1.Tampilkan Saldo")
        print("2.Deposit")
        print("3.Menarik Uang")
        print("4.keluar")
        print("************************")

        pilihan = input("Masukkan Pilihan anda (1-4) : ")
        print("************************")

        if pilihan == "1":
            system.tampilkan_saldo(saldo)
        elif pilihan == "2":
            saldo += system.deposit(saldo)
        elif pilihan == "3":
            saldo -= system.menarik_uang(saldo)
        elif pilihan == "4":
            program = False
        else:
            print("\nPilihan tidak cocok coba lagi\n")

            
    print("======TerimaKasih Telah Berkunjung======")

main()
    