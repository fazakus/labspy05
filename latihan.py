print("=======================================")
print("===\t Nama \t : Faza Ardan Kusuma \t===")
print("===\t NIM \t : 312010001 \t\t\t===")
print("===\t Kelas \t : T1.20.B1 \t\t\t===")
print("=======================================")
print()
print("==========\t | Latihan |\t ==========")
print()

kontak = {"Ari": "085215565501", "Dina": "08788767778"}
print("Daftar Kontak")
print("Nama | Nomor Telepon")
print(kontak)
print()

print("Kontak Ari")
print(kontak['Ari'])
print()

print("Menambahkan kontak baru dengan nama Riko - 087654544")
kontak['Riko'] = '087654544'
print(kontak['Riko'])
print()

print("Merubah kontak Dina dengan nomor baru 088999776")
kontak['Dina'] = '088999776'
print(kontak['Dina'])
print()

print("Nama - nama pada kontak")
print(kontak.keys())
print()

print("Nomor - nomor pada kontak")
print(kontak.values())
print()

print("Daftar kontak")
print(kontak.items())
print()

print("Menghapus kontak Dina")
del kontak['Dina']
print(kontak)