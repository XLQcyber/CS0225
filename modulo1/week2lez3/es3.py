#richiesta numero per la tabellina
numero= int(input("inserisci il numero che vorresti la tabellina: "))
#risultato tabellina
for i in range(1,11):
    print(f"{ numero} x {i} = {numero * i}")