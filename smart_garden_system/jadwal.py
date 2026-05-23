from struktur_data import Queue
antrian = Queue()

#Menambahkan Jadwal Penyiraman
def tambah_jadwal():
    nama = input("Masukkan nama tanaman : ")
    waktu = input("Masukkan waktu (misal: 08:00): ")
    antrian.enqueue((nama, waktu))
    print(f"✅ Jadwal penyiraman untuk {nama} pada {waktu} berhasil ditambahkan!")

#proses penyiraman
def proses_jadwal():
    if antrian.data:
        nama, waktu = antrian.dequeue()
        print(f"💧 Menyiram {nama} pada {waktu}...")
    else:
        print("❌ Tidak ada jadwal penyiraman!")

#Melihat Jadwal Penyiraman
def lihat_jadwal():
    print("\n=== Jadwal Penyiraman ===")
    if antrian.data:
        for i, (nama, waktu) in enumerate(antrian.data):
            print(f"{i}. {nama} - {waktu}")
    else:
        print("Tidak ada jadwal penyiraman!")