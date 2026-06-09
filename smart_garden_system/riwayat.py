from struktur_data import LinkedList

riwayat = LinkedList()  # Linked List digunakan untuk menyimpan riwayat aktivitas pengguna

# Menambahkan aktivitas baru ke riwayat
def tambah_riwayat(aksi):
    riwayat.tambah(aksi)

# Menampilkan seluruh riwayat aktivitas
def lihat_riwayat():
    print("=== Riwayat Aktivitas ===")
    riwayat.tampil()