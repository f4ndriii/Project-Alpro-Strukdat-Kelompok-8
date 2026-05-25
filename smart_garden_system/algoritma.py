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
    for item in data:
        if item.nama.lower() == nama.lower():
            return item
    return None
