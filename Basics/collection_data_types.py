'''
Data Collection terdapat 4 yaitu list, tuple, set dan dictionary 
'''

print("=========================List=============================")
data = ["Hikmal", 22, True, 3.56]
print(data[0])
print(data[1])
print(data[2])
print(data[3])

# Bersifat mutable
data[0] = "Afandi"
print(data)

brand_mobil = ["toyota", "honda", "suzuki", "daihatsu", "mitsubishi", "wuling", "hyundai"]
print(brand_mobil[0:3:1])
print(brand_mobil[1:])
print(brand_mobil[:5])

print("=========================Tuple=============================")
variable_tuple = ("Afandi", 23, False, "Bandung")

# Bersifat imutable
#variable_tuple[0] = "Hikmal" # akan error

print(variable_tuple)
print(variable_tuple[0:3:1])

print("=========================Set=============================")
# Set tidak memiliki indeks sehingga tidak bisa diakes melalui indexing
# Set tidak memiliki data yang sama
# Set bisa di gabungkan dan dicari irisannya

set1 = {1, 2, 4, 5, 7, "Hikmal"}
set2= {1, 3, 4, 7, "Afandi", "Hikmal"}
print(type(set1))
print(type(set2))

union = set1.union(set2)
print(union)

intersection = set1.intersection(set2)
print(intersection)

print("=========================Dictionary=============================")
# Dictionary adalah tipe data collection pada python yang memiliki pasangan key dan value
# Mengakses value nay dengan key

dict1 = {'name': "hikmal", 'age': 23, 'address': "Bandung"}
print(type(dict1))

# Mengakses value dengan key
print(dict1['name'])

# Menambahkan element baru
dict1['job'] = 'Web Developer'
print(dict1)

#Menghapus element
del dict1['age']
print(dict1)

#Mengubah value
dict1['job'] = 'Machine Learning Engineer'
print(dict1)