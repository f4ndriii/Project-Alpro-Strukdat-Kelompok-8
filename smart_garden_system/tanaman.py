from file_io import simpan_data, load_data
from algoritma import bubble_sort_umur, bubble_sort_tinggi, cari_nama
from struktur_data import Stack
undo_stack = Stack()
from struktur_data import Queue
from riwayat import tambah_riwayat
from struktur_data import TreeNode
antrian = Queue()
class Tanaman:
    # Membuat objek tanaman
    def __init__(self, nama, umur, tinggi, kategori):
        self.nama = nama
        self.umur = umur
        self.tinggi = tinggi
        self.kategori = kategori

data_tanaman = []

# Fungsi untuk menambahkan tanaman
def tambah_tanaman():
    print("\n=== Tambah Tanaman ===")
    
    nama = input("Nama tanaman: ")
    umur = int(input("Umur (bulan): "))
    tinggi = int(input("Tinggi (cm): "))
    kategori = input("Kategori (Hias/Buah/Sayur): ")

    t = Tanaman(nama, umur, tinggi, kategori)
    data_tanaman.append(t)

    # Menyimpan ke file txt
    simpan_data(data_tanaman)

    undo_stack.push (("tambah", t))  # Menyimpan aksi tambah ke stack untuk undo

    #Tambah ke riwayat
    tambah_riwayat(f"Menambah tanaman {nama}")

    print("✅ Tanaman berhasil ditambahkan!")

# Fungsi untuk melihat daftar tanaman
def lihat_tanaman():
    print("\n=== Data Tanaman ===")

    if not data_tanaman:
        print("Data masih kosong!")
        return

    nama_terpanjang = max(len(t.nama) for t in data_tanaman)
    lebar_kolom_nama = max(nama_terpanjang, 12)

    print(f"{'No.':<3} | {'Nama Tanaman':<{lebar_kolom_nama}} | {'Umur (bulan)':<16} | {'Tinggi (cm)':<13} | {'Kategori':<10}")
    total_lebar_garis = 4 + 3 + lebar_kolom_nama + 3 + 16 + 3 + 13 + 3 + 10
    print("-"*total_lebar_garis)

    for i, t in enumerate(data_tanaman):
        print(f"{i+1:<3} | {t.nama:<{lebar_kolom_nama}} | {t.umur:<16} | {t.tinggi:<15} | {t.kategori:<10}")

# Fungsi hapus tanaman
def hapus_tanaman():
    lihat_tanaman()

    if not data_tanaman:
        return

    try:
        index = int(input("Pilih nomor tanaman yang mau dihapus: ")) - 1

        if index < 0 or index >= len(data_tanaman):
            print("❌ Nomor tanaman tidak tersedia!")
            return

        data = data_tanaman.pop(index)

        simpan_data(data_tanaman)

        tambah_riwayat(f"Menghapus tanaman {data.nama}")

        undo_stack.push(("hapus", data, index))

        print("🗑️ Data berhasil dihapus!")

    except ValueError:
        print("❌ Masukkan angka!")

# Fungsi edit tanaman
def edit_tanaman():
    lihat_tanaman()

    if not data_tanaman:
        return

    try:
        index = int(input("Pilih nomor tanaman yang mau diedit: ")) - 1
        t = data_tanaman[index]

        print("Masukkan data baru:")
        t.nama = input("Nama baru: ")
        t.umur = int(input("Umur baru: "))
        t.tinggi = int(input("Tinggi baru: "))
        t.kategori = input("Kategori baru: ")

        # Menyimpan kembali data tanaman setelah diedit
        simpan_data(data_tanaman)

        tambah_riwayat(f"Mengedit tanaman {t.nama}")

        print("✏️ Data berhasil diupdate!")
    except:
        print("❌ Input tidak valid!")

# Memasukkan data dari file txt ke program
def init_data():
    global data_tanaman #Memakai data_tanaman global
    raw_data = load_data() #Mengambil data dari file

    #Mengubah tuple menjadi objek tanaman
    for nama, umur, tinggi, kategori in raw_data:
        data_tanaman.append(Tanaman(nama, umur, tinggi, kategori))

if __name__ == "__main__":
    t1 = Tanaman("Mawar", 3, 50, "Hias")

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
    if not data_tanaman:
        return

    bubble_sort_umur(data_tanaman)
    simpan_data(data_tanaman)
    tambah_riwayat("Mengurutkan tanaman berdasarkan umur")
    print("\n=== Tanaman Berhasil Diurutkan Berdasarkan Umur ===")
    print("\n=== pilih opsi lihat tanaman untuk melihat hasilnya ===")

#Sorting Tanaman Berdasarkan Tinggi
def sort_tinggi():
    if not data_tanaman:
        return

    bubble_sort_tinggi(data_tanaman)
    simpan_data(data_tanaman)
    tambah_riwayat("Mengurutkan tanaman berdasarkan tinggi")
    print("\n=== Tanaman Berhasil Diurutkan Berdasarkan Tinggi ===")
    print("=== pilih opsi lihat tanaman untuk melihat hasilnya ===")

#Mencari Tanaman Berdasarkan Nama
def cari_tanaman():
    if not data_tanaman:
        print("\nData masih kosong!")
        return

    nama = input("\nMasukkan nama tanaman yang ingin dicari: ")
    hasil = cari_nama(data_tanaman, nama)

    if hasil:
        print(f"Tanaman ditemukan: {hasil.nama} | Umur: {hasil.umur} | Tinggi: {hasil.tinggi} | Kategori: {hasil.kategori}")
    else:
        print("❌ Tanaman tidak ditemukan!")
    
# Fungsi undo
def undo():
    if undo_stack.data:
        aksi = undo_stack.pop()

        if aksi[0] == "tambah":
            data_tanaman.pop()  # Menghapus tanaman yang baru ditambahkan
            simpan_data(data_tanaman)  # Menyimpan perubahan ke file
            print("🔄 Undo: Tambah tanaman dibatalkan!")
        elif aksi[0] == "hapus":
            data_tanaman.insert(aksi[2], aksi[1])  # Mengembalikan tanaman yang dihapus
            simpan_data(data_tanaman)  # Menyimpan perubahan ke file
            print("🔄 Undo: Hapus tanaman dibatalkan!")
    else:
        print("❌ Tidak ada aksi untuk di-undo!")


def bangun_tree():
   
    akar = TreeNode("Tanaman")

    # Dictionary sementara untuk simpan node tiap kategori
    # contoh: {"Hias": NodeTree("Hias"), "Buah": NodeTree("Buah")}
    kategori_nodes = {}

    for t in data_tanaman:
        # Kalau kategori belum ada di tree, buat node baru
        if t.kategori not in kategori_nodes:
            node_kategori = TreeNode(t.kategori)
            akar.tambah_anak(node_kategori)
            kategori_nodes[t.kategori] = node_kategori

        # Tambahkan nama tanaman sebagai anak dari node kategorinya
        node_tanaman = TreeNode(f"{t.nama} (umur:{t.umur}bln, tinggi:{t.tinggi}cm)")
        kategori_nodes[t.kategori].tambah_anak(node_tanaman)

    return akar


def tampil_kategori():
    if not data_tanaman:
        print("\n❌ Belum ada data tanaman!")
        return

    print("\n=== Kategori Tanaman ===")
    akar = bangun_tree()   # bangun tree dari data terkini
    akar.tampil()

