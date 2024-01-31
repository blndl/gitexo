while 1:
    nbr = input("Entrez un nombre pour lancer le programme ou autre chose pour fermer\n")
    if nbr.isnumeric() == False:
        break
    i = 0
    while i <= 10:
        print(int(nbr) * i)
        i += 1