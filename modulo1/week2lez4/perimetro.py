#scelta perimetro delle figure geometriche da calcolare
figure_geometriche= input("Inserisci il perimetro della figura geometrica che desideri(quadrato, cerchio, rettangolo): ")
#calcoli dei perimetri
if figure_geometriche=="quadrato":
    lato= float(input("inserisci la lunghezza di un lato: "))
    perimetro= 4*lato
    print("il perimetro del quadrato e': ", perimetro)
elif figure_geometriche=="cerchio":
    raggio= float(input("inserisci il raggio del cerchio: "))
    perimetro= 2*3.14*raggio
    print("il perimetro del cerchio e': ", perimetro)
elif figure_geometriche=="rettangolo":
    lato1= float(input("inserisci la lunghezza del primo lato: "))
    lato2= float(input("inserisci la lunghezza del secondo lato: "))
    perimetro= 2*(lato1+lato2)
    print("il perimetro del rettangolo e': ", perimetro)
else:
    print("errore, perimetro non riconosciuto")
