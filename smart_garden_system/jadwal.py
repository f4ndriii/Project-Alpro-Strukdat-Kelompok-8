from struktur_data import Queue
antrian = Queue()  # Queue digunakan untuk menyimpan antrean jadwal penyiraman (FIFO)
from tanaman import data_tanaman

#Menambahkan Jadwal Penyiraman 
def tambah_jadwal():
    nama = input("Masukkan nama tanaman : ").strip()
    if nama == "":
        print("Nama tidak boleh kosong!")
        return

    # Memastikan nama tanaman sudah ada
    ditemukan = False
    for t in data_tanaman:
        if t.nama.upper() == nama.upper():
            ditemukan = True
            break

    if not ditemukan:
        print("Tanaman tidak ditemukan di data!")
        return

    waktu = input("Masukkan waktu (HH:MM): ").strip()
    if waktu == "":
        print("Waktu tidak boleh kosong!")
        return

    # cek format sederhana
    if ":" not in waktu:
        print("Format harus HH:MM!")
        return

    jam, menit = waktu.split(":")

    # cek angka
    if not (jam.isdigit() and menit.isdigit()):
        print("Jam dan menit harus angka!")
        return

    jam = int(jam)
    menit = int(menit)

    # cek range waktu
    if jam < 0 or jam > 23 or menit < 0 or menit > 59:
        print("Waktu tidak valid!")
        return
        
    # Jadwal dimasukkan ke antrean penyiraman
    antrian.enqueue((nama, waktu))
    print(f"Jadwal penyiraman untuk {nama} pada {waktu} berhasil ditambahkan!")

#proses penyiraman
def proses_jadwal():
    if antrian.data:
        nama, waktu = antrian.dequeue()
        print(f"Menyiram {nama} pada {waktu}...")
    else:
        print("Tidak ada jadwal penyiraman!")

#Melihat Jadwal Penyiraman
def lihat_jadwal():
    print("\n=== Jadwal Penyiraman ===")
    if antrian.data:
        for i, (nama, waktu) in enumerate(antrian.data, start=1):
            print(f"{i}. {nama} - {waktu}")
    else:
        print("Tidak ada jadwal penyiraman!")