import datetime
def assistente_virtuale(comando):                       
    if comando == "Qual è la data di oggi?":
         ##Mettere una legenda dei comandi che l'utente può chiedere all'assistente virtuale o fornire la lista di comandi quando l'utente inserisce 
         # comandi che l'assistente non riconosce.(errore logico perche' senza una lista di comandi gli da solo la risposta "Non ho capito la tua domanda"
        oggi = datetime.date.today()  
        #manca il punto in mezzo datetoday per far funzionare la funzione today dentro la classe date del modulo (errore di sintassi)       
        risposta = "La data di oggi è " + oggi.strftime("%d/%m/%Y")
    elif comando == "Che ore sono?":
        ora_attuale = datetime.datetime.now().time()
        risposta = "L'ora attuale è " + ora_attuale.strftime("%H:%M")
    elif comando == "Come ti chiami?":
        risposta = "Mi chiamo Assistente Virtuale"
    else:
        risposta = "Non ho capito la tua domanda."
    return risposta
# Messaggio di benvenuto e guida
print("Ciao! Sono il tuo Assistente Virtuale. Puoi farmi domande come Qual è la data di oggi?, Che ore sono? e Come ti chiami?.")
print("Per uscire, digita 'esci'.")
while True:                       
  #manca i due punti : al termine della riga (errore di sintassi) 
    comando_utente = input("Cosa vuoi sapere? ")
    if comando_utente.lower() == "esci":
         ##manca un messaggio di informazione all'utente per uscire dal ciclo while (errore di logica perche'                   
        #l'utente non sa che esiste il comando "esci" per uscire dal ciclo while
        print("Arrivederci!")
        break
    else:
        print(assistente_virtuale(comando_utente))