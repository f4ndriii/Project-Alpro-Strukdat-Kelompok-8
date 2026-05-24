def simpan_data(data):
    #Membuka file tanaman.txt dalam mode write (menimpa isi file lama)
    with open("data/tanaman.txt", "w") as f:
        for t in data:
            f.write(f"{t.nama},{t.umur},{t.tinggi}\n") #Menyimpan data dengan format nama,umur,tinggi

def load_data():
    data = []
    try:
        #Membuka file dalam mode read
        with open("data/tanaman.txt", "r") as f:
            for line in f:
                nama, umur, tinggi = line.strip().split(",") #Menghapus enter dan pisahkan berdasarkan koma
                data.append((nama, int(umur), int(tinggi))) #Simpan ke list sebagai tuple 
    except:
        print("File belum ada, data kosong.")

    return data

