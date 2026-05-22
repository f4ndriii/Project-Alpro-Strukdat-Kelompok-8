def simpan_data(data):
    with open("data/tanaman.txt", "w") as f:
        for t in data:
            f.write(f"{t.nama},{t.umur},{t.tinggi}\n")

def load_data():
    data = []
    try:
        with open("data/tanaman.txt", "r") as f:
            for line in f:
                nama, umur, tinggi = line.strip().split(",")
                data.append((nama, int(umur), int(tinggi)))
    except:
        print("File belum ada, data kosong.")

    return data

