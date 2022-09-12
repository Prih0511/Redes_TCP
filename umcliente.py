import socket

SERVIDOR_IP = "127.0.0.1"
PORTA = 8000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((SERVIDOR_IP, PORTA))
    s.sendall(b"Oi pessoal!")
    data = s.recv(1024)

print(f"received {data!r}")