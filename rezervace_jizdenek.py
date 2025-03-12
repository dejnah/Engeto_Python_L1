# Program bude umět:

# 1. **Pozdravit** uživatele,
# 2. **Vypsat** nabídku,
# 3. Dovolit uživateli **zadat vstupní data**,
# 4. **Zpracovat** vstupní data,
# 5. **Vypsat** zpracovaná data.

mesta = ["Praha", "Viden", "Olomouc", "Svitavy", "Zlin", "Ostrava"]
ceny = (150, 200, 120, 120, 100, 180)
cara = "=" * 35
nabidka = """1 - Praha   | 150
2 - Viden   | 200
3 - Olomouc | 120
4 - Svitavy | 120
5 - Zlin    | 100
6 - Ostrava | 180"""

#VITEJTE U NASI APLIKACE DESTINATIO!
#===================================

pozdrav = "VITEJTE U NASI APLIKACE DESTINATIO!"
pocet = len(pozdrav)
cara = "=" * pocet

print(pozdrav)
print(cara)
print(nabidka)
print(cara)

destinace = int(input("CISLO DESTINACE:"))
jmeno = input("JMENO:")
prijmeni = input("PRIJMENI:")
email = input("EMAIL:")
rok_narozeni = input("ROK NAROZENI:")

print(cara)
print(mesta[destinace - 1])
print(ceny[destinace-1])
print(cara)
print("Děkuji,", jmeno, "za objednávku,")
print("Cíl. destinace:", mesta[destinace - 1], "cena jízdného:", ceny[destinace-1])
print("na tvůj e-mail", email, "jsme ti poslali lístek.")
print(cara)
