def bubble_sort_umur(data):
    n = len(data)
    for i in range(n):
        for j in range(0, n-i-1):
            if data[j].umur > data[j+1].umur:
                data[j], data[j+1] = data[j+1], data[j]
    return data

def bubble_sort_tinggi(data):
    n = len(data)
    for i in range(n):
        for j in range(0, n-i-1):
            if data[j].tinggi > data[j+1].tinggi:
                data[j], data[j+1] = data[j+1], data[j]
    return data

def cari_nama(data, nama):
    hasil = []
    for item in data:
        if item.nama.lower() == nama.lower():
            hasil.append(item)
    return hasil

def total_kebutuhan_air(data, index=0):
    if index == len(data):
        return 0
    # Melakukan rekursi untuk menghitung total kebutuhan air
    return data[index].kebutuhan_air + total_kebutuhan_air(data, index+1)