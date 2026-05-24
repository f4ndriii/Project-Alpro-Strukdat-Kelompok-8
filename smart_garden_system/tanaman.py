from file_io import simpan_data, load_data
from algoritma import bubble_sort_umur, bubble_sort_tinggi, cari_nama
from struktur_data import Stack
undo_stack = Stack()
from struktur_data import Queue
antrian = Queue()
class Tanaman:
    # Membuat objek tanaman
    def __init__(self, nama, umur, tinggi):
        self.nama = nama
        self.umur = umur
        self.tinggi = tinggi

data_tanaman = []

# Fungsi untuk menambahkan tanaman
def tambah_tanaman():
    print("\n=== Tambah Tanaman ===")
    
    nama = input("Nama tanaman: ")
    umur = int(input("Umur (bulan): "))
    tinggi = int(input("Tinggi (cm): "))

    t = Tanaman(nama, umur, tinggi)
    data_tanaman.append(t)

    undo_stack.push (("tambah", t))  # Menyimpan aksi tambah ke stack untuk undo

    # Menyimpan ke file txt
    simpan_data(data_tanaman)

    print("✅ Tanaman berhasil ditambahkan!")

# Fungsi untuk melihat daftar tanaman
def lihat_tanaman():
    print("\n=== Data Tanaman ===")

    if not data_tanaman:
        print("Data masih kosong!")
        return

    for i, t in enumerate(data_tanaman):
        print(f"{i}. {t.nama} | Umur: {t.umur} | Tinggi: {t.tinggi}")

# Fungsi hapus tanaman
def hapus_tanaman():
    lihat_tanaman()

    if not data_tanaman:
        return

    try:
        index = int(input("Pilih index yang mau dihapus: "))
        data_tanaman.pop(index)

        # Menyimpan kembali data tanaman setelah dihapus
        simpan_data(data_tanaman)

        print("🗑️ Data berhasil dihapus!")
    except:
        print("❌ Input tidak valid!")

    data = data_tanaman.pop(index)
    undo_stack.push (("hapus", data, index))  # Menyimpan aksi hapus ke stack untuk undo


# Fungsi edit tanaman
def edit_tanaman():
    lihat_tanaman()

    if not data_tanaman:
        return

    try:
        index = int(input("Pilih index yang mau diedit: "))
        t = data_tanaman[index]

        print("Masukkan data baru:")
        t.nama = input("Nama baru: ")
        t.umur = int(input("Umur baru: "))
        t.tinggi = int(input("Tinggi baru: "))

        # Menyimpan kembali data tanaman setelah diedit
        simpan_data(data_tanaman)

        print("✏️ Data berhasil diupdate!")
    except:
        print("❌ Input tidak valid!")

# Memasukkan data dari file txt ke program
def init_data():
    global data_tanaman #Memakai data_tanaman global
    raw_data = load_data() #Mengambil data dari file

    #Mengubah tuple menjadi objek tanaman
    for nama, umur, tinggi in raw_data:
        data_tanaman.append(Tanaman(nama, umur, tinggi))

if __name__ == "__main__":
    t1 = Tanaman("Mawar", 3, 50)

    print(t1.nama)
    print(t1.umur)
    print(t1.tinggi)

    data_tanaman.append(t1)
    print(data_tanaman[0].nama)
    print(data_tanaman[0].umur)
    print(data_tanaman[0].tinggi)

    tambah_tanaman()
    lihat_tanaman()
    hapus_tanaman()
    lihat_tanaman()
    edit_tanaman()
    lihat_tanaman()

#Sorting Tanaman Berdasarkan Umur
def sort_umur():
    bubble_sort_umur(data_tanaman)
    print("\n=== Tanaman diurutkan berdasarkan umur ===")

#Sorting Tanaman Berdasarkan Tinggi
def sort_tinggi():
    bubble_sort_tinggi(data_tanaman)
    print("\n=== Tanaman diurutkan berdasarkan tinggi ===")

#Mencari Tanaman Berdasarkan Nama
def cari_tanaman():
    nama = input("Masukkan nama tanaman yang ingin dicari: ")
    hasil = cari_nama(data_tanaman, nama)

    if hasil:
        print(f"Tanaman ditemukan: {hasil.nama} | Umur: {hasil.umur} | Tinggi: {hasil.tinggi}")
    else:
        print("❌ Tanaman tidak ditemukan!")
    
# Fungsi undo
def undo():
    if undo_stack.data:
        aksi = undo_stack.pop()

        if aksi[0] == "tambah":
            data_tanaman.pop(aksi[1])  # Menghapus tanaman yang baru ditambahkan
            simpan_data(data_tanaman)  # Menyimpan perubahan ke file
            print("🔄 Undo: Tambah tanaman dibatalkan!")
        elif aksi[0] == "hapus":
            data_tanaman.insert(aksi[2], aksi[1])  # Mengembalikan tanaman yang dihapus
            simpan_data(data_tanaman)  # Menyimpan perubahan ke file
            print("🔄 Undo: Hapus tanaman dibatalkan!")
    else:
        print("❌ Tidak ada aksi untuk di-undo!")


