maximo = int(input("Numero de filas que desea:  "))
fila = 0
while fila <= maximo:
    columna = 0
    espacios = " " * (maximo - fila)
    while columna <= fila:
        print(espacios + f"({fila} , {columna})", end = " ")
        columna += 1
    fila += 1
    print("")

