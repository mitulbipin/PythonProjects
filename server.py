import socket

HOST = '127.0.0.1'
PORT = 8888

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    conn, adrr = s.accept()
    with conn:
        print('Accepting connection', adrr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)