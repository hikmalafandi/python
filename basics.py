##1. Variabel & Tipe Data
# Soal:
#Buat variabel nama yang berisi nama kamu dan variabel umur yang berisi umur kamu.
print("=======================Variabel & Tipe Data=======================")
nama = "hikmal"
umur = "22"

#Hitung luas persegi dengan sisi s = 7.
s = 7
luas_persegi = s * s
print("Luas persegi adalah ", luas_persegi)

#Ubah angka 3.14 (float) menjadi integer.
num = 3.14 
numInt = int(num)
print(type(numInt))


#2. Operasi Matematika
# Soal:
#Hitung hasil dari (10 + 5) * 3 - 8 / 4.
print("=======================Operasi Matematika=======================")
result = (10 + 5) * 3 - 8 / 4
print(result)

#Hitung sisa bagi dari 25 dibagi 4.
resultMod = 25 % 4
print(resultMod)

#Buat program yang menerima dua angka dari pengguna, lalu tampilkan hasil penjumlahan, pengurangan, perkalian, dan pembagian mereka.
a = int(input("Masukkan angka: "))
b = int(input("Masukkan angka: "))
penjumlahan = a + b
pengurangan = a - b
perkalian = a * b
pembagian = a / b

print(penjumlahan)
print(pengurangan)
print(perkalian)
print(pembagian)

# 3. Percabangan (if-else)
# Soal:
# Buat program yang meminta pengguna memasukkan angka. Jika angka lebih dari 10, tampilkan "Angka besar", jika tidak, tampilkan "Angka kecil".
print("=======================Percabangan=======================")
a = int(input("Masukkan angka: "))

if a >= 10 :
    print("Angka Besar")
elif a < 10:
    print("Angka Kecil")


# Periksa apakah suatu angka adalah genap atau ganjil.
bilangan = int(input("Masukkan angka: "))
if (bilangan % 2) == 0 :
    print("Genap")
elif (bilangan % 2) != 0 : 
    print("Ganjil") 

# Buat program yang meminta usia pengguna dan cek apakah dia cukup umur untuk mendapatkan SIM (minimal 17 tahun).
usia = int(input("Masukkan usia: "))
if usia >= 17 :
    print("Sudah cukup umur")
elif usia < 17 :
    print("Belum cukup umur")

# 4. Looping (for & while)
# Soal:
# Cetak angka 1 sampai 10 menggunakan for loop.
print("=======================Pengulangan=======================")
for i in range(1, 11):
    print(i)

# Cetak angka 10 sampai 1 menggunakan while loop.
i = 10
while(i >= 1):
    print(i)
    i-= 1

# Hitung jumlah dari semua angka 1 sampai 100 menggunakan loop.
total = 0
for i in range(1, 101):
    total = total + i 

print("Jumlah dari semua angka 1 sampai 100 adalah ", total)


# 5. List & Dictionary
# Soal:
# Buat list berisi 5 nama temanmu dan cetak nama ketiga.
print("=======================List & Dictionary=======================")
teman = ['zidan', 'ardy', 'andhyka', 'dimas', 'agus']
print(teman[2])

# Buat dictionary dengan key 'nama', 'umur', 'hobi', lalu cetak salah satu nilainya.
profile = {'nama': 'hikmal', 'umur': 22, 'hobi': 'coding'}
print(profile['nama'])

# Tambahkan nama baru ke dalam list yang sudah kamu buat tadi.
teman.append('farhan')
print(teman[5])


# 6. Fungsi (Function)
# Soal:
# Buat fungsi yang menerima dua angka dan mengembalikan hasil perkaliannya.
print("=======================Function=======================")
input1 = int(input('Masukkan angka: '))
input2 = int(input('Masukkan angka: '))

def perkalian(a, b):
    return a * b

result = perkalian(input1, input2)
print(f"Hasil perkalian antara {input1} dan {input2} adalah ", result)

# Buat fungsi untuk menghitung luas lingkaran dengan jari-jari sebagai parameter.
jari = int(input("Masukkan jari - jari: "))

def luas_lingkaran(r):
    return 3.14 * r**2

luas = luas_lingkaran(jari)
print(f"Luas lingkaran dengan jari - jari {jari} adalah ", luas)

# Buat fungsi yang menerima nama sebagai input, lalu mencetak "Halo, [nama]!".
nama = input("Masukkan nama: ")

def cetak_halo(n):
    return f"Halo, {n}!"

cetak_nama = cetak_halo(nama)
print(cetak_nama)