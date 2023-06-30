import socket
import logging
# import dotenv

HOST = '127.0.0.1'
PORT = 8534

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print("waiting connection on 127.0.0.1:8534")
    conn, addr = s.accept()
    # TODO: tambahkan verifikasi dengan enkripsi asimetrik
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)