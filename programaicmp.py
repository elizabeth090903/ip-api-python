from scapy.all import *

destino_ip = "8.8.8.8"  

respuesta = sr1(IP(dst=destino_ip)/ICMP(), timeout=2, verbose=0)

if respuesta:
    print("Respuesta recibida:")
    respuesta.show()
else:
    print("No se recibió respuesta.")
