# kolaborasi-kode
tugas strategi keamanan siber
while True:
    makanan = input("Masukkan nama makanan (atau ketik 'selesai' untuk mengakhiri): ")
    
if makanan.lower() == 'selesai':
        break
    daftar_makanan.append(makanan)
    print(f"{makanan} telah ditambahkan ke daftar.")

tampilkan_daftar()
