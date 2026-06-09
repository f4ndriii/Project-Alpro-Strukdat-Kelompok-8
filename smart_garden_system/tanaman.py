from file_io import simpan_data, load_data
from algoritma import bubble_sort_umur, bubble_sort_tinggi, total_kebutuhan_air
from struktur_data import Stack
undo_stack = Stack()
from riwayat import tambah_riwayat
from struktur_data import TreeNode

#Class yang merepresentasikan data sebuah tanaman
class Tanaman:
    # Membuat objek tanaman
    def __init__(self, nama, umur, tinggi, kategori, kebutuhan_air):
        self.nama = nama
        self.umur = umur
        self.tinggi = tinggi
        self.kategori = kategori
        self.kebutuhan_air = kebutuhan_air

data_tanaman = []       #Menyimpan seluruh objek tanaman   
hash_tanaman = {}       #Hash Table untuk pencarian tanaman berdasarkan nama
kategori_unik = set()   ## Set digunakan agar kategori tanaman tidak duplikat

# Fungsi untuk menambahkan tanaman
def tambah_tanaman():
    print("\n=== Tambah Tanaman ===")
    
    nama = input("Nama tanaman: ").strip()

    if nama == "":
        print("Nama tanaman tidak boleh kosong!")
        return

    try:
        umur = int(input("Umur (bulan): "))
        tinggi = int(input("Tinggi (cm): "))
        kebutuhan_air = int(input("Kebutuhan air (L): "))

    except ValueError:
        print("Input umur, tinggi, dan kebutuhan air harus berupa angka!")
        return

    kategori = input("Kategori (Hias/Buah/Sayur): ").strip().capitalize()
    if kategori not in ["Hias","Buah","Sayur"]:
        print("Kategori hanya boleh Hias, Buah, atau Sayur!")
        return

    t = Tanaman(nama, umur, tinggi, kategori, kebutuhan_air)    # Membuat objek tanaman baru
    data_tanaman.append(t)
    kategori_unik.add(kategori)

    key = t.nama.upper()
    if key not in hash_tanaman:
        hash_tanaman[key] = []
    # Menyimpan objek ke Hash Table berdasarkan nama tanaman
    hash_tanaman[key].append(t)

    # Menyimpan ke file txt
    simpan_data(data_tanaman)

    undo_stack.push (("tambah", t))  # Menyimpan aksi tambah ke stack untuk undo

    #Tambah ke riwayat
    tambah_riwayat(f"Menambah tanaman {nama}")

    print("Tanaman berhasil ditambahkan!")

# Fungsi untuk melihat daftar tanaman
def lihat_tanaman(data=data_tanaman):
    print("\n=== Data Tanaman ===")

    if not data:
        print("Data masih kosong!")
        return
    # Menampilkan data tanaman dalam bentuk tabel
    nama_terpanjang = max(len(t.nama) for t in data)
    lebar_kolom_nama = max(nama_terpanjang, 12)

    print(
        f"{'No.':<3} | {'Nama Tanaman':<{lebar_kolom_nama}} | {'Umur (bulan)':<13} | {'Tinggi (cm)':<12} | {'Kategori':<9} | {'Kebutuhan Air':<13}")

    total_lebar_garis = 4 + 3 + lebar_kolom_nama + 3 + 13 + 3 + 12 + 3 + 10 + 15
    print("-"*total_lebar_garis)

    for i, t in enumerate(data):
        print(f"{i+1:<3} | {t.nama:<{lebar_kolom_nama}} | {t.umur:<13} | {t.tinggi:<12} | {t.kategori:<9} | {t.kebutuhan_air:<13}")

# Fungsi hapus tanaman berdasarkan nomor
def hapus_tanaman():
    lihat_tanaman()

    if not data_tanaman:
        return

    try:
        index = int(input("Pilih nomor tanaman yang mau dihapus: ")) - 1

        if index < 0 or index >= len(data_tanaman):
            print("Nomor tanaman tidak tersedia!")
            return

        data = data_tanaman.pop(index)

        # Menghapus data dari Hash Table
        key = data.nama.upper()
        hash_tanaman[key].remove(data)
        if len(hash_tanaman[key]) == 0:
            del hash_tanaman[key]

        simpan_data(data_tanaman)

        tambah_riwayat(f"Menghapus tanaman {data.nama}")

        undo_stack.push(("hapus", data, index))

        print("Data berhasil dihapus!")

    except ValueError:
        print("Masukkan angka!")

