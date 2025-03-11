x = int(input("Vnesi x: "))
y = 0
for i in range (1, x):
    if x % i == 0:
        print(i)
        y = y + i

print(f"Vsota deljiteljev je {y}")

if x == y:
    print(f"število {x} je popolno število")

else:
    print(f"število {x} ni popolno število")