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
        print("🗑️ Data berhasil dihapus!")
    except:
        print("❌ Input tidak valid!")

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

        print("✏️ Data berhasil diupdate!")
    except:
        print("❌ Input tidak valid!")

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