from struktur_data import DoubleLinkedList

riwayat = DoubleLinkedList()

# Menambahkan aktivitas baru ke riwayat
def tambah_riwayat(aksi):
    riwayat.tambah(aksi)

# Menampilkan seluruh riwayat aktivitas
def lihat_riwayat():
    if riwayat.head is None:
        print("=== Riwayat Aktivitas ===")
        print("Belum ada riwayat aktivitas.")
        return

    print("=== Riwayat Aktivitas ===")
    pilihan = input("\nTampilkan dari:"
                    "\n(1) Lama→Baru"
                    "\natau (2) Baru→Lama"
                    "\npilih: ")

    if pilihan == "1":
        riwayat.tampil_maju()
    elif pilihan == "2":
        riwayat.tampil_mundur()
    else:
        print("Pilihan tidak valid.")