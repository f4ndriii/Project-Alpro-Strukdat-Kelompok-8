from struktur_data import LinkedList

riwayat = LinkedList()

def tambah_riwayat(aksi):
    riwayat.tambah(aksi)

def lihat_riwayat():
    print("=== Riwayat Aktivitas ===")
    riwayat.tampil()