# Fungsi edit tanaman
def edit_tanaman():
    lihat_tanaman()

    if not data_tanaman:
        return

    try:
        index = int(input("Pilih nomor tanaman yang mau diedit: ")) - 1

        if index < 0 or index >= len(data_tanaman):
            print("Nomor tanaman tidak tersedia!")
            return

        t = data_tanaman[index]

        undo_stack.push((
            "edit",
            t,
            t.nama,
            t.umur,
            t.tinggi,
            t.kategori,
            t.kebutuhan_air
        ))

        nama_lama = t.nama.upper()

        print("\n=== Edit Tanaman ===")
        nama_baru = input("Nama baru: ").strip()

        if nama_baru == "":
            print("Nama tanaman tidak boleh kosong!")
            return

        try:
            umur_baru = int(input("Umur baru (bulan): "))
            tinggi_baru = int(input("Tinggi baru (cm): "))
            kebutuhan_air_baru = int(input("Kebutuhan air baru (L): "))

        except ValueError:
            print("Input umur, tinggi, dan kebutuhan air harus berupa angka!")
            return

        kategori_baru = input("Kategori baru (Hias/Buah/Sayur): ").strip().capitalize()

        if kategori_baru not in ["Hias", "Buah", "Sayur"]:
            print("Kategori hanya boleh Hias, Buah, atau Sayur!")
            return
        
        t.umur = umur_baru
        t.tinggi = tinggi_baru
        t.kategori = kategori_baru
        kategori_unik.discard(t.kategori)
        kategori_unik.add(kategori_baru)
        t.kebutuhan_air = kebutuhan_air_baru

        # HAPUS dari hash lama dengan aman
        if nama_lama in hash_tanaman:
            if t in hash_tanaman[nama_lama]:
                hash_tanaman[nama_lama].remove(t)

            if len(hash_tanaman[nama_lama]) == 0:
                del hash_tanaman[nama_lama]

        # UPDATE DATA NAMA TANAMAN
        t.nama = nama_baru
        key_baru = t.nama.upper()

        # MASUKKAN KE HASH BARU
        if key_baru not in hash_tanaman:
            hash_tanaman[key_baru] = []

        hash_tanaman[key_baru].append(t)

        # Menyimpan kembali data tanaman setelah diedit
        simpan_data(data_tanaman)

        tambah_riwayat(f"Mengedit tanaman {t.nama}")

        print("Data berhasil diupdate!")

    except ValueError:
        print("Masukkan angka yang valid!")

# Memasukkan data dari file txt ke program
def init_data():
    global data_tanaman #Memakai data_tanaman global
    data_tanaman.clear()
    hash_tanaman.clear()
    kategori_unik.clear()
    raw_data = load_data() #Mengambil data dari file

    for nama, umur, tinggi, kategori, kebutuhan_air in raw_data:
        t = Tanaman(nama,umur,tinggi,kategori,kebutuhan_air)
        data_tanaman.append(t)
        kategori_unik.add(kategori)
        
        key = t.nama.upper()
        if key not in hash_tanaman:
            hash_tanaman[key] = []
        hash_tanaman[key].append(t)

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

    nama = input("\nMasukkan nama tanaman yang ingin dicari: ").strip().upper()
    if nama == "":
        print("Nama tanaman tidak boleh kosong!")
        return

    hasil = hash_tanaman.get(nama.upper(), [])  # Jika key tidak ditemukan: mengembalikan list kosong

    if hasil:
        print("\n(Hasil dari Hash Table - Akses Cepat)\n")
        lihat_tanaman(hasil)

    else:
        print("Tanaman tidak ditemukan!")

## Membatalkan aksi tambah atau hapus terakhir menggunakan Stack
def undo():
    if undo_stack.data:
        aksi = undo_stack.pop()

        # UNDO TAMBAH
        if aksi[0] == "tambah":
            t = aksi[1]
            if t in data_tanaman:
                data_tanaman.remove(t)

            key = t.nama.upper()
            if key in hash_tanaman:
                if t in hash_tanaman[key]:
                    hash_tanaman[key].remove(t)

                if len(hash_tanaman[key]) == 0:
                    del hash_tanaman[key]

        # UNDO HAPUS
        elif aksi[0] == "hapus":
            t = aksi[1]
            index = aksi[2]

            if t not in data_tanaman:
                data_tanaman.insert(index, t)

            key = t.nama.upper()
            if key not in hash_tanaman:
                hash_tanaman[key] = []

            hash_tanaman[key].append(t)

        # UNDO EDIT
        elif aksi[0] == "edit":
            t = aksi[1]

            nama_sekarang = t.nama.upper()

            if nama_sekarang in hash_tanaman:
                hash_tanaman[nama_sekarang].remove()

                if t in hash_tanaman[nama_sekarang]:
                    hash_tanaman[nama_sekarang].remove(t)

                if len(hash_tanaman[nama_sekarang]) == 0:
                    del hash_tanaman[nama_sekarang]

            # Kembalikan data lama
            t.nama = aksi[2]
            t.umur = aksi[3]
            t.tinggi = aksi[4]
            t.kategori = aksi[5]
            t.kebutuhan_air = aksi[6]

            key_lama = t.nama.upper()

            if key_lama not in hash_tanaman:
                hash_tanaman[key_lama] = []

            hash_tanaman[key_lama]

        simpan_data(data_tanaman)
        tambah_riwayat("Undo aksi terakhir")
        print(f"Undo {aksi[0]} berhasil.")

    else:
        print("Tidak ada aksi untuk di-undo!")

# Membangun struktur Tree berdasarkan kategori tanaman
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

# Menampilkan struktur kategori tanaman dalam bentuk Tree
def tampil_kategori():
    if not data_tanaman:
        print("\nBelum ada data tanaman!")
        return

    print("\n=== Kategori Tanaman ===")
    akar = bangun_tree()   # bangun tree dari data terkini
    akar.tampil()

# Menampilkan total kebutuhan air menggunakan fungsi rekursif
def lihat_total_air():
    total = total_kebutuhan_air(data_tanaman)
    print(f"\nTotal kebutuhan air {total} liter")

# Menampilkan daftar kategori
def tampilkan_daftar_kategori():
    print("\n--Daftar kategori--\n")

    for k in list(kategori_unik):
        print(f">{k}")

# Filter per kategori
def filter_kategori():
    if not data_tanaman:
        print("Data masih kosong!")
        return

    tampilkan_daftar_kategori()
    pilih = input("\nPilih kategori (ketik): ").strip().capitalize()

    temp = []
    for t in data_tanaman:
        if t.kategori.strip().capitalize() == pilih:
            temp.append(t)

    if temp:
        lihat_tanaman(temp)

    else:
        print(f"\nTidak ada tanaman dengan kategori {pilih}")