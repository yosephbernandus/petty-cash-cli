def petty_cash():

    list_uang_masuk = []
    list_uang_keluar = []
    while True:
        print("0. Quit Application")
        print("1. Masukan Uang Masuk")
        print("2. Masukan Uang Keluar")
        print("3. List Uang Masuk")
        print("4. List Uang Keluar")
        print("5. Total Uang Masuk - Total Uang Keluar")

        choice = input("Masukan pilihan [0 / 1 / 2 / 3 / 4 / 5] : ")
        if choice == "1":
            while True:
                print("================================================================")
                uang_masuk = input("Jumlah Uang Masuk : ")
                if not uang_masuk.isdigit():
                    print("Jumlah uang salah, mohon ulangi kembali")
                    continue
                else:
                    break

            amount = int(uang_masuk)
            list_uang_masuk.append(amount)

            print("Uang Masuk :", amount)
            print("================================================================")
        elif choice == "2":
            while True:
                print("================================================================")
                uang_keluar = input("Jumlah Uang Keluar : ")
                if not uang_keluar.isdigit():
                    print("Jumlah uang keluar salah, mohon ulangi kembali")
                    continue
                else:
                    break

            amount = int(uang_masuk)
            list_uang_keluar.append(amount)

            print("Uang Keluar :", amount)
            print("================================================================")
        elif choice == "3":
            print("List uang masuk", list_uang_masuk)
            print("================================================================")
        elif choice == "4":
            print("List uang keluar", list_uang_keluar)
            print("================================================================")
        elif choice == "5":
            print("Total Uang Masuk - Total Uang Keluar", sum(list_uang_masuk) - sum(list_uang_keluar))
            print("================================================================")
        else:
            break

    print("================================================================")
    print("Berhasil Keluar Applications")
