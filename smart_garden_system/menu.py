from tanaman import (
    undo,
    sort_umur,
    sort_tinggi,
    cari_tanaman,
    tambah_tanaman,
    lihat_tanaman,
    hapus_tanaman,
    edit_tanaman,
    tampil_kategori,
    lihat_total_air,
    filter_kategori
)

from jadwal import (
    tambah_jadwal,
    proses_jadwal,
    lihat_jadwal
)

from riwayat import lihat_riwayat

def jalan_menu():
    while True:
        print("\n=============================")
        print("     SMART GARDEN SYSTEM     ")
        print("=============================")
        print("============ MENU ===========")
        print("1. Tambah Tanaman")
        print("2. Lihat Tanaman")
        print("3. Hapus Tanaman")
        print("4. Edit Tanaman")
        print("5. Urutkan Berdasarkan Umur")
        print("6. Urutkan Berdasarkan Tinggi")
        print("7. Cari Tanaman")
        print("8. Undo")
        print("9. Tambah Jadwal Penyiraman")
        print("10. Proses Penyiraman")
        print("11. Lihat Jadwal Penyiraman")
        print("12. Lihat Riwayat")
        print("13. Lihat Kategori Tanaman")
        print("14. Total kebutuhan air")
        print("15. Filter Berdasarkan Kategori")
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
        elif pilih == "5":
            sort_umur()
        elif pilih == "6":
            sort_tinggi()
        elif pilih == "7":
            cari_tanaman()
        elif pilih == "8":
            undo()
        elif pilih == "9":
            tambah_jadwal()
        elif pilih == "10":
            proses_jadwal()
        elif pilih == "11":
            lihat_jadwal()
        elif pilih == "12":
            lihat_riwayat()
        elif pilih == "13":
            tampil_kategori()
        elif pilih == "14":
            lihat_total_air()
        elif pilih == "15":
            filter_kategori()
        elif pilih == "0":
            break
        else:
            print("Pilihan tidak valid")

if __name__ == "__main__":
    jalan_menu()