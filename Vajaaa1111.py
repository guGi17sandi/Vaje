x = int(input("Vnesite stevilo x: "))

if x > 1:
    for i in range(2, x):
        if x % i == 0:
            print(f"Stevilo {x} ni prastevilo")
            break
    else:
        print(f"Stevilo {x} je prastevilo")
else:
    print(f"Stevilo {x} ni prastevilo")