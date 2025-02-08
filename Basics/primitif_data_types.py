'''
Pada python secara garis besar terdapat 2 tipe data yaitu data primitif dan data collection.
Data primitif: number(integer, float, complex), boolean(true, false), string
'''
print("=======================DATA PRIMITIF============================")
print("=======================NUMBER============================")
a = 1
b = 1.0
c = 1 + 2j
print(type(a))
print(type(b))
print(type(c))

print("=======================Boolean============================")
d = True
e = False
print(type(d))
print(type(e))

print("=======================STRING============================")
f = "hikmal"
print(type(f))

print("Mengakses per indeks pada indeks 0 yaitu", f[0])
print(type(f[0]))

print("====MENAMPILKAN STRING====")
print("====FORMATTED STRING====")
name = "hikmal"
print(f"Nama saya {name}")

print("==== % FORMATTING STRING====")
print("Nama saya %s" % (name))

print("====STR.FORMAT STRING====")
print("Nama saya {}".format(name))