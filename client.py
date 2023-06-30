import socket
# import dotenv

HOST = '127.0.0.1'
PORT = 8534


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        inp = input("masukkan data: ")
        if not inp:
            break
        s.sendall(bytes(inp, 'utf-8'))
        data = s.recv(1024)
        print(f"Received {data!r}")