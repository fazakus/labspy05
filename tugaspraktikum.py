data = {}
while True:
    print("")
    x = input("(L)ihat, (T)ambah, (U)bah, (H)apus,(C)ari, (K)eluar: ")
    if x.lower() == "l":
        if data.items():
            print("================================== Daftar Nilai ======================================")
            print("======================================================================================")
            print("|  No  |      NIM      |      NAMA         |    TUGAS   |   UTS   |   UAS   | AKHIR  |")
            print("======================================================================================")
            i = 0
            for x in data.items():
                i += 1
                print("| {6:4} | {0:13s} | {1:17} | {2:10d} |  {3:6d} | {3:7d} | {5:6.2f} | " \
                      .format(x[0], x[1][0], x[1][1], x[1][2], x[1][3], x[1][4], i))
        else:
            print("===================================== Daftar Nilai ===================================")
            print("======================================================================================")
            print("|  No  |      Nama     |      NIM      |   TUGAS  |   UTS   |   UAS   | Nilai Akhir  |")
            print("======================================================================================")
            print("|                                    Tidak Ada Data                                  |")
        print("======================================================================================")
    elif x.lower() == "t":
        print("Tambah Data")
        nama = input("Nama\t\t: ")
        nim = int(input("NIM\t\t\t: "))
        tugas = int(input("NIlai Tugas\t: "))
        uts = int(input("Nilai UTS\t: "))
        uas = int(input("Nilai UAS\t: "))
        nilaiakhir = ((tugas) * 30 / 100 + (uts) * 35 / 100 + (uas) * 35 / 100)
        data[nama] = nim, tugas, uts, uas, nilaiakhir
    elif x.lower() == "u":
        print("===============================")
        print("===Edit Data Nilai Mahasiswa===")
        print("===============================")
        nama = input("Masukan Nama\t\t: ")
        print("===============================")
        if nama in data.keys():
            nim = input("NIM baru\t\t\t: ")
            tugas = int(input("Nilai Tugas Baru\t: "))
            uts = int(input("Nilai UTS Baru\t\t: "))
            uas = int(input("Nilai UAS Baru\t\t: "))
            nilaiakhir = ((tugas) * 30 / 100 + (uts) * 35 / 100 + (uas) * 35 / 100)
            data[nama] = nim, tugas, uts, uas, nilaiakhir
            print()
            print("================================")
            print("=====BERHASIL MENGUBAH DATA=====")
            print("================================")
        else:
            print("Data nilai{0} tidak ada ".format(nama))
    elif x.lower() == "h":
        print("Hapus Data Nilai Mahasiswa")
        nama = input(" Masukan Nama\t:")
        if nama in data.keys():
            del data[nama]
            print()
            print("================================")
            print("====BERHASIL MENGHAPUS DATA====")
            print("================================")
        else:
            print("Data {0} tidak ada".format(nama))
    elif x.lower() == "c":
        print("Cari Data Nilai Mahasiswa")
        nama = input("Masukan Nama\t: ")
        if nama in data.keys():
            print("============================ Daftar Nilai ========================================")
            print("==================================================================================")
            print("====================| NAMA | (NIM, TUGAS, UTS, UAS, NILAI AKHIR) |================")
            print("==================================================================================")
            print("                    | {0} | {1} | ".format(nama, data[nama]))
            print("==================================================================================")
        else:
            print("Datanya {0} tidak ada ".format(nama))
    elif x.lower() == "k":
        print("=================================")
        print("====== KELUAR DARI PROGRAM ======")
        print("=================================")
        break

    else:
        print("Pilih Menu Yang Tersedia")