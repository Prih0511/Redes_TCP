import socket

SERVIDOR_IP = "127.0.0.1"
PORTA = 8000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((SERVIDOR_IP, PORTA))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print("O Cliente" ,addr, "se conectou.")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)