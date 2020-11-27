# labspy05

##Tugas Praktikum 5

Setelah tugas praktikum 4, maka lanjut untuk tugas praktikum 5
Bila di tugas 4 membuat data mahasiswa dengan list, di tugas 5 ini akan membuat data mahasiswa dengan ***dictionary*** yang kita dapat menambah, mengubah, dan menghapus datanya.

Sebelum ke tugas praktikum, adapun tugas latihan, berikut adalah latihannya

###Latihan
Pada latihan ini saya disuruh membuat dictionary daftar kontak, lalu disertai cara untuk menambah, mengubah, menampilkan key, values & item tersebut, dan menghapus<br>

Berikut adalah soal latihannya<br>
![Latihan](Pic/latihan.png)<br>

Untuk source codenya <br>
![sclatihsn](Pic/outputlatihan.png) <br>

###Tugas Praktikum
Untuk tugas praktikum 5 ini, tugasnya membuat program daftar nilai mahasiswa sederhana yang bisa ditambah, dihapus, diubah, dilihat dan dimasukkan kedalam tabel, & keluar dari program tersebut

Berikut untuk flowcartnya <br>

Tugas 5<br>
![tugas5](Pic/tugaspraktikum.png)<br>

Output pada tugas :<br>
    *  Jika sebelum kita memasukkan data mahasiswa, bila kita ingin melihat tabel maka outputnya seperti ini
  ![outputtugas](Pic/output1.png)<br>
     
* ![outputtugas2](Pic/output2.png)<br>
   Untuk output selanjutnya menggunakan tabel

Untuk source code nya
```python
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
```

Penjelasan :

Program ini dibuat dengan ***Dictionary***, dengan pilihan melihat, menambahkan, mengubah, menghapus, mencari & keluar dari program.

* Membuat menu pilihan<br>
    Untuk membuat pilihan saya menggunakan perulangan **while true** 
    ```python
    data = {}
    while True:
        print("")
        x = input("(L)ihat, (T)ambah, (U)bah, (H)apus,(C)ari, (K)eluar: ")
    ``` 
  * **data = {}**, membuat dictionary kosong<br>
  * **x = input**, untuk menampilkan opsi pilihan<br>
  
* Melihat data
    Karena menggunakan perulangan **while true**, dan ada banyak pilihan, maka disini menggunakan **if, elif & else**<br>
    Setelah muncul menu, maka bila kita masukkan menu **l** atau Lihat
    agar bisa memunculkan tabel, maka berikut source codenya
    ```python
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
    ```
  * **x.lower()**, berfungsi apabila kita memasukkan huruf L besar(kapital) maka akan otomatis terbaca menjadi huruf kecil, jadi agar tidak ada error apalabila kita memasukkan huruf besar maupun kecil, maka bila ditambahkan menjadi **if x.lower() == "l":** dia akan menampilkan list <br>
  * Di pilihan **"l"** ada 2 output, yaitu output dengan data dan output tanpa data, bila kita belum memasukkan data apapun dan kita memilih menu **lihat** atau **"l"** maka outputnya akan seperti berikut <br>
  ![outoutl1](Pic/outputpraktikuml.png) <br>
  tapi bila sudah ada data maka data akan ditampilkan seperti ini<br>
  ![outputl2](Pic/outputpraktikuml1.png)
  * Karena ada 2 output dalam pilihan **"l"** maka menggunakan **"if"** & **"else"**
  * **print("| {6:4} | {0:13s} | {1:17} | {2:10d} |  {3:6d} | {3:7d} | {5:6.2f} | "**, berfungsi untuk membuat spasi atau jarak lalu di ikuti dengan **.format(x[0], x[1][0], x[1][1], x[1][2], x[1][3], x[1][4], i))**, untuk menampilkan data yang telah di input<br>
  
* 
