def simpan_data(data):
    #Membuka file tanaman.txt dalam mode write (menimpa isi file lama)
    with open("data_tanaman.txt", "w") as f:
        for t in data:
            f.write(f"{t.nama},{t.umur},{t.tinggi},{t.kategori}\n") #Menyimpan data dengan format nama,umur,tinggi

def load_data():
    data = []
    try:
        #Membuka file dalam mode read
        with open("data_tanaman.txt", "r") as f:
            for line in f:
                nama, umur, tinggi, kategori = line.strip().split(",") #Menghapus enter dan pisahkan berdasarkan koma
                data.append((nama, int(umur), int(tinggi), str(kategori))) #Simpan ke list sebagai tuple 
    except:
        print("File belum ada, data kosong.")

    return data

