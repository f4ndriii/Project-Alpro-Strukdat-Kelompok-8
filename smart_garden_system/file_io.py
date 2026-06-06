def simpan_data(data):
    with open("data/tanaman.txt", "w") as f:
        for t in data:
            f.write(f"{t.nama},{t.umur},{t.tinggi},{t.kategori},{t.kebutuhan_air}\n")

def load_data():
    data = []
    try:
        #Membuka file dalam mode read
        with open("data/tanaman.txt", "r") as f:
            for line in f:
                nama, umur, tinggi, kategori, kebutuhan_air = line.strip().split(",") #Menghapus enter dan pisahkan berdasarkan koma
                data.append((nama, int(umur), int(tinggi), str(kategori), int(kebutuhan_air))) #Simpan ke list sebagai tuple 
    except FileNotFoundError:
        print("File belum ada, data kosong.")

    return data

