from tanaman import (
    tambah_tanaman,
    lihat_tanaman,
    hapus_tanaman,
    edit_tanaman
)

def jalan_menu():
    while True:
        print("\n=== MENU ===")
        print("1. Tambah Tanaman")
        print("2. Lihat Tanaman")
        print("3. Hapus Tanaman")
        print("4. Edit Tanaman")
        print("0. Keluar")

        pilih = input("Pilih: ")

        if pilih == "1":
            tambah_tanaman()
        elif pilih == "2":
            lihat_tanaman()
        elif pilih == "3":
            hapus_tanaman()
        elif pilih == "4":
            edit_tanaman()
        elif pilih == "0":
            break
        else:
            print("❌ Pilihan tidak valid")