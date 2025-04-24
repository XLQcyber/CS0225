import socket

target = input("inserisci un ip da scannerizzare: ")
portrange = input("inserisci un range di porte da scannerizzare (es 8-210): ")

lowport = int(portrange.split("-")[0])
highport = int(portrange.split("-")[1])

print("host da scannerizzare", target, "da porta", lowport, "a porta", highport)

for port in range (lowport, highport):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    status = s.connect_ex((target, port))
    if (status== 0):
        print("port", port, "-open ")
    else:
        print("port", port, "-closed ")
    s.close()