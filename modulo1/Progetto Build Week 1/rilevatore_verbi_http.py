import requests

# Chiediamo all'utente di inserire l'indirizzo del sito da controllare
url = input("Inserisci l'URL da controllare (esempio: http://192.168.1.1): ")

# Inviamo una richiesta HTTP di tipo OPTIONS per sapere quali metodi sono supportati
response = requests.options(url)

# Controlliamo se nella risposta è presente l'header 'Allow'
# Questo header contiene i metodi HTTP supportati dal server (es: GET, POST, ecc.)
if 'Allow' in response.headers:
    metodi_supportati = response.headers['Allow']
else:
    metodi_supportati = ""

# Creiamo una lista dei metodi che vogliamo verificare
metodi_da_testare = ["GET", "POST", "PUT", "DELETE"]

# Stampiamo il risultato per ogni metodo
print("\nRisultato:")
for metodo in metodi_da_testare:
    if metodo in metodi_supportati:
        print(f"{metodo} - supportato")
    else:
        print(f"{metodo} - non supportato")