while True:
    agno = int(input("Agno a analizar: "))

    if agno == 0: break

    if (agno % 4 == 0 and agno % 100 != 0) or (agno % 4 == 0 and agno % 400 == 0):
        print("Su agno es bisiesto")
    else:
        print("Su agno no es bisiesto")