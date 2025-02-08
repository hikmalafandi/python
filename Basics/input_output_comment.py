'''
Membuat aplikasi untuk menginputkan biodata

'''

# Buat pembatas dulu agar program rapih  
print("========================================")
print("==============FORM BIODATA==============")
print("========================================")

name = input("Masukkan nama: ")
age = int(input("Masukkan umur: "))
address = input("Masukkan alamat: ")

print("========================================")

parentName = input("Masukkan nama orang tua / wali: ")
parentAge = int(input("Masukkan umur orang tua / wali: "))
parentAddress = input("Masukkan alamat orang tua / wali: ")

print("========================================")

# Mencari selisih umur parent dan child
result = parentAge - age
print("Selisih umur parent dan anak adalah", result) 
# print(type(age))
# print(type(parentAge))


print("========================================")
