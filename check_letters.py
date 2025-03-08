add_konsonan = 0
add_vokal = 0
vokal = "aiueoAIUEO"

letter = input("Masukkan kata: ")

for i in letter:
    if i in vokal: 
        add_vokal+= 1
    else: 
        add_konsonan+=1

print(f"Jadi huruf konsonannya berjumlah {add_konsonan}")
print(f"Jadi huruf vokalnya berjumlah {add_vokal}")