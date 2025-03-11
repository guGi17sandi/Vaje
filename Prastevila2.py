n = int(input("Vnesite stevilo n: "))
prastevila = []

for x in range(2, n + 1):
    je_prastevilo = True
    for i in range(2, x):
        if x % i == 0:
            je_prastevilo = False
            break
    if je_prastevilo:
        prastevila.append(x)

print("Prastevila med 1 in", n, ":", prastevila)