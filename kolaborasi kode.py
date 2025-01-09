daftar_makanan = []

def tampilkan_daftar():
    print("\nDaftar Makanan:")
    if not daftar_makanan:
        print("Daftar makanan kosong.")
    else:
        for i, makanan in enumerate(daftar_makanan, start=1):
            print(f"{i}. {makanan}")

while True:
    makanan = input("Masukkan nama makanan (atau ketik 'selesai' untuk mengakhiri): ")
    
    if makanan.lower() == 'selesai':
        break
    
    daftar_makanan.append(makanan)
    print(f"{makanan} telah ditambahkan ke daftar.")

tampilkan_daftar()