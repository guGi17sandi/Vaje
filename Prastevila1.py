from AppData.Local.Programs.Python.Python313.Lib.operator import truediv

# Uporabnik vnese število, ki ga želimo preveriti
x = int(input("Vnesite število x: "))

# Predpostavimo, da je število prastevilo
je_prastevilo = True

# Preverimo deljivost števila z vsemi števili od 2 do x-1
for i in range(2, x):
    if x % i == 0:  # Če je število deljivo, potem ni prastevilo
        je_prastevilo = False
        break  # Ustavimo preverjanje, ker že vemo, da ni prastevilo

# Izpišemo rezultat
if je_prastevilo and x > 1:  # Število mora biti večje od 1, da je prastevilo
    print(f"Število {x} je prastevilo")
else:
    print(f"Število {x} ni prastevilo")
