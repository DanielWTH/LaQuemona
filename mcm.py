n = int(input("Primer numero:   "))
m = int(input("Segundo numero:  "))

i = 2
while True:
    act1 = n * i
    if act1 % m == 0:
        print(f"el mcm es {act1}")
        break

    act2 = m * i
    if act2 % n == 0:
            print(f"el mcm es {act2}")
            break
    i += 1
    
