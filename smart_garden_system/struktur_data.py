# Implementasi Stack untuk fitur Undo (LIFO)
class Stack:
    def __init__(self):
        self.data = []
    
    def push(self, item):
        self.data.append(item)

    def pop(self):
        if self.data:
            return self.data.pop()
        return None

# Implementasi Queue untuk antrean jadwal penyiraman (FIFO)    
class Queue:
    def __init__(self):
        self.data = []
    
    def enqueue(self, item):
        self.data.append(item)

    def dequeue(self):
        if self.data:
            return self.data.pop(0)
        return None
    
    def tampil(self):
        for item in self.data:
            print(item)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Single Linked List untuk menyimpan riwayat aktivitas
class LinkedList:
    def __init__(self):
        self.head = None

    def tambah(self, data):
        node_baru = Node(data)
        #Jika linked list kosong
        if not self.head:
            self.head = node_baru
        #Jika sudah ada isi
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node_baru

    def tampil(self):
        #Menampilkan seluruh isi linked list
        current = self.head
        while current:
            print(current.data)
            current = current.next

class DNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def tambah(self, data):
        node = DNode(data)

        if self.head is None:
            self.head = self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node

    def tampil_maju(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def tampil_mundur(self):
        current = self.tail
        while current:
            print(current.data)
            current = current.prev

#Tree untuk mengelompokkan tanaman berdasarkan kategori
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

    def tambah_anak(self, node):
        self.children.append(node)

    def tampil(self, level=0):
        #Menampilkan tree secara bertingkat
        print("  " * level + self.data)
        for child in self.children:
            child.tampil(level + 1)