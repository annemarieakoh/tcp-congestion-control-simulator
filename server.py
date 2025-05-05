import socket
import random
import time

HOST = '127.0.0.1'
PORT = 12345
PACKET_LOSS_RATE = 0.2  # 20% packet loss simulation

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)
print(f"Server listening on {HOST}:{PORT}")

conn, addr = server_socket.accept()
print(f"Connected by {addr}")

while True:
    try:
        data = conn.recv(1024)
        if not data:
            print("Connection closed by client.")
            break

        if random.random() < PACKET_LOSS_RATE:
            print("Packet lost!")
            continue

        # Split and clean packet stream
        for packet in data.decode().split("Packet "):
            if packet.strip():
                print(f"Received: Packet {packet.strip()}")

        time.sleep(0.5)
        conn.sendall(b"ACK")


    except ConnectionResetError:
        print("Connection reset by client.")
        break
    except ConnectionAbortedError:
        print("Connection aborted by client.")
        break

conn.close()
server_socket.close()
